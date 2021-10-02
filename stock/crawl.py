import requests
from bs4 import BeautifulSoup

def crawl_stock(stock_name):
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
    }
  else:
    context = {'none': None}
    price = 0

  return [context, price]