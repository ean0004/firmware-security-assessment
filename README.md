# Secure Firmware Update & Cybersecurity Conformance Assessment

## Project Overview

This project demonstrates the development and security assessment of a Python-based firmware update simulator.

The aim was to evaluate firmware authenticity, integrity verification and downgrade protection through practical security testing.

The project references selected security principles from ETSI EN 303 645 and uses three assessment approaches:

- Conceptual Assessment
- Functional Completeness Assessment
- Functional Sufficiency Assessment

## Technologies Used

- Python
- Cryptography (Ed25519 digital signatures)
- Visual Studio Code
- PowerShell
- JSON
- GitHub

## Security Testing

| Test ID | Test Description | Result |
|---|---|---|
| FW-01 | Valid Signed Firmware Update | PASS |
| FW-02 | Tampered Firmware Detection | PASS |
| FW-03 | Firmware Downgrade Protection | PASS |
| FW-04 | Unsigned Firmware Rejection | PASS |

All four tests produced the expected outcomes under the tested conditions.

## Assessment Methodology

**Conceptual Assessment:** Reviewed the security design, including cryptographic key generation, firmware signing and signature verification.

**Functional Completeness Assessment:** Examined the Python implementation to identify which security functions were present and which remained unimplemented.

**Functional Sufficiency Assessment:** Evaluated the implemented security mechanisms using four practical firmware update tests.

## Key Findings

The simulator demonstrated basic firmware authenticity and integrity verification. However, several limitations were identified:

- The simulator records firmware versions rather than installing real firmware binaries.
- The private signing key is stored locally without encryption.
- The recorded firmware version is not protected against direct file modification.
- The testing covers selected scenarios rather than all possible security threats.

## Running the Project

1. Install Python.
2. Create a virtual environment.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Run `python firmware_lab.py init`.
5. Create a signed package using `python firmware_lab.py build 2 "security patch" update_v2.json`.
6. Install it using `python firmware_lab.py install update_v2.json`.
7. Check the version using `python firmware_lab.py status`.

## Documentation

The `documentation/` folder contains the technical assessments and final project report.

The `evidence/` folder contains screenshots collected during development and security testing.

## Disclaimer

This is an independent educational cybersecurity project. It is not an official product certification or a complete ETSI EN 303 645 conformance assessment.