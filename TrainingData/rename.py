import os


def main():
    i = 0
    directory = "RawImage"
    
    for file in os.listdir(directory):
        src = file
        dst = "Pic" + str(i) + ".jpg"
        src = os.path.join(directory, src)
        dst = os.path.join(directory, dst)

        os.rename(src, dst)

        i+=1

main()
print("done")
