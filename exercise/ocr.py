#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

image = Image.open("/Users/weipengjie/Desktop/abc.png")
code = pytesseract.image_to_string(image)
print(code)