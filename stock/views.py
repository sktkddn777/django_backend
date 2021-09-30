from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from . models import Kstock
from .forms import StockCreateForm
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
  url = f"https://search.naver.com/search.naver?query={stock_name}"
  response = requests.get(url)
  if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    up_down = ['up','eq','dw']

    for i in up_down:
      price = soup.select_one(f'#_cs_root > div.ar_spot > div > h3 > a > span.spt_con.{i} > strong')
      if price:
        price = price.text
        break

    high = soup.select_one("#_cs_root > div.ar_cont > div.cont_dtcon > div > ul.lst > li.hp > dl > dd").text
    low = soup.select_one("#_cs_root > div.ar_cont > div.cont_dtcon > div > ul.lst > li.lp > dl > dd").text
    trading_volume = soup.select_one('#_cs_root > div.ar_cont > div.cont_dtcon > div > ul.lst > li.vl > dl > dd').text
    foreigner = soup.select_one('#_cs_root > div.ar_cont > div.cont_dtcon > div > ul.lst > li.frr > dl > dd').text
    chart = soup.select_one('#_cs_root > div.ar_cont > div.cont_grp > div.grp_img > div.img.graph_area.open > a > img')

    context = {
      'name': stock_name,
      'high': high,
      'low': low,
      'trading': trading_volume,
      'foreigner': foreigner,
      'chart': chart['src'],
      'revenue': int(price.replace(',','')) - stock.buy_price,
    }
  else:
    context = {'none': None}
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