<img src="website/public/brand/logo-contact.png" alt="Tsu Contact logo" height="96">

# Tsu Contact

[Tiếng Việt](README.md) · **English**

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/16836/badge)](https://www.bestpractices.dev/projects/16836)

A desktop tool that converts **CSV contact lists to vCard (.vcf)** for importing into phones. It runs fully offline on
your computer: no account, no telemetry, no network access at all.

A [TsuDEV](https://tsudev.com) product. Website: <https://contact.tsudev.com>. Formerly named `tsudev-contact`
(renamed 16/11/2026, [ADR-0001](docs/adr/0001-ten-san-pham-tsu-contact.md)); old repository links redirect here.

## Install (Windows 10/11 x64)

With [Scoop](https://scoop.sh) (verifies SHA-256, updates automatically):

```powershell
scoop bucket add tsudev https://github.com/tsudev-org/scoop-bucket
scoop install tsudev/tsucontact
```

Or download `tsucontact_<version>_windows-x64-setup.exe` from the [latest release](https://github.com/tsudev-org/tsucontact/releases/latest).
It is a single portable executable; no Python needed. Verify it before running:

```powershell
Get-FileHash .\tsucontact_<version>_windows-x64-setup.exe -Algorithm SHA256   # compare with SHA256SUMS.txt
gh attestation verify .\tsucontact_<version>_windows-x64-setup.exe --repo tsudev-org/tsucontact
gh attestation verify .\SHA256SUMS.txt --repo tsudev-org/tsucontact    # SHA256SUMS is Sigstore-signed
```

The executable is not yet Authenticode-signed, so Windows SmartScreen may warn on first run.

## Features

- Drag and drop a CSV file; encoding (UTF-8, UTF-16, Windows-1258) and delimiter are detected automatically.
- Automatic column mapping for Vietnamese/English headers and Google Contacts exports, with sample values.
- Row-by-row validation: Vietnamese phone number normalisation (`+84`, leading zeros dropped by Excel, several numbers
  in one cell), e-mail, birthdays (including Excel serial dates), duplicate detection.
- vCard 3.0 output per RFC 6350 (Android, iPhone, Google Contacts, Outlook) and an error report CSV.
- Hardened against vCard and CSV formula injection; contact data stays in memory only.
- Vietnamese (default) and English UI; Light / Dark / System themes.

## Development

```bash
python -m venv .venv && . .venv/bin/activate
pip install --require-hashes --no-deps -r requirements.txt -r requirements-dev.txt
QT_QPA_PLATFORM=offscreen python -m pytest -q
python tsucontact.pyw
```

Architecture and threat model: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Reporting vulnerabilities:
[SECURITY.md](SECURITY.md) (private GitHub advisories, never public issues).

## License

[Apache-2.0](LICENSE), see [NOTICE](NOTICE) and [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). The TsuDEV name and
logo are trademarks and are not covered by the license.
