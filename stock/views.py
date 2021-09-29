from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from . models import Kstock

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

  stock = Kstock.objects.filter(name=stock_name)[0]
  print(stock.description)
  url = f"https://search.naver.com/search.naver?query={stock_name}"
  response = requests.get(url)
  if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    price = soup.select_one('#_cs_root > div.ar_spot > div > h3 > a > span.spt_con.up > strong')
    if price == None:
      price = soup.select_one('#_cs_root > div.ar_spot > div > h3 > a > span.spt_con.dw > strong').text
    else:
      price = price.text

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