from django.shortcuts import render

from selenium import webdriver
from bs4 import BeautifulSoup
import requests


# from .models import CurrencyRate, WeatherForecast
#

def weather(request, mul: str):
    response = requests.get(
        "https://weather.com/weather/monthly/l/5ead5bf0831e9c4adb7cc4a4f0f66264147a55a24823c075c67035cbfb30724b")
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    weather_data = []
    day = int(mul) * soup.find('div', {'class': 'CalendarDateCell--tempHigh--3k9Yr'}).text
    weather_data.append({'day', day})
    night = int(mul) * soup.find('div', {'class': 'CalendarDateCell--tempLow--2WL7c'}).text
    weather_data.append({'night', night})
    date = int(mul) * soup.find('span', {'class': 'CalendarDateCell--date--JO3Db'}).text
    weather_data.append({'date', date})
    return render(request, 'weather.html', {'day': weather_data})


from selenium.webdriver.chrome.options import Options


def currency(request):
    options = Options()
    options.headless = True
    options.add_argument('--headless')  # запускаем браузер в фоновом режиме
    # cache_key = 'currency_rates'
    # cached_data = cache.get(cache_key)
    # if cached_data:
    # использовать закешированные данные
    # context = cached_data
    # else:
  
    driver = webdriver.Chrome(options=options)
    driver.get('https://kurs.kz')
    usd_rate = driver.find_element_by_xpath('//div[@id="USD"]/div[@class="value"]')
    eur_rate = driver.find_element_by_xpath('//div[@id="EUR"]/div[@class="value"]')
    usd_text = usd_rate.text
    eur_text = eur_rate.text
    driver.quit()

    # сохранить данные в кэш
    context = {'usd_rate': usd_text, 'eur_rate': eur_text}
    # cache.set(cache_key, (usd_rate, eur_rate), timeout=60)

    return render(request, 'currency.html', context)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def weather(request): не смог вытащить уникальные значения, взял другой сайт .
#     url = 'https://www.gismeteo.kz/weather-almaty-5205/10-days/'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#         "Referer": "https://www.google.com/",
#         "Accept-Language": "en-US,en;q=0.5",
#     }
#     response = requests.get(url=url, headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     # находим все теги div с классом weather_item и выводим их содержимое
#     weather_items = soup.find_all('div', {'class': 'now'})
#
#     weather_data = []
#     for item in weather_items:
#         day = item.find('div', {'class': 'now-localdate'}).text
#         temperature = item.find('span', {'class': 'sign'}).text
#         temperature_night = item.find('div', {'class': 'now-info-item humidity'}).text
#         weather_data.append({'day': day, 'temperature': temperature, 'temperature_night': temperature_night})
#         return HttpResponse(str(weather_data))


# def currency(request):
#
#     cache_key = 'currency_rates'
#     cached_rates = cache.get(cache_key)
#     if cached_rates:
#         usd_rate, eur_rate = cached_rates
#     else:
#
#         driver = webdriver.Chrome
#         driver.get('https://kurs.kz')
#
#         usd_rate_element = driver.find_element_by_xpath('//div[@id="USD"]/div[@class="value"]')
#         eur_rate_element = driver.find_element_by_xpath('//div[@id="EUR"]/div[@class="value"]')
#
#
#         usd_rate = float(usd_rate_element.text)
#         eur_rate = float(eur_rate_element.text)
#

#         driver.quit()

#         cache.set(cache_key, (usd_rate, eur_rate))
#
#         CurrencyRate.objects.create(usd_rate=usd_rate, eur_rate=eur_rate)
#
#     context = {'usd_rate': usd_rate, 'eur_rate': eur_rate}
#     return render(request, 'currency.html', context)
#
# from django.core.cache import cache
#
#
# def currency(request):
#     cache_key = 'currency_rates'
#     cached_data = cache.get(cache_key)
#     if cached_data:

#         context = cached_data
#     else:

#         driver = webdriver.Chrome('/path/to/chromedriver') #
#         driver.get('https://kurs.kz')
#         usd_rate = driver.find_element_by_xpath('//div[@id="USD"]/div[@class="value"]')
#         eur_rate = driver.find_element_by_xpath('//div[@id="EUR"]/div[@class="value"]')
#         usd_text = usd_rate.text
#         eur_text = eur_rate.text
#         driver.quit()
#

#         context = {'usd_rate': usd_text, 'eur_rate': eur_text}
#         cache.set(cache_key, context, timeout=60*60) # хранить данные в кэше на 1 час
#
#     return render(request, 'currency.html', context)
#


# def currency(request):
#     url = 'https://kurs.kz'
#     options = Options()
#     options.add_argument('--headless')  # запускаем браузер в фоновом режиме
#     browser = webdriver.Chrome(options=options)
#     browser.get(url)
#
#     currency_data = []
#     currency_items = browser.find_elements_by_css_selector('.table-hover tbody tr')
#     for item in currency_items:
#         currency_name = item.find_element_by_css_selector('td:nth-child(1)').text
#         currency_rate = item.find_element_by_css_selector('td:nth-child(2)').text
#         currency_data.append({'name': currency_name, 'rate': currency_rate})
#     browser.quit()
#     return HttpResponse(str(currency_data))
