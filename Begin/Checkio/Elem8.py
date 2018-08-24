'''Дана таблица всех доступных продуктов на складе. Данные представлены в виде  list of dicts
Ваша миссия - найти ТОП самых дорогих товаров. Количество товаров, входящих в топ, будет переданно в первом аргументе, а все данные по товарам будут переданы вторым аргументом.
Input: Число и массив диктов (int and list of dicts). Каждый дикт имеет 2 ключа "name" и "price".
Output: Такой же как и второй аргумент. '''
def bigger_price(quality, quantity):
	result= sorted(quantity, key= lambda k: k['price'], reverse= True)
	return result[:quality]

# from operator import itemgetter
# newlist = sorted(list_to_be_sorted, key=itemgetter('name')) 

#return sorted(data, key=lambda x: x['price'], reverse=True)[:quality]

#import operator, heapq, functools
#bigger_price = functools.partial(heapq.nlargest, key=operator.itemgetter('price'))



if __name__ == '__main__':


	assert bigger_price(2, [
		{"name": "bread", "price": 100},
		{"name": "wine", "price": 138},
		{"name": "meat", "price": 15},
		{"name": "water", "price": 1}
		]) == [
		{"name": "wine", "price": 138},
		{"name": "bread", "price": 100}
		], "First"
	assert bigger_price(1, [
		{"name": "pen", "price": 5},
		{"name": "whiteboard", "price": 170}
		]) == [{"name": "whiteboard", "price": 170}], "Second"

	print('Done! Looks like it is fine. Go and check it')