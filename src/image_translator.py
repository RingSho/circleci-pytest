#! python3
import os

import cv2


class ImageTranslator:
    """画像の変換を扱うクラス"""
    def __init__(self, image_path=""):
        self.image_path = image_path
        self.image_name = os.path.splitext(os.path.basename(image_path))[0]
        self.image = cv2.imread(image_path)

    def get_image_shape(self) -> tuple:
        """画像の高さと幅をタプル(height, width)で返す"""
        self.height, self.width = self.image.shape[:2]
        return (self.height, self.width)
    
    def get_image_name(self) -> str:
        """ファイル名を返す"""
        return str(self.image_name)
    
    def get_image_ext(self) -> str:
        """拡張子を返す"""
        root, ext = os.path.splitext(self.image_path)
        return str(ext)

    def resize2half(self):
        """1/2に画像をリサイズして返す"""
        self.image = cv2.resize(self.image, dsize=None, fx=0.5, fy=0.5)
        return self.image
    
    def resize2twice(self):
        """2倍に画像をリサイズして返す"""
        self.image = cv2.resize(self.image, dsize=None, fx=2, fy=2)
        return self.image
    
    def resize2target_size(self, height, width):
        """指定したサイズにリサイズした画像を返す"""
        self.image = cv2.resize(self.image, dsize=(width, height))
        return self.image


if __name__ == "__main__":
    image_translator = ImageTranslator("images/octocat.png")
    print("image name: ", image_translator.get_image_name())
    print("image size: ", image_translator.get_image_shape())
    print("image ext: ", image_translator.get_image_ext())

    image_translator.resize2half()
    print("image size: ", image_translator.get_image_shape())

    target_h, target_w = (256, 196)
    image_translator.resize2target_size(target_h, target_w)
    print("image size: ", image_translator.get_image_shape())
