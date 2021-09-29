from stock.views import detail, index
from django.urls import path

from . import views

# url name이 겹치는 경우를 대비.
app_name = 'stock'

urlpatterns = [
  # /stock/
  path('', views.index, name='stock_index'),
  # /stock/한화생명
  path('<str:stock_name>/', views.detail, name='detail'),
]