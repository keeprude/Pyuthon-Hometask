import os
import time
import librosa
import numpy
from multiprocessing import Process

data_path = "/Users/keeprude/Desktop/tasktest/aac"
answer_path = "/Users/keeprude/Desktop/answertest3"

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

def mfcc_iter(data_path, answer_path, start, stop):
    list_of_obj = os.listdir(data_path)
    for i in range(start, stop):
        tmp_data = data_path + '/' + list_of_obj[i]
        tmp_save = answer_path + '/' + list_of_obj[i]
        if not os.path.exists(tmp_save) :
            os.mkdir(tmp_save)
        mfcc(tmp_data, tmp_save)

if __name__ == "__main__":

    list_of_files = os.listdir(data_path)
    length = len(list_of_files)
    part_1 = length % 4
    part_2 = length % 2
    part_3 = 3 * length % 4 

    process1 = Process(target = mfcc_iter, args = (data_path, answer_path, 0, length//4 + part_1, ))
    process2 = Process(target = mfcc_iter, args = (data_path, answer_path, length//4, length//2 + part_2, ))
    process3 = Process(target = mfcc_iter, args = (data_path, answer_path, length//2, 3*length//4 + part_3, ))
    process4 = Process(target = mfcc_iter, args = (data_path, answer_path, 3*length//4, length, ))

    start_time = time.time()
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    finish_time = time.time()

    print(finish_time - start_time)
