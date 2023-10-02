# type stub for redwood module
# see https://pyo3.rs/v0.16.4/python_typing_hints.html
from pathlib import Path
from typing import BinaryIO

def generate_source_key_pair(passphrase: str, email: str) -> tuple[str, str, str]: ...
def encrypt_message(recipients: list[str], plaintext: str, destination: Path) -> None: ...
def encrypt_stream(recipients: list[str], plaintext: BinaryIO, destination: Path) -> None: ...
def decrypt(ciphertext: bytes, secret_key: str, passphrase: str) -> bytes: ...

class RedwoodError(Exception): ...
