import socket
import sys

host = 'localhost'

port = 51183
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
