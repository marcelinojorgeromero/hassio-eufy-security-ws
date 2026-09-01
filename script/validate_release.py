#!/usr/bin/env python3
"""Validate the add-on metadata and its immutable WebSocket release artifact."""

from __future__ import annotations

import hashlib
import re
import tempfile
import urllib.request
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ADDON = ROOT / "eufy-security-ws"


def fail(message: str) -> None:
    raise SystemExit(f"release validation failed: {message}")


def main() -> None:
    config = yaml.safe_load((ADDON / "config.yaml").read_text(encoding="utf-8"))
    build = yaml.safe_load((ADDON / "build.yaml").read_text(encoding="utf-8"))

    version = str(config.get("version", ""))
    architectures = config.get("arch", [])
    build_from = build.get("build_from", {})
    args = build.get("args", {})
    package_url = str(args.get("EUFY_SECURITY_WS_PACKAGE_URL", ""))
    expected_sha256 = str(args.get("EUFY_SECURITY_WS_PACKAGE_SHA256", "")).lower()

    if not version:
        fail("config.yaml has no version")
    if sorted(architectures) != ["aarch64", "amd64"]:
        fail(f"unexpected architecture list: {architectures!r}")
    if any(arch not in build_from for arch in architectures):
        fail("build.yaml does not define a base image for every architecture")
    if f"/v{version}/" not in package_url or not package_url.endswith(
        f"eufy-security-ws-{version}.tgz"
    ):
        fail("package URL and add-on version do not match")
    if not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
        fail("package SHA-256 is not a lowercase 64-character digest")

    with tempfile.TemporaryDirectory(prefix="eufy-ws-release-") as temporary_directory:
        archive = Path(temporary_directory) / "eufy-security-ws.tgz"
        with urllib.request.urlopen(package_url, timeout=60) as response, archive.open("wb") as target:
            while chunk := response.read(1024 * 1024):
                target.write(chunk)
        actual_sha256 = hashlib.sha256(archive.read_bytes()).hexdigest()

    if actual_sha256 != expected_sha256:
        fail(f"artifact checksum mismatch: expected {expected_sha256}, got {actual_sha256}")

    print(f"validated add-on {version}: {actual_sha256}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, yaml.YAMLError) as error:
        fail(str(error))
