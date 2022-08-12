# This program prints Hello, world!
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish connection
s.connect(('www.google.com', 80))

#send data:
s.send(b'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n')

# recieve data:
buffer = []
while True:
    # Receive up to 1k bytes at a time:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# close the connection
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# Write the received data to a file:
with open('google.html', 'wb') as f:
    f.write(html)