from socket import *


ip_adress = ""
PORTA = 40000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((ip_adress, PORTA))
serverSocket.listen(1)
print("Servidor pronto para receber !")

while 1:
    connectionSocket, addr = serverSocket.accept()
    
    sentence = connectionSocket.recv(500000000)
    conteudo = sentence.decode()
    print("\nFrom client:", conteudo)

    
    resposta = input('Digite a resposta a ser enviada para o cliente: ')
    if resposta == "EXIT":
        break
    else:
        connectionSocket.send(resposta.encode())

