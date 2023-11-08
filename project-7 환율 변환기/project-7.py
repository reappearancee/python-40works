
### 7-1번
# from currency_converter import CurrencyConverter

# cc = CurrencyConverter()
# print(cc.currencies)

### 7-2번
# from currency_converter import CurrencyConverter

# cc = CurrencyConverter('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
# result = cc.convert(1,'USD', 'KRW')
# print(result)

### 7-3번 (x)
import requests
from bs4 import BeautifulSoup

def 환율(target1, target2):
    headers = {
        'User-Agent' : 'Mozila/5.0',
        'Content-Type' : 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers) 
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)

환율('usd', 'krw')
