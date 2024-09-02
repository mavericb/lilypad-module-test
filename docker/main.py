# import os
# from PIL import Image
#
# def main():
#     print("main started")
#     image_path = '/app/image.jpg'
#     if os.path.exists(image_path):
#         with Image.open(image_path) as img:
#             print(f"Image size: {img.size}")
#             print(f"Image format: {img.format}")
#             print(f"Image mode: {img.mode}")
#     else:
#         print("Image not found")
#
# if __name__ == "__main__":
#     main()

import os
from PIL import Image


def main():
    print("Main started")
    image_path = '/app/image.jpg'
    output_path = '/outputs/image_info.txt'

    if os.path.exists(image_path):
        with Image.open(image_path) as img:
            info = f"Image size: {img.size}\n"
            info += f"Image format: {img.format}\n"
            info += f"Image mode: {img.mode}\n"

        os.makedirs('/outputs', exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(info)
        print(f"Image information written to {output_path}")
    else:
        print("Image not found")


if __name__ == "__main__":
    main()