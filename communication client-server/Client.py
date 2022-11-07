from socket import *
from time import *


ip_adress = ""
PORTA = 40000
sentence = input("Digite a mensagem a ser enviada: ")

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((ip_adress, PORTA))

    'envia mensagem'
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(500000000)

    print("From server:", modifiedSentence.decode())

    sentence = input("\nDigite a mensagem a ser enviada: ")
    if sentence == "EXIT":
        break


