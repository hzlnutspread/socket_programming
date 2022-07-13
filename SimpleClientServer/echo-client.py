import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ''
while True:
    msg = s.recv(8)  # 8 is the buffer. How big of chunks we want to receive at a time
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)