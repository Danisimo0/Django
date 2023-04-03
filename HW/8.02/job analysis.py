import requests
from bs4 import BeautifulSoup
import io

URL = 'https://almaty.hh.kz/search/vacancy'
PARAMS = {
    'text': 'Python, Django, DRF',
    'ored_clusters': 'true',
    'enable_snippets': 'true',
    'salary': '',
    'page': 0  # Номер страницы результатов поиска
}
MAX_VACANCIES = 50  # Максимальное количество вакансий для сканирования
requirements = set()
recommendations = set()

with io.open('requirements.txt', 'w', encoding='utf8') as file:
    scanned_vacancies = 0  # Счетчик просмотренных вакансий
    visited_links = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3 '
    }
    while scanned_vacancies < MAX_VACANCIES:
        response = requests.get(URL, PARAMS, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        vacancies = soup.find_all('div', {'class': 'serp-item'})
        # print(vacancies)
        if not vacancies:
            print('Вакансии не найдены')
            break

        for vacancy in vacancies:
            if scanned_vacancies >= MAX_VACANCIES:
                print("Change the number of vacancies")
                break
            vacancy_link = vacancy.find('a', {'data-qa': 'serp-item__title'})['href']
            # print(vacancy_link)
            if vacancy_link in visited_links:
                continue
            visited_links.add(vacancy_link)

            vacancy_response = requests.get(vacancy_link, headers=headers)
            vacancy_soup = BeautifulSoup(vacancy_response.content, 'html.parser')
            vacancy_requirements = vacancy_soup.find('div', {'class': 'vacancy-section'}).find_all('ul')

            for requirement in vacancy_requirements:
                requirements.add(requirement.text.strip())

            for recommendation in vacancy_requirements:
                recommendations.add(recommendation.text.strip())

                with open('requirements_and_recommendations.txt', 'w', encoding='utf-8') as f:
                    f.write('Требования:\n\n')
                    for requirement in sorted(requirements):
                        f.write(requirement + '*\n*')

                    f.write('\n\nРекомендации:\n\n')

                    for recommendation in sorted(recommendations):
                        f.write(recommendation + '*\n*')
