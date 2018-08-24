import urllib.request as req
import urllib

response= req.urlopen('http://ya.ru')
#response.code
html= response.read()
htmlStr= html.decode('utf-8')
query_args= {'text': 'wiki'}
url_args= urllib.parse.urlencode(query_args)
r= req.urlopen('http://ya.ru'+'?'+url_args)#GET запрос
htmlStr= r.read().decode('utf-8')
print(html[:500])
b_url_args= url_args.encode('utf-8')
r= req.urlopen('http://ya.ru', b_url_args)#POST запрос
#urllib.error.HTTPError: HTTP Error 403: Forbidden - отказ в обработке запроса 

