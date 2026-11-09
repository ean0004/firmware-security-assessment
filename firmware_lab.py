
import argparse
import json
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

DATA = Path("lab_data")
PRIVATE_KEY = DATA / "signing_private.pem"
PUBLIC_KEY = DATA / "trusted_public.pem"
STATE = DATA / "device_state.json"


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


def initialise():
    DATA.mkdir(exist_ok=True)

    if any(p.exists() for p in [PRIVATE_KEY, PUBLIC_KEY, STATE]):
        raise ValueError("Lab already initialised")

    key = Ed25519PrivateKey.generate()

    PRIVATE_KEY.write_bytes(key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()
    ))

    PUBLIC_KEY.write_bytes(key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    ))

    STATE.write_text(json.dumps({"version": 1}))
    print("Lab ready. Installed firmware version: 1")


def build(version, payload, filename):
    key = serialization.load_pem_private_key(
        PRIVATE_KEY.read_bytes(), password=None
    )

    message = {"version": version, "payload": payload}
    signature = key.sign(canonical(message)).hex()

    package = {**message, "signature": signature}
    Path(filename).write_text(json.dumps(package, indent=2))
    print(f"Signed package created: {filename}")


def install(filename):
    package = json.loads(Path(filename).read_text())
    public_key = serialization.load_pem_public_key(
        PUBLIC_KEY.read_bytes()
    )

    message = {
        "version": package["version"],
        "payload": package["payload"]
    }

    if type(message["version"]) is not int or message["version"] < 1:
        raise ValueError("Invalid firmware version")

    if not isinstance(message["payload"], str):
        raise ValueError("Invalid firmware payload")

    try:
        public_key.verify(
            bytes.fromhex(package["signature"]),
            canonical(message)
        )
    except (InvalidSignature, ValueError, KeyError, TypeError):
        raise ValueError("Rejected: invalid firmware signature")

    state = json.loads(STATE.read_text())

    if message["version"] <= state["version"]:
        raise ValueError("Rejected: firmware downgrade or replay")

    STATE.write_text(json.dumps({"version": message["version"]}))
    print(f"Accepted: firmware version {message['version']} installed")


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init")
    sub.add_parser("status")

    create = sub.add_parser("build")
    create.add_argument("version", type=int)
    create.add_argument("payload")
    create.add_argument("filename")

    update = sub.add_parser("install")
    update.add_argument("filename")

    args = parser.parse_args()

    try:
        if args.command == "init":
            initialise()
        elif args.command == "status":
            print(STATE.read_text())
        elif args.command == "build":
            build(args.version, args.payload, args.filename)
        elif args.command == "install":
            install(args.filename)
    except (ValueError, KeyError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
