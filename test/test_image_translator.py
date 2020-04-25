#! python3
import pytest

from src.image_translator import ImageTranslator


def test_get_image_name():
    image_translator = ImageTranslator("images/octocat.png")
    assert "octocat" == image_translator.get_image_name()

def test_get_image_ext():
    image_translator = ImageTranslator("images/octocat.png")
    assert ".png" == image_translator.get_image_ext()

def test_get_image_shape():
    """長さが2で要素がintのtupleが返ってくる"""
    image_translator = ImageTranslator("images/octocat.png")
    assert tuple == type(image_translator.get_image_shape())
    assert int == type(image_translator.get_image_shape()[0])
    assert int == type(image_translator.get_image_shape()[1])
    assert 2 == len(image_translator.get_image_shape())

def test_resize2half():
    image_translator = ImageTranslator("images/octocat.png")
    image_translator.resize2half()
    assert (1000, 1000) == image_translator.get_image_shape()

def test_resize2twice():
    image_translator = ImageTranslator("images/octocat.png")
    image_translator.resize2twice()
    assert (4000, 4000) == image_translator.get_image_shape()
    
def test_resize2target_size():
    image_translator = ImageTranslator("images/octocat.png")
    image_translator.resize2target_size(256, 192)
    assert (256, 192) == image_translator.get_image_shape()