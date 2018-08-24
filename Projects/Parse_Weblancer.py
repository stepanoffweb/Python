import urllib.request
from bs4 import BeautifulSoup

def main():
	print(get_html(url))
	
def get_html(url):
	resp= urllib.request.urlopen(url)
	return resp.read()
	
def parse(html):
	soup= BeautifulSoup(html)
	
url= 'https://www.weblancer.net/jobs/'
	
	
	

if __name__ == '__main__':
	main()