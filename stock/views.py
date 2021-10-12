from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from . models import Kstock
from .forms import StockCreateForm
from .crawl import crawl_stock

# Create your views here.


def index(request):
  try:
    stock_list = Kstock.objects.filter(user=request.user).order_by('name')

    context = {
      'stock_list': stock_list,
    }
    return render(request, 'stock/index.html', context)
  except:
    return redirect('user:home')


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
    name = request.POST['name']
    purchase_data = request.POST['purchase_data']
    buy_price = request.POST['buy_price']
    description = request.POST['description']

    user = request.user

    stock = Kstock(
      name = name,
      purchase_data = purchase_data,
      buy_price = buy_price,
      description = description,

      user = user,
    )
    stock.save()
    return redirect('stock:stock_index')
  else:
    form = StockCreateForm()
    return render(request, 'stock/create.html', {'form': form})