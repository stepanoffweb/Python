'''предоставляется набор координат, в которых расставлены БЕЛЫЕ пешки. Вы должны подсчитать количество защищенных пешек.
Входные данные: Координаты расставленных пешек в виде набора строк(set) .
Выходные данные: Количество защищенных пешек в виде целого числа. 
0 < pawns ≤ 8 
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
'''
# class pown(self, coord, color):# coord= 'b4'
	# self.coord= coord
	# self.color= color

	# def defend(coord, color):
		# color= self.color
		# coord= self.coord
		# def_fields= {str(chr(ord(coord[0])+1)+ coord[1]+1), str(chr(ord(coord[0])-1)+ coord[1]+1}
		# return def_fields


def defend(coord):
	letter_left= str(chr(ord(coord[0])-1))
	letter_right= str(chr(ord(coord[0])+1))
	field_number= int(coord[1])+1
	def_field_left= letter_left + str(field_number)
	def_field_right= letter_right+ str(field_number)
	def_fields= {def_field_left, def_field_right}
	return def_fields

#pawns= {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
def safe_pawns(pawns):
	def_fields = set()
	for pawn in pawns:
		def_fields.update(defend(pawn))
	return len(pawns.intersection(def_fields))

if __name__== '__main__':
	#main(pawns)
	assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
	assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#    return sum(1 if chr(ord(pawn[0]) + 1) + chr(ord(pawn[1]) - 1) in pawns or chr(ord(pawn[0]) - 1) + chr(ord(pawn[1]) - 1) in pawns else 0 for pawn in pawns)

	# paw_indexes = set()
    # for p in pawns:
        # row=int(p[1])-1
        # col=ord(p[0])-97
        # paw_indexes.add((row, col))
    # n=0
    # for a in paw_indexes:
        # if ((a[0]-1, a[1]-1)) in paw_indexes or ((a[0]-1, a[1]+1)) in paw_indexes:
            # n=n+1
    # return n

