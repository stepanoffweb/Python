def check():
	for numeral in range(1000000):
		if (numeral%4==0):
			print(numeral)
		if (numeral%4==0) and (numeral%2!=0):
			print("Ooops!!! ", numeral)
			return 1
		
if check()!=1: 
	print("No, it's impossible!!!!")
# Ãûדû, קמ, ןמילאכ חאיקטךא?