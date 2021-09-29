from roadmap.views import index
from django.urls import path

from . import views

app_name = 'roadmap'

urlpatterns = [
  path('', views.index, name='roadmap_index')
]