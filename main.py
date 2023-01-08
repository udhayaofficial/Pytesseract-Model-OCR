import pytesseract
from pytesseract import Output
import cv2
import numpy as np
import pandas as pd
import io
from io import BytesIO
import sys
import os
import tempfile
import csv
import json
from csv import writer

def main(filename):

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\HARIHARAN\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract'
    img = cv2.imread(filename)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)  
    json_format=json.dumps(d)    
    print(json_format)
    with open("D:\\FTP1\\40042897883.json", "w") as outfile:json.dump(d, outfile)


if __name__ == "__main__":
    #id=2
    image_path = '40042897883.tiff'
    main(image_path)