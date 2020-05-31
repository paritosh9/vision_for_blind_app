import os
from multiprocessing import Pool


#processes = ('yolov3_model_loader.py', 'video_capture.py', 'yolov3_object_detection.py', 'text_to_audio.py')
processes = ('opencv_yolo.py', 'text_to_audio.py')

def run_process(process):
    os.system('python {}'.format(process))

if __name__ == "__main__":
    pool = Pool(processes=2)
    pool.map(run_process, processes)
