'''You need to figure if a wellfounded and wellsized iterable is completely empty.
An iterable x0 is wellfounded if there is no infinite sequence
x1,x2,x3...such that... in x3 in x2 in x1 in x0
(where in is meant iteratively, x(n+1) will be encountered while iterating through xn ).
A wellfounded iterable is wellsized if it has only finitely many iterable elements, and all of them are wellsized.
A wellfounded iterable is completely empty when all its elements are completely empty.
Some consequences of the above definitions:
    any empty iterable is completely empty
    a non-iterable is never completely empty
    the only wellfounded string is    ''  , and it is completely empty
    bytes, and (possibly nested) tuples/frozensets of them are always wellfounded and wellsized
    {'': 'Nonempty'}   is a wellfounded and completely empty iterable
    after    c=[];c.append(c), c is a non-wellfounded iterable
    itertools.repeat(())  is wellfounded but not wellsized
    itertools.repeat(5)   is wellfounded and wellsized
Input: A wellfounded and wellsized iterable.
Output: A bool. '''
import collections
def completely_empty(array):
    if type(array) == str:
        return True if array == '' else False
    if type(array) == list:
        return True if len(array) == 0 else   all([completely_empty(i) for i in array])
    if type(array) == dict:
        return True if len(array) == 0 or  (len(array.keys()) == 1 and '' in array) else False
    if type(array) == tuple:
        return completely_empty(list(array))
    try:
        array.__getitem__(0)
    except IndexError:
        return True
    except AttributeError:
        pass
    return all([completely_empty(i) for i in array])  if isinstance(array, collections.Iterable)
        else False











if __name__ == '__main__':
    assert( completely_empty([])) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    print('Done')