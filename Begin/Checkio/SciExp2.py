'''Даны длины сторон треугольника и необходимо найти углы треугольника. Если невозможно сформировать треугольник из данных сторон (или для вырожденного треугольника), тогда результатом должны быть все нули. Результат должен быть представлен, как список (list) целых чисел в возрастающем порядке. Углы должны быть записаны в градусах и округляются до целого числа (стандартное округление).
 Входные данные: Длины сторон треугольник, как целые числа (int).
Выходные данные: Углы данного треугольника в градусах, как сортированный список (list) целых чисел (int).  
alpha= arrcos(b**2+ c**2 -a**2\ 2bc)
beta= arccos(a**2 + c**2 -b**2\ 2ac)
gamma= 180 -(alpha + beta)
'''
import math

def checkio(a, b, c):
	try:
		alpha= math.acos((b**2+ c**2- a**2)/ (2*b* c))
	except ValueError: return [0, 0, 0]

	beta= math.acos((a**2+ c**2- b**2)/ (2*a* c))
	gamma= 180- (math.degrees(alpha)+ math.degrees(beta))# неправильно!-Suppose the true angles are 59.6, 59.7 and 60.7. Then you’re supposed to return [60, 60, 61] and not [60]*3.
	if alpha==0 or beta==0 or gamma==0:
		return [0, 0, 0]
	list_angles = [round(math.degrees(alpha)), round(math.degrees(beta)), round(gamma)]
	return sorted(list_angles)
=======================================================================================
# from math import acos, degrees

# def checkio(a, b, c):
    # if a + b <= c or a + c <= b or b + c <= a:
        # return [0, 0, 0]
    # find_angle = lambda s1, s2, so: int(round(
        # degrees(acos((s1 ** 2 + s2 ** 2 - so ** 2) / (2 * s1 * s2))), 0)) здесь лямбда неуместна: “Always use a def statement instead of an assignment statement that binds a lambda expression directly to a name.” (new version of PEP8)
    # return sorted([find_angle(a, b, c), find_angle(a, c, b), find_angle(b, c, a)]) можно отсортить входные данные!
=======================================================================================











if __name__ == '__main__':
	assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
	assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
	assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
	print( checkio(10, 20, 30) == [0, 0, 0], "It's can not be a triangle")

	print("Coding complete? Click 'Check' to earn cool rewards!")
