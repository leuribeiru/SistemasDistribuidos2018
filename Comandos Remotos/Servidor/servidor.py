#coding: utf-8

import socket, commands

def main():
	executado_sem_retorno = "(Comando executado, porém sem retorno)"
	comando_sair = "sair"
	zfill_size = 10
	buffer_size = 16
	server_address = ('', 10000)
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(server_address)
	sock.listen(1)
	
	print("Servidor Online")
	while True:
		
		try:
			connection, client_address = sock.accept()
			print("Cliente Entrou")
			
			while True:
				dados = connection.recv(buffer_size)
				tamanho = int(dados[0:zfill_size])
				conteudo = dados[zfill_size:]
				tamanho_lido = buffer_size - zfill_size;
				while(tamanho_lido < tamanho):
					conteudo += connection.recv(buffer_size)
					tamanho_lido += buffer_size	
				
				if conteudo == "" or conteudo == comando_sair:
					print("Cliente saiu")
					raise Exception
					
				print("Recebido: " + str(conteudo))
				result = commands.getoutput(conteudo).strip()
				if result != "":
					connection.sendall(str(len(result)).zfill(zfill_size) + result)
				else:
					connection.sendall(str(len(executado_sem_retorno)).zfill(zfill_size) + executado_sem_retorno)
				
					
		except:
			connection.close()
			print("Cliente Desconectado")

	sock.close()
	
if __name__ == "__main__":
    main()
