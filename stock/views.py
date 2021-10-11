from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from . models import Kstock
from .forms import StockCreateForm
from .crawl import crawl_stock

# Create your views here.


def index(request):
  stock_list = Kstock.objects.order_by('name')
  context = {
    'stock_list': stock_list,
  }
  return render(request, 'stock/index.html', context)


def detail(request, stock_name):
  import requests
  from bs4 import BeautifulSoup

  stock = Kstock.objects.filter(name=stock_name).first()

  stock_name = stock_name.replace('&','')
  crawl_data = crawl_stock(stock_name)
  context, price = crawl_data[0], crawl_data[1]
  if 'none' in context:
    context = context
  else:
    context['revenue'] = int(price.replace(',','')) - stock.buy_price

  return render(request, 'stock/detail.html', context)

def new(request):
  return render(request, 'stock/create.html')

def create(request):
  '''
  POST방식으로 요청이 들어옴.
  입력된 내용을 form에 저장.
  form이 정의한 필드에 적합하면 저장.
  '''
  if request.method=='POST':
    form = StockCreateForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
      return redirect('stock:stock_index')
    else:
      return redirect('stock:stock_index')
  else:
    form = StockCreateForm()
    return render(request, 'stock/create.html', {'form': form})