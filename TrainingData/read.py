import numpy as np
import json
from PIL import Image, ImageDraw
import os
import ast


def getPic():
    drt = os.path.join("RawImage", "Pic6.jpg")
    img = Image.open(drt)
    width, height = img.size

    return img
    
    
def getAnn():
    drt = os.path.join("RawAnn", "Ann6.jpg.json")
    
    with open(drt) as json_file:
        data = json.load(json_file)
        
        print(str(len(data['objects'])), 'fuel cells found.')

        
        for p in data['objects']:
            points = p['points']
            exterior = points['exterior']
            array = np.asarray(exterior)
            
    return array

def main():
    pic = getPic()
    ann = getAnn()

    draw = ImageDraw.Draw(pic)
    draw.line((ann[0][0], ann[0][1]) + (ann[1][0], ann[1][1]), fill=(255, 0, 0))
    del draw

    pic.show()
    
getAnn()
#main()





'''
for pixel in iter(img.getdata()):
    print(pixel)
'''
