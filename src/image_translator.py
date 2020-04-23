#! python3
import os

import cv2
import numpy as np


class ImageTranslator:
    """画像の変換を扱うクラス"""
    def __init__(self, image_path=""):
        self.image_path = image_path
        self.image_name = os.path.splitext(os.path.basename(image_path))[0]
        self.image = cv2.imread(image_path)
        
    def get_image_shape(self) -> tuple:
        """画像の高さと幅をタプルで返す"""
        self.height, self.width = self.image.shape[:2]
        return (self.height, self.width)
    
    def resize_half(self):
        """1/2に画像をリサイズして返す"""
        self.image = cv2.resize(self.image, dsize=None, fx=0.5, fy=0.5)
        return self.image
    
    def resize2twice(self):
        """2倍に画像をリサイズして返す"""
        self.image = cv2.resize(self.image, dsize=None, fx=2, fy=2)
        return self.image
    
    def resize2target_size(self, height, width):
        self.image = cv2.resize(self.image, dsize=(width, height))
        return self.image


if __name__ == "__main__":
    image_translator = ImageTranslator("images/octocat.png")
    print(image_translator.get_image_shape())

    image_translator.resize_half()
    print(image_translator.get_image_shape())

    target_h, target_w = (256, 196)
    image_translator.resize2target_size(target_h, target_w)
    print(image_translator.get_image_shape())
