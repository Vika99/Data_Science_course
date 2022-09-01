

import numpy as np
import cv2, time, os
import tensorflow as tf
from tensorflow.keras import models



# Инициалицация переменных и подключение к камере
video = cv2.VideoCapture(0)
ww = video.get(cv2.CAP_PROP_FRAME_WIDTH)
hh = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

print (ww, hh)


# Определяем метрику и функцию потерь

def IoU(y_true, y_pred):
    y_true_f = tf.keras.backend.flatten(y_true)
    y_pred_f = tf.keras.backend.flatten(y_pred)
    intersection = tf.keras.backend.sum(y_true_f * y_pred_f)
    return (2. * intersection + 1.0) / (tf.keras.backend.sum(y_true_f) + tf.keras.backend.sum(y_pred_f) + 1.0)


mod = models.load_model('Face_net.h5', custom_objects={'IoU': IoU})

FLAG = False
i = 100
# главный цикл анализа видеопотока
while (True):

    ret, frame = video.read()
        
    if ret:
	
        #frame2 = cv2.resize(frame,(853, 480))

#        cv2.imshow('frame',frame)

        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame2 = frame2 / 255

        frame2 = np.expand_dims(frame2,axis=0)

        pred = mod.predict(frame2)

        tr = (pred.reshape((480,640))>0.5).astype('uint8')
        
        cont, heir = cv2.findContours(tr.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   

        for c in cont:
            x,y, w,h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y),(x+w,y+h), color = (255,0,0))

        cv2.imshow('frame',frame)
        



    inn = cv2.waitKey(1) & 0xFF	
    if inn == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

