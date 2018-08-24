 # определить угол солнца над горизонтом, зная время суток. Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов. В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00 солнце садится за горизонт и угол равен 180 градусов. В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".
 # Входные данные: Время в виде строки 
# Выходные данные: Угол солнца над горизонтом, округленный до 2 знаков после запятой. 
# Предусловия:
# 00:00 <= время <= 23:59 -->  180/(12* 3600)

#Преобразуем время в кол-во минут от восхода, если <0 или >(12* 60= 720) --> 'не вижу', else : *0,175
import datetime

def sun_angle(time):
	time= datetime.datetime.strptime(time, "%H:%M")# возвращает объект, а нужно - время из него в секундах
	print(time)# 1900-01-01 07:00:00
	time_start= datetime.datetime.strptime('06:00', "%H:%M")
	print(time_start)# 1900-01-01 06:00:00
	time_end= datetime.datetime.strptime('18:00', "%H:%M")
	print(time_end)
	if time_start<= time <= time_end:
		return (time - time_start).total_seconds()* (180/(12* 3600)) # в минутах хочу (хотя проще- в секундах?)
	else:
		return "I don't see the sun!"

    # h, m = map(int, time.split(":"))
    # total_minutes = h * 60 + m
    # # 06:00 = 360 minutes, 18:00 = 1080 minutes
    # if 360 <= total_minutes <= 1080:
        # # 0.25 degree in one minute
        # return (total_minutes - 360) * 0.25
    # else:
        # return "I don't see the sun!"

# sun_angle=lambda t:["I don't see the sun!",int(t[:2])*15+int(t[~1:])/4-90][6<=int(t[:2])+int(t[~1:])/60<=18]

# degrees = (int(time[0:2]) + int(time[3:])/60) * 15 - 90
# return degrees if 0 <= degrees <= 180 else "I don't see the sun!"





if __name__ == '__main__':
	#sun_angle(time)

	assert sun_angle("07:00") == 15
	assert sun_angle("01:23") == "I don't see the sun!"
	print("Coding complete? Click 'Check' to earn cool rewards!")