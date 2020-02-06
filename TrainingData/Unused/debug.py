#C:\code\RecognitionWithML\TrainingData\DownloadedFile\ann1\DSC02119.jpg
#C:\code\RecognitionWithML\TrainingData

import shutil

source = "C:/code/RecognitionWithML/TrainingData/DownloadedFile/ann1/DSC02119.jpg.json"

destination = "copied.jpg.json"

shutil.copyfile(source, destination)

