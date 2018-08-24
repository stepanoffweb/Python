x, y, z = 10, -10, 'Ara'
x, y, z = y, z, x
print(x)

empty_tuple = ()
test1 = ("a")
test2 = ("a",)
test3 = 1, 2, 3
print(test1, test2, test3)
print(tipe(test3))

survey = (21, "Switzerland", True)
age, country, flag = survey
print(age)
print(country)
print(flag)


>>> tuple1=()
>>> print(dir(tuple1))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '_
_eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs
__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__'
, '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_e
x__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclas
shook__', 'count', 'index']
>>>
import sys
print(help(sys.getsizeof))

import timeit
list_test = timeit.timeit(testlist = "[1, 2, 3, 4, 5]", number = 1 000 000)
list_tuple = timeit.timeit(testtuple = "(1, 2, 3, 4, 5)", number = 1 000 000)

