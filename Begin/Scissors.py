{R:0, P:1, S:2}
 if (human_number- comp_number)%3 ==1:
	COMPUTER_SCORE +=1
elif hum_num == comp_num:
	print('Tie')
else:
	HUMAN_SCORE +=1
# разобраться с mod : -1%3==2; -2%3==1; 1%3 ==1 ЧО ЗА БРЕД!!!