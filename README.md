# Eufy Security WS Compatibility add-on repository

> [!IMPORTANT]
> This fork is a temporary compatibility build for existing Home Assistant
> installations. It uses pinned, checksum-verified prerelease packages and includes
> narrowly reviewed Mega/v6 transition fixes. It remains dependent on the legacy
> inventory APIs described below and is not affiliated with Eufy.

> [!CAUTION]
> # 🚨🚨🚨 LIBRARY DEPRECATION NOTICE 🚨🚨🚨
>
> ### ⚠️ Eufy is shutting down the legacy APIs this library is built on. ⚠️
>
> Eufy is in the middle of a large migration of their ecosystem. The newer **Eufy Mega**
> platform (the "5-in-1" app, covering Security / Clean / Lights / Care) is gradually
> becoming the only supported backend, and Eufy has **already started removing access to
> the legacy APIs** this library was originally built on. Until recently both worked in
> parallel — that is no longer guaranteed.
>
> **🔔 What this means for you:**
>
> - 🟢 A recent PR restores **push notifications** against the new v6 ("eufy_mega")
>   backend, so push works again **for now**. This is a short-term stopgap.
> - 🟡 Other functionality that still depends on legacy endpoints may stop working
>   **without warning** as Eufy continues the rollout. The current Eufy app no longer
>   uses the legacy API at all.
> - 🔴 Once the legacy API is fully shut down, **this library will stop functioning** —
>   no amount of patching here will change that.
>
> **🚧 What's next:**
>
> A new integration built around **Eufy Mega** is in active development (auto-discovery,
> less battery drain for P2P), designed from the ground up rather than bolted onto the
> Security-only structure, and coordinated across the Home Assistant, Homebridge and
> Homey communities so the new library works for everyone.
>
> ### 👉 Treat this release as a **temporary stopgap.** 👈
>
> *This notice will be updated as the migration progresses.*

![Logo](docs/_media/eufy-security-ws.png)

![Logo](eufy-security-ws/logo.png)

[![ci][ci-shield]][ci-url] ![Release][release-shield] ![Stars][stars-shield]

Join us on Discord:

<a target="_blank" href="https://discord.gg/5wjQ2asb64"><img src="https://dcbadge.limes.pink/api/server/5wjQ2asb64" alt="" /></a>

## Add-ons

This repository contains the following add-ons

### [eufy-security-ws add-on](./eufy-security-ws/README.md)

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]

## Installation

1. To add this repository to Home Assistant you have 2 options:

   1. Go to **Settings → Add-ons → Add-on store** and click **⋮ → Repositories**, fill in `https://github.com/marcelinojorgeromero/hassio-eufy-security-ws` and click **Add → Close**
   2. click the **Add repository** button below, click **Add → Close** (You might need to enter the **internal IP address** of your Home Assistant instance first).

      [![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fmarcelinojorgeromero%2Fhassio-eufy-security-ws)

2. Stop the official add-on because both use port `3000` by default.
3. Install **Eufy Security WS Compatibility**, enter the configuration, and start it.

## Changelog

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

All notable changes to this project will be documented in the [CHANGELOG.md](eufy-security-ws/CHANGELOG.md) file.

Version for releases is based on [eufy-security-ws](https://github.com/bropat/eufy-security-ws) format: `X.Y.Z`.

Any changes on the addon that do not require a new version of [eufy-security-ws](https://github.com/bropat/eufy-security-ws) will use the format: `X.Y.Z-A` where `X.Y.Z` is fixed on the [eufy-security-ws](https://github.com/bropat/eufy-security-ws) release version and `A` is related to the addon.

## Issues

If you find a compatibility-build issue, use this fork's [issue tracker](https://github.com/marcelinojorgeromero/hassio-eufy-security-ws/issues). The upstream projects are deprecated and no longer process normal feature requests.

Feel free to create a PR for fixes and enhancements.

[ci-shield]: https://github.com/marcelinojorgeromero/hassio-eufy-security-ws/workflows/Publish/badge.svg
[ci-url]: https://github.com/marcelinojorgeromero/hassio-eufy-security-ws/actions?query=workflow%3APublish
[release-shield]: https://img.shields.io/github/v/release/marcelinojorgeromero/hassio-eufy-security-ws.svg
[stars-shield]: https://img.shields.io/github/stars/marcelinojorgeromero/hassio-eufy-security-ws.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg

## Deployment

Instructions aimed at maintainers for deploying a new version: [Deployment](deployment.md)
