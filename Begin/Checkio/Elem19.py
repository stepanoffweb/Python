''' You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
Input: a list of strings.
Output: a string. '''
def most_frequent(list_strings):
		return max(list_strings, key=lambda s: list_strings.count(s))

---------------------------------------------------------
#return max(data, key=data.count)
--------------------------------------------------------
#from statistics import mode as most_frequent
-----------------------------------------------------









if __name__ == '__main__':
	print('Example:')
	print(most_frequent(['a', 'b', 'c', 'a', 'b','a']))
	assert most_frequent(['a', 'b', 'c', 'a', 'b','a']) == 'a'
	assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
	print('Done')
