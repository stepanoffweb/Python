def g(x):
	return x[::-1]

s= ['Hello', 'World']
s= list(map(g, s))
print(s)

