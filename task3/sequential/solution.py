import os
import time
import librosa
import numpy

data_path = "/Users/keeprude/Desktop/tasktest"
answer_path = "/Users/keeprude/Desktop/taskanswer"

def mfcc(data_path, answer_path):
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
            arr = librosa.feature.mfcc(y = y, sr = sr)
            numpy.save(temp, arr)


start_time = time.time()
mfcc(data_path, answer_path)
finish_time = time.time()
print(finish_time - start_time)
