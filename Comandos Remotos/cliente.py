#coding: utf-8

import socket


def main():
	server_address = ('localhost', 10000)
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(server_address)
	
	while True:
		
		message = raw_input("Digite um comando: ")
			
		try:
			sock.sendall(message)
			
			if(message == "exit"):
				break;
				
			data = sock.recv(512)
			print(data)
			
		except:
			break;
	sock.close()

if __name__ == "__main__":
    main()

