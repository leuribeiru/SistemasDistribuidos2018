#coding: utf-8

import socket, commands

def main():
	server_address = ('localhost', 10000)
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(server_address)
	
	sock.listen(1)
	
	while True:
		connection, client_address = sock.accept()
		
		try:
			while True:
				data = connection.recv(512)
				
				if data == "exit":
					print("Cliente saiu")
					break;
					
				print("received: " + str(data))
				result = commands.getoutput(data)
					
				connection.sendall(result)
		except:
			break;
	
	connection.close()
	sock.close()
	
if __name__ == "__main__":
    main()
