ARG BUILD_FROM=ghcr.io/home-assistant/base:3.23
FROM $BUILD_FROM

ARG EUFY_SECURITY_WS_PACKAGE_URL
ARG EUFY_SECURITY_WS_PACKAGE_SHA256

WORKDIR /usr/src/app
RUN \
    set -x \
    # The Alpine 3.23 base image (see build.yaml) ships Node.js 24 in its main
    # repository, so nodejs/npm install directly with no edge-repo workarounds.
    && apk add --no-cache \
        jq \
        nodejs \
        npm \
    && node --version \
    # Fail the build if the base ever regresses below Node 24.
    && case "$(node --version)" in v24.*) ;; *) echo "Expected Node 24, got $(node --version)" >&2; exit 1 ;; esac \
    && wget -O /tmp/eufy-security-ws.tgz "${EUFY_SECURITY_WS_PACKAGE_URL}" \
    && echo "${EUFY_SECURITY_WS_PACKAGE_SHA256}  /tmp/eufy-security-ws.tgz" | sha256sum -c - \
    && npm install --force /tmp/eufy-security-ws.tgz \
    && rm -f /tmp/eufy-security-ws.tgz

COPY run.sh /
RUN chmod a+x /run.sh
WORKDIR /data

CMD [ "/run.sh" ]
