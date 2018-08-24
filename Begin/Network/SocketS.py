import socket

def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8007
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()'''conn - new socket, блокирует приложение до запроса! В реале клиентов тысячи: Для этого существует несколько различных подходов:
    использование отдельного потока на каждого клиента;
    использование неблокирующих сокетов;
    использование select/poll.

В Python неблокирующий сокет реализуется с помощью специального метода setblocking() с параметром, равным нулю.
Пример:
lstn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs = []
nc = 2
for i in range(nc):
   (clnt,ap) = lstn.accept()
   clnt.setblocking(0)
   cs.append(clnt)
Недостаток этого метода в том, что нам вручную нужно проверять готовность каждого клиента. Третий вариант с использованием select() позволяет переложить эту проверку на саму операционную систему. Более поздняя его вариация – функция poll().'''
    print('Connection from: ', addr)
    while True:
        data= conn.recv(1024)
        if not data:# Сколько ждем??
            break
        print('From connected user: ', data )# получает ответ в байтах а печатает строкой...?
        response= str.encode(input('Respond is '))
        conn.send(response)# conn not s!!!
    '''data = conn.recv(1024)
    print('client is at', addr, data)
    conn.send(data)
    z = raw_input()
    s.close() нужно ли дублировать закрытие'''

    conn.close()
if __name__ == '__main__':
    Main()
