from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

ARTIFACT = Path("internal/artifacts/flag.enc")


def decrypt_artifact(key_hex):
    key = bytes.fromhex(key_hex.strip())

    if len(key) != 16:
        raise ValueError("Key harus berupa 32 karakter hexadecimal.")

    data = ARTIFACT.read_bytes()

    if len(data) < 32:
        raise ValueError("flag.enc tidak valid.")

    iv = data[:16]
    ciphertext = data[16:]

    if len(ciphertext) % AES.block_size != 0:
        raise ValueError("Ciphertext memiliki ukuran tidak valid.")

    plaintext = unpad(
        AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext),
        AES.block_size,
    )

    print("\nDecrypted artifact:")
    print(plaintext.decode())


def main():
    print("Desktop Sync Artifact Recovery")
    print("=" * 32)

    key = input("Enter recovery key: ")

    try:
        decrypt_artifact(key)
    except Exception as exc:
        print(f"Recovery failed: {exc}")


if __name__ == "__main__":
    main()
