from threading import Thread
from time import sleep
from socket import socket, AF_INET, SOCK_DGRAM


def envia_mensagens(msg):
    mensagem_codificada = msg.encode()
    UDPSocket.sendto(mensagem_codificada, ('localhost', 9500))


active = True
mensagem_a_enviar = ''
UDPSocket = socket(AF_INET, SOCK_DGRAM)

nome = input("Seja bem vindo(a) ao jogo! Insira seu nome para iniciar: ")
envia_mensagens(nome)

resposta_recebida = UDPSocket.recvfrom(1024)
print(resposta_recebida[0].decode())

for partida in range(5):
    resposta_recebida = UDPSocket.recvfrom(1024)
    print(f'\n\n**** Partida {partida+1} ****')

    # Imprime pergunta
    print(resposta_recebida[0].decode())

    # Envia tentativa de resposta
    envia_mensagens(input('R -> '))

    # Verifica se resposta está correta
    status_resposta = UDPSocket.recvfrom(1024)
    print(status_resposta[0].decode())

ranking = UDPSocket.recvfrom(1024)
print(ranking[0].decode())

print('Obrigada por jogar. Volte sempre!')

