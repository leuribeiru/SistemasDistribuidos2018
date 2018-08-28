#coding: utf-8

import socket, commands


def main():
	executado_sem_retorno = "(Comando executado, porém sem retorno)"
	comando_sair = "sair"
	zfill_size = 10
	buffer_size = 16
	server_address = ('localhost', 10000)
	
	servidorOff = True
	while True:
		
		message = "";
		while message == "":
			message = raw_input("Digite um comando: ").strip()
			
		try:
			if servidorOff:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect(server_address)
				servidorOff = False
			
			sock.sendall(str(len(message)).zfill(zfill_size) + message.strip())
			dados = sock.recv(buffer_size)
			tamanho = int(dados[0:zfill_size])
			conteudo = dados[zfill_size:]
			tamanho_lido = buffer_size - zfill_size;
			while(tamanho_lido < tamanho):
				conteudo += sock.recv(buffer_size)
				tamanho_lido += buffer_size				
			
			if conteudo == "":
				raise Exception
			
			print("Executado no servidor.")
			print(conteudo)
			
		except:
			sock.close()
			servidorOff = True
			result = commands.getoutput(message).strip()
			
			print("Executado localmente.")
			if result != "" and message != comando_sair:
				print(result)
			else:
				print(executado_sem_retorno)
		finally:
			if message == comando_sair:
				sock.close()
				return 0
	
	sock.close()
	return 0

if __name__ == "__main__":
    main()

