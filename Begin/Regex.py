import re

def cneckio(data):
	#(?=) is positive lookahead for make sure the enclosed pattern exists.
	return bool (re.search(r'^(?=.*\d)(?=.*[a-z](?=.*[A-Z]).{10,}$',data))# 1Var.
	#2 Var.
	#return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data)>=10 else False
	
	