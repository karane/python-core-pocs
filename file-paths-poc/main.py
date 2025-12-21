import os
from pathlib import Path


# Using os module
def os_examples():
    print("=== os module examples ===")

    # Get current working directory
    cwd = os.getcwd()
    print("Current working directory:", cwd)

    # Create a new folder
    folder = "os_demo"
    os.makedirs(folder, exist_ok=True)
    print(f"Created directory: {folder}")

    # Create a file inside it
    file_path = os.path.join(folder, "example.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("This is an example file created using os module.\n")
    print(f"Created file: {file_path}")

    # List directory contents
    print("Directory contents:", os.listdir(folder))

    # Rename file
    new_file_path = os.path.join(folder, "renamed.txt")
    os.rename(file_path, new_file_path)
    print(f"Renamed file to: {new_file_path}")

    # Remove file and folder
    os.remove(new_file_path)
    os.rmdir(folder)
    print(f"Removed file and directory: {folder}")


# Using pathlib module
def pathlib_examples():
    print("\n=== pathlib module examples ===")

    # Get current working directory
    cwd = Path.cwd()
    print("Current working directory:", cwd)

    # Create a new folder
    folder = cwd / "pathlib_demo"
    folder.mkdir(exist_ok=True)
    print(f"Created directory: {folder}")

    # Create a file inside it
    file_path = folder / "example.txt"
    file_path.write_text("This is an example file created using pathlib.\n", encoding="utf-8")
    print(f"Created file: {file_path}")

    # List files in the directory
    print("Directory contents:")
    for f in folder.iterdir():
        print(" -", f.name)

    # Rename the file
    new_file = folder / "renamed.txt"
    file_path.rename(new_file)
    print(f"Renamed file to: {new_file.name}")

    # Check file existence
    if new_file.exists():
        print(f"File exists: {new_file}")

    # Delete the file and folder
    new_file.unlink()
    folder.rmdir()
    print(f"Removed file and directory: {folder}")


def main():
    os_examples()
    pathlib_examples()


if __name__ == "__main__":
    main()
