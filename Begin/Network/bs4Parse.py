import requests
#import csv
from bs4 import BeautifulSoup

source = requests.get('https://www.nytimes.com/').text
# print(source)#<class 'requests.models.Response'>
# print(type(source))#<class 'str'>
soup = BeautifulSoup(source, 'lxml')
# print(type(soup))#<class 'bs4.BeautifulSoup'>
# (h2 section-heading, h2 story-heading, h2 headline)
with open('NYTimes_headers.txt', 'w', encoding='utf') as ny:
    for h2 in soup.find_all('h2', class_='story-heading'):
        try:
            headline = h2.text
            # print(type(headline))#<class 'str'>
            ny.write(f'Another headline: {headline}\n')
        except AttributeError:
            ny.write("'NoneType' object has no attribute 'text'\n")  # как отследить строку, вызывающую ошибку?
        except TypeError:
            ny.write('NoneType object is not callable\n')

        print('Another headline: ', headline)
'''
csv_file= open('cms_scrape.csv', 'w')
csv_writer= csv.writer(csv_file)
csv_writer.writerow(['headline'])
'''
'''with open('NYTimes_headers.txt', 'w') as ny:
    for h2 in soup.find_all('h2', class_='story-heading'):
        headline = h2.a.text  # AttributeError: 'NoneType' object has no attribute 'text'
        print(f'Another headline h2 story-heading: {headline}')
        try:
            ny.write(headline + "\n")
        except AttributeError:
            ny.write('Пустой заголовок?')  # как отследить строку, вызывающую ошибку?
        except TypeError:
            ny.write('NoneType object is not callable')'''

# отловить AttributeError: 'NoneType' object has no attribute 'text' - на какой позиции (строке) текста возникает...
'''with open('NYTimes.html', encoding='utf-8') as ny:
    soup = BeautifulSoup(ny, 'lxml')

data = soup.find_all('h2', class_="story-heading")
print(soup.prettify())
print(type(soup))
print(type(data))  # <class 'bs4.element.ResultSet'>

'''
# print(data.h2.a.text)


# urlopen('https://www.nytimes.com/')
