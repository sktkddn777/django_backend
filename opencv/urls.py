from opencv.views import index, face_detection
from django.urls import path

from . import views

# url name이 겹치는 경우를 대비.
app_name = 'opencv'

urlpatterns = [
  # /stock/
  path('', views.index, name='index'),

  path('face/', views.face_detection, name='face'),

]