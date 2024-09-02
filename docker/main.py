import os
import sys
from PIL import Image


def write_to_stdout(content):
    sys.stdout.write(content + '\n')
    sys.stdout.flush()


def log_directory_contents(path):
    write_to_stdout(f"Contents of {path}:")
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        write_to_stdout(f"{indent}[DIR] {os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            write_to_stdout(f"{sub_indent}[FILE] {file}")


def main():
    write_to_stdout("Image processing script started")

    log_directory_contents("/")
    log_directory_contents("/app")

    image_path = '/app/image.jpg'

    if os.path.exists(image_path):
        try:
            with Image.open(image_path) as img:
                write_to_stdout(f"Image successfully opened: {image_path}")
                write_to_stdout(f"Image size: {img.size}")
                write_to_stdout(f"Image format: {img.format}")
                write_to_stdout(f"Image mode: {img.mode}")
        except Exception as e:
            write_to_stdout(f"Error processing image: {str(e)}")
    else:
        write_to_stdout(f"Image not found at path: {image_path}")

    write_to_stdout("Image processing script completed")


if __name__ == "__main__":
    main()