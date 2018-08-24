ages = {
'bob' : 33,
'John' : 24,
#'Dick' : 56
}

age = ages.get('Dick', 'Unknown')
print('Dick is %s years old' % age)
