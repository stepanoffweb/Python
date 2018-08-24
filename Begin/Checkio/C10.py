''' Вам дан результат игры, и вы должны решить, кто победил или что это ничья. Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок. В случае ничьи, результат должен быть "D". 
 Результаты игры представлены, как список (list) строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.
Вх. данные: Результат игры, как список (list) строк (str, unicode).
Вых. данные: "X", "O" или "D", как строка (str). 
 Эта задача поможет вам лучше понять, как работать с матрицами и вложеными массивами. Ну и конечно, это будет полезно при разработке игр, так как надо уметь оценивать результаты.
Предусловия:
В играх может быть только один победитель или ничья.
len(game_result) == 3
all(len(row) == 3 for row in game_result) '''
# >>> a= list('X'*3)
# >>> a
# ['X', 'X', 'X']
# >>> a=['X'*3]
# >>> a
# ['XXX']
def checkio(list1):
	column1= list1[0][0]+ list1[1][0]+ list1[2][0]
	column2= list1[0][1]+ list1[1][1]+ list1[2][1]
	column3= list1[0][2]+ list1[1][2]+ list1[2][2]
	diag1= list1[0][0]+list1[1][1]+ list1[2][2]
	diag2= list1[0][2]+list1[1][1]+ list1[2][0]

	if list1[0]=='XXX' or list1[1]=='XXX' or list1[2]=='XXX' or column1=='XXX' or column2=='XXX' or column3=='XXX' or diag1== 'XXX' or diag2== 'XXX':
		return 'X'
	elif list1[0]=='O'*3 or list1[1]=='O'*3 or list1[2]=='O'*3 or column1=='O'*3 or column2=='O'*3 or column3=='O'*3 or diag1== 'O'*3 or diag2== 'O'*3:
		return 'O'
	else:
		return 'D'

#from typing import List
# def checkio(result: List[str]) -> str:
    # for i in range(len(result)):
        # if (result[i][0]!='.')and(result[i].count(result[i][0])==3):
            # return result[i][0]
        # for j in range(len(result[0])):
            # if (result[0][i]!='.')and(result[0][i]==result[1][i]==result[2][i]):
                # return result[0][i]
    # if (result[1][1]!='.')and((result[1][1]==result[0][0]==result[2][2]) or result[1][1]==result[0][2]==result[2][0]):
        # return result[1][1]
    # return 'D'



assert checkio([
	"X.O",
	"XXX",
	".OO"]) == "X", "Xs wins"
assert checkio([
	"OO.",
	"XOX",
	"XOX"]) == "O", "Os wins"
assert checkio([
	"OOX",
	"XXO",
	"OXX"]) == "D", "Draw"
assert checkio([
	"O.X",
	"XX.",
	"XOO"]) == "X", "Xs wins again"
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")