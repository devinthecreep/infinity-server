import socket, time, os

host = ("206.189.66.223")
port = 80

s = socket.socket()

s.bind((host, port))

while True:
	try:
		s.listen(1)
		conn, address = s.accept()
		break

	except:
		pass

print ("Connected to: " + str(address[0]))
conn.close()
s.close()

