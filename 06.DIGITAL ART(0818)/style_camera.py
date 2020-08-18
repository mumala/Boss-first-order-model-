import cv2
from keras.models import load_model
from utils import ReflectionPadding2D
import argparse

class StyleVideoCamera(object):
    style_name = None
    img_shape = None
    generator = None
    def __init__(self):
        StyleVideoCamera.style_name = 'picasso'
        StyleVideoCamera.img_shape = (188, 336)

        StyleVideoCamera.generator = load_model('weights/' + StyleVideoCamera.style_name + '.h5', 
                        custom_objects={'ReflectionPadding2D': ReflectionPadding2D})
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        
        frame = cv2.resize(frame, StyleVideoCamera.img_shape)[None]
        pred = StyleVideoCamera.generator.predict_on_batch(frame).astype('uint8')[0]
        pred = cv2.resize(pred, (640, 480))
           # cv2.imshow('style transfer', pred)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        _,jpeg = cv2.imencode('.jpg',pred)
        return jpeg.tobytes()
