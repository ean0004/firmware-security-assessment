# CA-01 — Firmware Authenticity and Integrity

**Assessment Type:** Conceptual Assessment  
**Reference:** ETSI EN 303 645 V2.1.1 — Provision 5.3-9  
**System Under Assessment:** Python Firmware Update Simulator

### Objective

I aimed to assess whether my firmware update simulator was designed to verify the authenticity and integrity of firmware packages before accepting them.

### Assessment Procedure

- I reviewed the design and Python source code of my firmware update simulator.
- I identified the use of Ed25519 digital signatures to protect firmware packages.
- I examined how the private key is used to sign firmware and how the trusted public key is used to verify signatures.
- I reviewed the requirement for signature verification before a firmware update is accepted.
- I examined the version-checking mechanism designed to prevent firmware downgrades.

### Findings

- The simulator uses a digital signature mechanism intended to detect modifications to signed firmware data.
- The design includes a trusted public key for verifying firmware signatures.
- The verification process is designed to reject firmware with invalid signatures.
- The simulator also includes a version check to prevent installation of older firmware.
- The prototype uses local files for cryptographic key storage and device state, which introduces security limitations compared with a production IoT device.

### Assessment Conclusion

Based on my review of the intended design, I found that the simulator includes appropriate basic mechanisms for firmware authenticity and integrity verification.

However, the prototype does not demonstrate production-grade protection of cryptographic keys or device state. Further assessment would be required before making a full conformance claim.

**Preliminary Verdict:** Conceptually suitable for the defined laboratory scope, with identified limitations.