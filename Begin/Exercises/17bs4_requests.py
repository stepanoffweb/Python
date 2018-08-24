'''Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
Concepts for this week:
    Libraries
    requests
    BeautifulSoup
http://www.nytimes.com/'''
from bs4 import BeautifulSoup
import requests

source= requests.get('http://www.nytimes.com/').text
soup= BeautifulSoup(source, 'lxml')
story_headers[]
for header in 	soup.find_all('h3', class_= "story-heading")
	headline= header.a.text
	story_headers= append(header)
#refer_headers= soup.find_all('h2', class_= "refer-heading")


'''with open('NYTimes.html', encoding= 'utf-8') as htmlfile:
	soup= BeautifulSoup(htmlfile, 'html5lib')#UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 52853: character maps to <undefined> 'lxml' - тот же результат

#print(soup.prettify())
with open("NYheaders.txt", 'w') as NYh:
	headers= soup.find_all('h3', class_= "story-heading")
for header in headers:
	#header= 'Story-headers'+ header#TypeError: must be str, not Tag

	NYh.write( header)'''

print(soup.find_all('h3', class_= "story-heading"))
print(soup.find_all('h2', class_= "refer-heading"))
