# Home Assistant Add-on: Eufy Security WS Compatibility

![Logo][logo]

> [!IMPORTANT]
> Temporary compatibility build using checksum-pinned prerelease packages. It is
> designed to coexist with the official add-on under a different slug, but only one
> add-on may listen on port `3000` at a time. Legacy Eufy inventory APIs are still
> required.

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]

The add-on bridges Eufy events and controls over the schema-21 WebSocket contract used
by the existing Home Assistant Eufy Security integration.

It includes the reviewed Mega/v6 success-code compatibility patch and robust station-IP
option parsing. It is not the unreleased native Mega replacement and is not affiliated
with Eufy.

See the Documentation tab for configuration details.

[logo]: https://raw.githubusercontent.com/bropat/hassio-eufy-security-ws/master/eufy-security-ws/logo.png
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
