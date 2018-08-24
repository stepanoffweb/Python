import socket


def Main():
    host = '127.0.0.1'
    port = 8007
    addr = (host, port)

    s = socket.socket()  # два параметра по умолчанию? (TCP)
    s.connect(addr)
    msg = input('-> ')
    while msg != 'q':
        data = str.encode(msg)
        s.send(data)  # TypeError: a bytes-like object is required, not 'str'
        data = bytes.decode(s.recv(1024))
        print('Recieved from server: {}'.format(data))
        msg = input('->')
    s.close()  # Освобождаем порт
    print('Disconnected')


if __name__ == '__main__':
    Main()
