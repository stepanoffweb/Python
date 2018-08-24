 raw_input() is used to input a string, input() is used to input danger. :) input() in Python 2 invokes the eval() function, and that can be dangerous - see Eval really is dangerous by SO member Ned Batchelder. That article covers some advanced Python concepts, but it may help you understand that using eval() on random user input is not wise.
	 1
input evaluates the input, while raw_input does not.
For example, capturing the input 5, returns the int 5. However, capturing the raw_input 5, returns the str '5'
