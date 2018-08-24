'''To calculate max walk to distance of 4 units'''
import random

x, y = (0, 0)
lenth_walk = 30
def distance(lenth_walk):
	for i in lenth_walk:
		(dx, dy) = random.choice[(0, 1),(0, -1), (1, 0), (-1, 0)]
		x  += dx
		y += dy
		i += 1
		