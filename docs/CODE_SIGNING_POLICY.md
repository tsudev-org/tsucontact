# Code signing policy

Tsu Contact is free, open-source software (Apache-2.0) by [TsuDEV](https://tsudev.com). This page describes how its Windows
release files are built and signed.

## Signing provider

Status: the project intends to apply to the SignPath Foundation for free code signing; release files are not
Authenticode-signed yet. Once the project is accepted, every Windows release will be signed and this section will read:

> Free code signing provided by [SignPath.io](https://about.signpath.io), certificate by [SignPath Foundation](https://signpath.org)

## What is signed

Only files built from this repository by the release workflow
[`build-release-win.yml`](https://github.com/tsudev-org/tsucontact/blob/main/.github/workflows/build-release-win.yml) on
GitHub Actions, from a version tag `vYY.M.DDNN`:

- `tsucontact.exe`: the application, built with PyInstaller from this repository's sources. The PyInstaller bootloader is
  compiled from its source on the build runner.
- `tsucontact_<version>_windows-x64-setup.exe`: the Inno Setup installer built from
  [`packaging/inno/tsucontact.iss`](https://github.com/tsudev-org/tsucontact/blob/main/packaging/inno/tsucontact.iss).

Third-party binaries bundled with the application (the Python runtime, Qt for Python / PySide6 libraries) are upstream
files. They are listed in the SBOM attached to each release and are not signed as our own. Release files carry the product
name `Tsu Contact` / `tsucontact` and a file version equal to the release version.

## Team roles

| Role | Who |
| --- | --- |
| Authors (committers) | Members of the [tsudev-org](https://github.com/orgs/tsudev-org/people) GitHub organization with write access to this repository |
| Reviewers | Repository maintainers. Every change reaches `main` through a pull request; the branch ruleset requires passing CI (lint, tests on Linux and Windows, secret scanning, standards check) and resolved review conversations |
| Approvers | Owners of the tsudev-org organization. Each signing request is approved manually, one release at a time |

All team members use multi-factor authentication. Two-factor authentication is enforced for every member of the
tsudev-org GitHub organization, and is required for SignPath accounts.

## Privacy

This program will not transfer any information to other networked systems unless specifically requested by the user or
the person installing or operating it.

Tsu Contact runs fully offline: the network module of Qt is excluded from the build, there is no telemetry and no update
check. Contact data stays in memory and is written only to files the user chooses. Web links (for example the project
website) open in the user's browser only when the user clicks them. Privacy policy:
[tsudev.com/privacy](https://tsudev.com/privacy). Security architecture:
[contact.tsudev.com/bao-mat/kien-truc/](https://contact.tsudev.com/bao-mat/kien-truc/).

## System changes and uninstall

The installer installs per user (no administrator rights) into the user's programs folder, adds a Start Menu shortcut
and an optional desktop shortcut, and registers a standard uninstall entry (Settings, Apps). It does not change system
settings, does not start with Windows and does not install services. Uninstalling removes the program files; the only
settings file, `%LOCALAPPDATA%\tsucontact\settings.json`, can be deleted by hand. A portable zip with the same
application is also published.

## Verifying a download

- `SHA256SUMS.txt` lists the hash of every release file and is signed with Sigstore (`SHA256SUMS.txt.sigstore.json`).
- Build provenance (SLSA): `gh attestation verify <file> --repo tsudev-org/tsucontact`.
- Every release file is scanned on VirusTotal before the release is published; report links are in the release notes.

## Reporting a problem

Report a security problem or a suspected mis-signed file privately as described in
[SECURITY.md](https://github.com/tsudev-org/tsucontact/blob/main/SECURITY.md). The team will cooperate with any
investigation by SignPath Foundation.
