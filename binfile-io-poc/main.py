import struct
from pathlib import Path

def write_binary_file(filename):
    """Write some bytes and numbers to a binary file."""
    with open(filename, "wb") as f:
        # Write raw bytes
        f.write(b"HELLO")  # 5 bytes
        # Write an integer (4 bytes, little-endian)
        f.write(struct.pack("<I", 123456))
        # Write a float (4 bytes)
        f.write(struct.pack("<f", 3.14))
    print(f"[WRITE] Wrote binary data to {filename}")


def read_binary_file(filename):
    """Read and decode the binary content."""
    with open(filename, "rb") as f:
        raw = f.read()
    print(f"[READ] Raw bytes: {raw}")
    
    # Decode first part as ASCII text
    text = raw[:5].decode("ascii")
    number = struct.unpack("<I", raw[5:9])[0]
    flt = struct.unpack("<f", raw[9:13])[0]
    
    print(f"Decoded text: {text}")
    print(f"Decoded integer: {number}")
    print(f"Decoded float: {flt:.2f}")


def copy_binary_file(src, dst):
    """Copy a binary file efficiently."""
    with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
        while chunk := fsrc.read(4096):  # read in chunks
            fdst.write(chunk)
    print(f"[COPY] Copied {src} → {dst}")


def main():
    Path("output").mkdir(exist_ok=True)
    data_file = Path("output/data.bin")
    copy_file = Path("output/data_copy.bin")

    # 1. Write binary file
    write_binary_file(data_file)

    # 2. Read and interpret
    read_binary_file(data_file)

    # 3. Copy it
    copy_binary_file(data_file, copy_file)


if __name__ == "__main__":
    main()
