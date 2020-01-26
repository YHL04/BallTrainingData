import numpy as np
import json
from PIL import Image
import os

def main():
    drt = os.path.join("RawImage", "Pic30.jpg")
    img = Image.open(drt)
    width, height = img.size

    '''
    area = (0, 0, width/2, height/2)
    img = img.crop(area)
    '''
    img.show()

    
def getAnn():
    drt = os.path.join("RawAnn", "Ann30.jpg.json")
    with open(drt) as json_file:
        data = json.load(json_file)
        for p in data:
            print(p)

main()
getAnn()



'''
for pixel in iter(img.getdata()):
    print(pixel)
'''
