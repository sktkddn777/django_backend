from stock.views import detail, index, new, create
from django.urls import path

from . import views

# url name이 겹치는 경우를 대비.
app_name = 'stock'

urlpatterns = [
  # /stock/
  path('', views.index, name='stock_index'),
  # /stock/show/한화생명
  path('show/<str:stock_name>/', views.detail, name='detail'),
  # /stock/new
  path('new/', views.new, name='new'),
  # /stock/create
  path('create/', views.create, name='create'),
]