def oper(x):
	if x == (3 or 7):# Срабатывает только первое выражение во вложенных скобках, второе не проверяется...
		print('Yes!')
	else:
		print('Alles!')
oper(7)
''' 
Operators are short circuiting. Consider the statement a and b: if a is not True, the value of b does not matter for the result. Thus, Python will not bother evaluating b at all.
This is useful if b is undefined without a. For example, consider an optional dictionary argument. You can test whether it is set, and test one of its key within one expression - the later would be an invalid operation otherwise.    
 an empty list is considered “false”, while a list with elements is considered “true”. If they are used in an expression, boolean operators return the actual objects, not just True or False.
    This is useful if you need to keep on working with the result. For example, one can test whether something is empty and use it in an assignment.
    points = list_param or [1, 2, 3]
Both of these are also the reason why there is no xor operator: it cannot short-circuit. The xor translates to (a and not b) or (b and not a). If you play that out, you realise that both a and b must be evaluated. This makes it impossible to short-circuit. It is also impossible to always use either a or b as the result - for example, if both a and b are True, xor must return a generic False.'''
