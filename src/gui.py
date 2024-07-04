from pathlib import Path
import tkinter as tk
import ttkbootstrap as tb
from PIL import Image
import os


def asset_path(*paths):
    ASSETS_PATH = Path(__file__).resolve().parent / "Assets"
    return ASSETS_PATH / Path(*paths)


def open_image(image_path):
    if os.path.exists(image_path):
        # Open the image
        img = Image.open(image_path)
        # Optionally, do something with the image, like showing it
        img.show()
    else:
        print(f"Image file '{image_path}' does not exist.")



open_image(asset_path("Homeframe", "home.png"))
