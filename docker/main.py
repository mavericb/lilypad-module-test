import os
from PIL import Image

def main():
    print("main started")

    # Get prompt from $INPUT, falling back to "question mark floating in space" if not set
    input = os.environ.get("INPUT") or "question mark floating in space"
    print(f"Input: {input}")

    image_path = '/app/image.jpg'
    if os.path.exists(image_path):
        with Image.open(image_path) as img:
            print(f"Image size: {img.size}")
            print(f"Image format: {img.format}")
            print(f"Image mode: {img.mode}")
    else:
        print("Image not found")

if __name__ == "__main__":
    main()
