# Functional Sufficiency Assessment

## FSA-01 — Valid Firmware Installation

**Objective:** Verify that a valid digitally signed firmware update can be accepted.

**Assessment performed:** I created a digitally signed firmware version 2 package and attempted to install it while the simulator was running version 1.

**Visible evidence:** My terminal displayed `Accepted: firmware version 2 installed`, followed by `{"version": 2}`.

**Result:** PASS.

**Conclusion:** I confirmed that my simulator accepted a valid signed firmware package and updated the recorded version number under the tested conditions.

## FSA-02 — Tampered Firmware Detection

**Objective:** Verify that the simulator detects modifications to a signed firmware package.

**Assessment performed:** I modified the firmware payload from `"original update"` to `"malicious update"` without changing the digital signature.

**Visible evidence:** My terminal displayed `ERROR: Rejected: invalid firmware signature`.

**Result:** PASS.

**Conclusion:** I confirmed that the digital signature verification mechanism detected the modified firmware package and prevented the simulated update.

## FSA-03 — Firmware Downgrade Protection

**Objective:** Verify that older firmware versions cannot be installed through the simulator's update mechanism.

**Assessment performed:** I created a signed firmware version 1 package and attempted to install it while the recorded installed version was 2.

**Visible evidence:** My terminal displayed `ERROR: Rejected: firmware downgrade or replay`, and the recorded firmware version remained at 2.

**Result:** PASS.

**Conclusion:** I confirmed that the version-checking mechanism rejected an older firmware version under the tested conditions.

## FSA-04 — Unsigned Firmware Rejection

**Objective:** Verify that firmware packages without digital signatures cannot be installed.

**Assessment performed:** I created a firmware version 4 package without a signature field and attempted to install it.

**Visible evidence:** My terminal displayed `ERROR: Rejected: invalid firmware signature`, and the recorded firmware version remained at 2.

**Result:** PASS.

**Conclusion:** I confirmed that the simulator rejected the unsigned firmware package without changing the recorded installed version.


## Functional Sufficiency — Limitations

Although all four initial security tests passed, I identified several limitations in my assessment.

- My simulator only records the installed firmware version rather than installing an actual firmware binary.
- My private signing key is stored locally without encryption.
- The recorded firmware version is stored in a local JSON file without protection against direct modification.
- My testing does not cover every possible malformed firmware package or attacker-controlled input.
- My assessment is limited to a simulated firmware update mechanism and does not demonstrate full compliance with ETSI EN 303 645.

These limitations show that additional implementation and security testing would be needed for a production IoT device.


## Functional Sufficiency Assessment — Conclusion

I carried out four security tests to evaluate the firmware update mechanism implemented in my Python simulator.

The simulator successfully accepted a valid signed firmware update, rejected modified firmware, prevented an older version from being installed and rejected an unsigned firmware package.

All four tests produced the expected results, demonstrating that the implemented security mechanisms functioned as intended under the tested conditions.

However, I identified limitations relating to firmware installation, key protection, device-state security and the scope of testing. Therefore, my results provide evidence of basic firmware update security functionality rather than full regulatory conformance.