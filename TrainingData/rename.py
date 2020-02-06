import os

def main():
    i = 0
    directory = "DownloadedFile/img3/"
    
    for filename in os.listdir(directory):
        dst = directory + "Pic" + str(i) + ".jpg"
        src = directory + filename

        os.rename(src, dst)
        i+=1

main()
print("done")
