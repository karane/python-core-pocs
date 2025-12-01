def write_text_file(filename, lines):
    """Write a list of lines to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"[WRITE] Wrote {len(lines)} lines to {filename}")


def read_text_file(filename):
    """Read all content from a text file."""
    print(f"[READ] Reading {filename} (all at once):")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print(content.strip())
    return content


def read_line_by_line(filename):
    """Read a text file line by line."""
    print(f"[READ] Reading {filename} (line by line):")
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            print(f"Line {i}: {line.strip()}")


def append_to_file(filename, text):
    """Append a line to the end of a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"[APPEND] Added line to {filename}: {text}")


def main():
    filename = "example.txt"
    lines = [
        "Python is fun!",
        "File I/O is easy.",
        "Closures and decorators are powerful!"
    ]

    # 1. Write file
    write_text_file(filename, lines)

    # 2. Read entire file
    read_text_file(filename)

    # 3. Read line-by-line
    read_line_by_line(filename)

    # 4. Append new line
    append_to_file(filename, "This line was appended later.")

    # 5. Read again to confirm
    read_text_file(filename)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR] {e}")
