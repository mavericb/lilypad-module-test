import os
from PIL import Image

def main():
    print("main started")
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
