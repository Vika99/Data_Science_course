

import numpy as np
import cv2, time, os
import tensorflow as tf
from tensorflow.keras import models


# Инициалицация переменных и подключение к камере
video = cv2.VideoCapture(0)
ww = video.get(cv2.CAP_PROP_FRAME_WIDTH)
hh = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

print (ww, hh)

#определяем метрику и функцию
def IoU(y_true, y_pred):
    y_true_f = tf.keras.backend.flatten(y_true)
    y_pred_f = tf.keras.backend.flatten(y_pred)
    intersection = tf.keras.backend.sum(y_true_f * y_pred_f)
    return (2. *intersection +1.0 )/(tf.keras.backend.sum(y_true_f) + tf.keras.backend.sum(y_pred_f) +1.0
 
#mod = models.load_model('Face_net.h5',custom_objects = {'IoU': IoU})    
    
FLAG = False
i = 100


files = os.listdir('pics/')
#files = sorted(files)

data =[]

for fi in files:
    im = cv2.imread('pics/'+fi)
    data.append(im)
    
data = np.array(im)
# главный цикл анализа видеопотока
while (True):

    ret, frame = video.read()
        
    if ret:
	
        #frame2 = cv2.resize(frame,(853, 480))

        cv2.imshow('frame',frame)


    inn = cv2.waitKey(1) & 0xFF	
    if inn == ord(' '):
        FLAG = not FLAG
                                                                                                                                                                                          
    if FLAG:
        fname ='pictures/pic_' + str(i)+'.jpg'
        i = i+1
        cv2.imwrite(fname,frame)
    
    inn = cv2.waitKey(1) & 0xFF	
    
    if inn == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

