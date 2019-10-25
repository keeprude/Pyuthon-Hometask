"""solution"""

import os
import time
import librosa
import numpy

DATA_PATH = "/Users/keeprude/Desktop/tasktest"
ANSWER_PATH = "/Users/keeprude/Desktop/taskanswer"

def mfcc(data_path, answer_path):
    """extracting mfcc"""

    list_of_obj = os.listdir(data_path)
    for obj in list_of_obj:
        path = data_path + '/' + obj
        if os.path.isdir(path):
            save_path = answer_path + '/' + obj
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            mfcc(path, save_path)
        elif os.path.isfile(path) and obj != ".DS_Store":
            temp = answer_path + '/' + obj[:len(obj) - 4]
            print(temp)
            y, sr = librosa.load(path)
            arr = librosa.feature.mfcc(y=y, sr=sr)
            numpy.save(temp, arr)

if __name__ == "__main__":
    START_TIME = time.time()
    mfcc(DATA_PATH, ANSWER_PATH)
    FINISH_TIME = time.time()
    print(FINISH_TIME - START_TIME)
