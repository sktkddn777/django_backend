from django.http.response import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip

import cv2
import threading

# Create your views here.
def index(request):
  return HttpResponse("HELLO OPENCV")

@gzip.gzip_page
def face_detection(request):
  try:
    cam = VideoCamera()
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
  except:
    pass

# 비디오 클래스를 캡쳐하기 위해.

class VideoCamera(object):
  def __init__(self):
    self.video = cv2.VideoCapture(0)
    (self.grabbed, self.frame) = self.video.read()
    threading.Thread(target=self.update, args=()).start()


  def __del__(self):
    self.video.release()

  def get_frame(self):
    image = self.frame
    _, jpeg = cv2.imencode('.jpg', image)
    return jpeg.tobytes()

  def update(self):
    self.xml = 'opencv/harrcascades/haarcascade_frontalface_alt.xml'
    self.face_cascade = cv2.CascadeClassifier(self.xml)
    self.font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
      (self.grabbed, self.frame) = self.video.read()
      self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
      self.faces = self.face_cascade.detectMultiScale(self.gray, 1.3, 5)

      if len(self.faces):
        print(self.faces)
        for (x,y,w,h) in self.faces:
          cv2.rectangle(self.frame,(x,y),(x+w,y+h),(255,0,0),2)
          cv2.putText(self.frame, 'Face', (x-5, y-5), self.font, 0.5,  (255,255,0), 2)
def gen(camera):
  
  while True:
    frame = camera.get_frame()

    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')