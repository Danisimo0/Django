from django.shortcuts import render
from django.views.decorators.cache import cache_page
from selenium import webdriver

@cache_page(60 * 15) # кэширование на 15 минут
def get_currency(request):
    driver = webdriver.Chrome()
    driver.get('https://kurs.kz')
    data = []
    for item in driver.find_elements_by_css_selector('.js-currency__item'):
        currency_name = item.find_element_by_css_selector('.js-currency__title').text
        currency_rate = item.find_element_by_css_selector('.js-currency__value').text
        data.append({
            'name': currency_name,
            'rate': currency_rate,
        })
    driver.quit()

    return render(request, 'currency.html', {'data': data})