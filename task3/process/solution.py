""""solution"""

from multiprocessing import Process
import os
import time
import librosa
import numpy

DATA_PATH = "/Users/keeprude/Desktop/tasktest/aac"
ANSWER_PATH = "/Users/keeprude/Desktop/answertest3"

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

def mfcc_iter(data_path, answer_path, start, stop):
    """mfcc for a portion of dirs"""

    list_of_obj = os.listdir(data_path)
    for i in range(start, stop):
        tmp_data = data_path + '/' + list_of_obj[i]
        tmp_save = answer_path + '/' + list_of_obj[i]
        if not os.path.exists(tmp_save):
            os.mkdir(tmp_save)
        mfcc(tmp_data, tmp_save)

if __name__ == "__main__":

    LIST_OF_FILES = os.listdir(DATA_PATH)
    LENGTH = len(LIST_OF_FILES) 

    PROCESS1 = Process(target=mfcc_iter, args=(DATA_PATH, ANSWER_PATH, 0, LENGTH//4,))
    PROCESS2 = Process(target=mfcc_iter, args=(DATA_PATH, ANSWER_PATH, LENGTH//4, LENGTH//2,))
    PROCESS3 = Process(target=mfcc_iter, args=(DATA_PATH, ANSWER_PATH, LENGTH//2, 3*LENGTH//4,))
    PROCESS4 = Process(target=mfcc_iter, args=(DATA_PATH, ANSWER_PATH, 3*LENGTH//4, LENGTH,))

    START_TIME = time.time()
    PROCESS1.start()
    PROCESS2.start()
    PROCESS3.start()
    PROCESS4.start()

    PROCESS1.join()
    PROCESS2.join()
    PROCESS3.join()
    PROCESS4.join()
    FINISH_TIME = time.time()

    print(FINISH_TIME - START_TIME)
