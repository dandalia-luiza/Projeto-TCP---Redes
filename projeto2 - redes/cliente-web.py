from socket import socket, AF_INET, SOCK_STREAM

socket_cliente = socket(AF_INET, SOCK_STREAM)


socket_cliente.connect(('localhost', 7745))

mensagem = ''
mensagem += 'GET /danda HTTP/1.0\r\n'
mensagem += 'Host: localhost:7745\r\n'
mensagem += 'Connection: close\r\n'
mensagem += 'Accept-Language: pt-BR,pt;q=0.9\r\n'
mensagem += ('User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
             '(KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36\r\n')
mensagem += '\r\n'

socket_cliente.send(mensagem.encode())

dados = socket_cliente.recv(2048)

mensagem = dados.decode()

print('Resposta recebida: ')
print(f'{mensagem}')
