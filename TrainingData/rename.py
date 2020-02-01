import os
from shutil import copyfile


def main():
    for x in range(1, 4):
        ann_dir = "/DownloadedFile/ann" + str(x)
        img_dir = "/DownloadedFile/img" + str(x)
        rawann_dir = "/RawAnn"
        rawimg_dir = "/RawPic"

        i = 0
        
        for picfile in os.listdir(img_dir):
            for annfile in os.listdir(ann_dir):
                if annfile == picfile + ".json":
                    
                    copyfile(ann_dir + "/" + annfile, rawann_dir + "/" + )
                    
                    
                    


main()
print("done")
