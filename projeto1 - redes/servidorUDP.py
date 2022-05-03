from threading import Thread
from time import sleep
from socket import socket, AF_INET, SOCK_DGRAM
import random


def ler_arquivo():
    arq_perguntas = open("perguntas.txt", "r")
    dados = arq_perguntas.read().split("\n")
    arq_perguntas.close()
    ls = []
    for n in range(len(dados)):
        if n % 2 == 0:
            ls.append([dados[n], dados[n + 1]])
    return ls


def envia_mensagens(msg, endereco):
    mensagem_codificada = msg.encode()
    UDPServerSocket.sendto(mensagem_codificada, endereco)


continua = True
UDPServerSocket = socket(AF_INET, SOCK_DGRAM)
UDPServerSocket.bind(('localhost', 9500))
print("Servidor UDP ouvindo mensagens de clientes...")

lista_perguntas = ler_arquivo()

# Inicia o jogo
resposta_recebida = UDPServerSocket.recvfrom(1024)

nome_cliente = resposta_recebida[0].decode()
endereco_cliente = resposta_recebida[1]
print(f'Jogador: {nome_cliente} se conectou no endereço {endereco_cliente}!')
print('Enviando mensagem de boas vindas')
sleep(1)
envia_mensagens('Seja bem vindo ao jogo! Iniciando partida em 5 segundos...', endereco_cliente)
sleep(5)
print('Iniciando partida')

# Escolhe 5 perguntas aleatórias

lista_perguntas_temp = []
for x in range(5):
    elemento = random.choice(lista_perguntas)
    if elemento not in lista_perguntas_temp:
        lista_perguntas_temp.append(elemento)

# 5 partidas

pontuacao = []

continua = True

for x in range(5):
    print(f'\n\nPartida {x+1}')
    print('Pergunta: ', lista_perguntas_temp[x-1][0])
    print('Resposta esperada: ', lista_perguntas_temp[x-1][1])
    sleep(0.5)
    envia_mensagens(lista_perguntas_temp[x-1][0], endereco_cliente)
    print('----Enviou pergunta')
    respx = UDPServerSocket.recvfrom(1024)
    resp = respx[0].decode()

    print('----Resposta devolvida: ', resp)

    if resp == lista_perguntas_temp[x-1][1]:
        envia_mensagens('Resposta correta! [+20 pontos]', endereco_cliente)
        print('Resposta correta [+20 pontos]')
        pontuacao.append(20)
    else:
        envia_mensagens('Resposta incorreta 😥 [-5 pontos]', endereco_cliente)
        print('Resposta incorreta [-5 pontos]')
        pontuacao.append(-5)
    sleep(2)

ranking = ''
ranking += '\n\nFim de Jogo! Obrigada por jogar!\n'
ranking += 'Ranking:\n'

pont_total = 0

for x in range(0, 5):
    ranking += f'Partida {x+1} ---> {pontuacao[x]}\n'
    pont_total += pontuacao[x]
    
ranking += '---------------\n'
ranking += f'Pontuação Final: {pont_total}\n'

envia_mensagens(ranking, endereco_cliente)

print('Fim de jogo.')
