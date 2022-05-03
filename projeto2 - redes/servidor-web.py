import mimetypes
import os
from datetime import datetime
from email.utils import formatdate
from socket import socket, AF_INET, SOCK_STREAM
import time


def lista_diretorio(lista_arquivos, stamp_ls, req_ls, req_index):
    resposta = ''
    resposta += 'HTTP/1.1 200 OK\r\n'
    resposta += f'Date: {formatdate(timeval=stamp_ls, localtime=False, usegmt=True)}\r\n'
    resposta += 'Server: Apache /0.0.0.1 (Python)\r\n'
    resposta += 'Content-Type: text/html\r\n'
    resposta += '\r\n'

    if os.name == 'nt':
        nivel_diretorio = req_index.count('\\')
    else:
        nivel_diretorio = req_index.count('/')

    html_ls = ''
    html_ls += f'<!DOCTYPE html>'
    html_ls += f'<head><meta charset="UTF-8"><title>Index de {req_index}</title></head>'

    html_ls += f'<table><h1>Index de {req_index}</h1>'

    html_ls += '<thead>'
    html_ls += f'<tr>' \
               f'<th>Tipo de arquivo</th>' \
               f'<th>Nome do arquivo</th>' \
               f'<th>Último modificado</th>' \
               f'<th>Tamanho</th>' \
               f'</tr><thead>'
    html_ls += '<tbody>'

    for arquivo in lista_arquivos:
        try:
            try:
                extensao = arquivo.split('.')[1]

                if extensao == 'iso':
                    content_type = 'application/octet-stream'
                else:
                    content_type = mimetypes.guess_type('teste.' + extensao)[0]
            except IndexError:
                content_type = 'Folder'

            if nivel_diretorio == 1 and (req_index == "/" or req_index == "\\"):

                html_ls += '<tr>'
                html_ls += f'<td>{content_type}</td>'
                html_ls += f'<td><a href = "{req_index + arquivo}">{arquivo}</a></td>'
                html_ls += f'<td> {time.ctime(os.path.getmtime(req_ls + arquivo))} </td>'
                html_ls += f'<td>{str(os.path.getsize(req_ls + arquivo)) + " bytes"} </td>'

            else:
                html_ls += '<tr>'
                html_ls += f'<td>{content_type}</td>'
                html_ls += f'<td><a href = "{req_index + "/" + arquivo}">{arquivo}</a></td>'
                html_ls += f'<td> {time.ctime(os.path.getmtime(req_ls + "/" + arquivo))} </td>'
                html_ls += f'<td>{str(os.path.getsize(req_ls + "/" + arquivo)) + " bytes"} </td>'

        except FileNotFoundError:
            html_ls += '<tr>'
            html_ls += f'<td > - </td>'
            html_ls += f'<td > - </td>'
            html_ls += f'<td > - </td>'
            html_ls += f'<td > - </td></tr>'

    html_ls += '<!-- partial --></body>'
    html_ls += '</html>'

    resposta += html_ls

    return resposta


def return_code_505(stamp505):
    res505 = ''
    res505 += 'HTTP/1.1 505 HTTP Version Not Supported\r\n'
    res505 += f'Date: {formatdate(timeval=stamp505, localtime=False, usegmt=True)}\r\n'
    res505 += 'Server: CIn UFPE/0.0.0.1 (Ubuntu)\r\n'
    res505 += 'Content-Type: text/html\r\n'
    res505 += '\r\n'

    html505 = ''
    html505 += '<html>'
    html505 += '<head>'
    html505 += '<title>Not Supported - CIn/UFPE</title>'
    html505 += '<meta charset="UTF-8">'
    html505 += '</head>'
    html505 += '<body>'
    html505 += '<h1>505 - HTTP Version Not Supported</h1>'
    html505 += '</body>'
    html505 += '</html>'

    res505 += html505
    socket_cliente.send(res505.encode())

    print('505 http version not supported')


def return_code_501(stamp501):
    res501 = ''
    res501 += 'HTTP/1.1 501 Not Implemented\r\n'
    res501 += f'Date: {formatdate(timeval=stamp501, localtime=False, usegmt=True)}\r\n'
    res501 += 'Server: CIn UFPE/0.0.0.1 (Ubuntu)\r\n'
    res501 += 'Content-Type: text/html\r\n'
    res501 += '\r\n'

    html501 = ''
    html501 += '<html>'
    html501 += '<head>'
    html501 += '<title>Not Implemented - CIn/UFPE</title>'
    html501 += '<meta charset="UTF-8">'
    html501 += '</head>'
    html501 += '<body>'
    html501 += '<h1>501 Not Implemented</h1>'
    html501 += '</body>'
    html501 += '</html>'

    res501 += html501
    socket_cliente.send(res501.encode())

    print('501 not implemented')

def return_code_400(stamp400):
    res400 = ''
    res400 += 'HTTP/1.1 400 Bad Request\r\n'
    res400 += f'Date: {formatdate(timeval=stamp400, localtime=False, usegmt=True)}\r\n'
    res400 += 'Server: CIn UFPE/0.0.0.1 (Ubuntu)\r\n'
    res400 += 'Content-Type: text/html\r\n'
    res400 += '\r\n'

    html400 = ''
    html400 += '<html>'
    html400 += '<head>'
    html400 += '<title>Bad Request</title>'
    html400 += '<meta charset="UTF-8">'
    html400 += '</head>'
    html400 += '<body>'
    html400 += '<h1>400 - Mensagem de requisição não entendida pelo servidor</h1>'
    html400 += '</body>'
    html400 += '</html>'

    res400 += html400
    socket_cliente.send(res400.encode())

    print('400 Bad Request')


def return_code_404(stamp404, file_not_found):
    resposta404 = ''
    resposta404 += 'HTTP/1.1 404 Not Found\r\n'
    resposta404 += f'Date: {formatdate(timeval=stamp404, localtime=False, usegmt=True)}\r\n'
    resposta404 += 'Server: CIn UFPE/0.0.0.1 (Ubuntu)\r\n'
    resposta404 += 'Content-Type: text/html\r\n'
    resposta404 += '\r\n'

    html404 = ''

    html404 += '<html>'
    html404 += '<head>'
    html404 += '<title>Not Found - CIn/UFPE</title>'
    html404 += '<meta charset="UTF-8">'
    html404 += '</head>'
    html404 += '<body>'
    html404 += '<h1>Erro 404</h1>'
    html404 += '</body>'

    html404 += '<body>'
    html404 += f'<h2>A requisicao para {file_not_found} não foi encontrada no servidor</h2>'
    html404 += '</body>'
    html404 += '</html>'

    html404 += '<td valign="top"></td>'
    html404 += f'<td><a href="{os.path.join(file_not_found, os.pardir)}">Retornar para o diretório pai</a></td>'
    html404 += '<td>&nbsp;</td>'

    resposta404 += html404

    socket_cliente.send(resposta404.encode())
    print('404 not found')


def return_file_200(stamp_200, req_200):
    # Descobrir a extensao do arquivo solicitado

    extensao = req_200.split('.')[1]

    if extensao == 'iso':
        content_type = 'application/octet-stream'
    else:
        content_type = mimetypes.guess_type('teste.' + extensao)[0]

    print(f'Extensao: {content_type}')

    arq_requisitado = open(req_200, 'rb')

    # Caso o arquivo requisitado seja encontrado
    resposta = ''
    resposta += 'HTTP/1.1 200 OK\r\n'
    resposta += f'Date: {formatdate(timeval=stamp_200, localtime=False, usegmt=True)}\r\n'
    resposta += 'Server: CIn UFPE/0.0.0.1 (Windows)\r\n'
    resposta += f'Content-Length: {os.path.getsize(req_200)}\r\n'
    resposta += f'Content-Type: {content_type}\r\n'
    resposta += '\r\n'

    socket_cliente.send(resposta.encode())

    try:
        while True:
            pedaco = arq_requisitado.read(1024)
            if len(pedaco) == 0:
                arq_requisitado.close()
                break
            else:
                socket_cliente.send(pedaco)

    except ConnectionAbortedError:
        print("Conexão interrompida!")


def return_dir_200(stamp_ls, req_ls, req_index):
    print('É diretório!', req_ls)

    lista_arquivos = os.listdir(req_ls)

    if any('index.html' in arquivo for arquivo in lista_arquivos):
        print("Tem aquivo index.html!")
        req_ls += '/index.html'

        return_file_200(stamp_ls, req_ls)

    else:
        print("Sem index.html --> Listando o diretório")

        resposta = lista_diretorio(lista_arquivos, stamp_ls, req_ls, req_index)
        socket_cliente.send(resposta.encode())


# Inicio - main()

socket_servidor = socket(AF_INET, SOCK_STREAM)
host = 'localhost'
porta = 7745
socket_servidor.bind((host, porta))
git

print(f'Servidor WEB ouvindo requisições em http://{host}:{porta}')

pasta_base = 'Arquivos'
os.chdir(pasta_base)
dir_base = os.getcwd()

requisicao_anterior = ''

# t = Thread(target=recebe_mensagens, daemon=True)  #Thread para receber mensagens dos usuarios
# t.start()

while True:
    # Ouve por novas requisições
    socket_servidor.listen()
    # Aceita cada uma delas
    socket_cliente, endereco_cliente = socket_servidor.accept()

    # Recebe os dados dessas requisicões
    dados = socket_cliente.recv(2048)
    requisicao = dados.decode()

    print('\n** Requisição recebida **')

    # Caso nao seja uma requisicao vazia
    if requisicao != '':

        # Data atual
        now = datetime.now()
        stamp = time.mktime(now.timetuple())

        try:
            linhas = requisicao.strip().split('\r\n')

            # valores_http = {}  # Guarda os valores dos cabeçalhos HTTP
            metodo, requisicao, versao_http = '', '', ''

            for i, linha in enumerate(linhas):
                if i == 0:
                    colunas = linha.split(' ')
                    metodo = colunas[0]
                    requisicao = colunas[1].replace('%20', ' ')  # %20 = espaço
                    versao_http = colunas[2]
                else:
                    colunas = linha.split(':')
                    # valores_http[colunas[0]] = colunas[1].strip()

            print(metodo, versao_http, requisicao)

            if os.name == 'nt':
                divisor = '\\'
                requisicao = requisicao.replace('/', divisor)
            else:
                divisor = '/'  

            # Verifica versao HTTP
            if versao_http != 'HTTP/1.1':
                return_code_505(stamp)

            # Verifica metodo
            elif metodo != 'GET':
                return_code_501(stamp)

            else:
                #try:
                requisicao_abs = dir_base + requisicao  # diretorio absoluto do arquivo/diretorio solicitado

                parent = requisicao_abs.rsplit(divisor, 1)[0]
                file = requisicao_abs.rsplit(divisor, 1)[1]

                curr = os.getcwd()
                os.chdir(parent)

                if os.path.isfile(requisicao_abs):  # caso requisição seja arquivo, verifica se ele existe
                    return_file_200(stamp, requisicao_abs)  # arquivo existe

                elif os.path.isdir(requisicao_abs):  # caso requisicao seja diretorio, verifica se ele existe

                    requisicao_anterior = requisicao_abs
                    return_dir_200(stamp, requisicao_abs, requisicao)  # diretorio existe

                elif os.path.isfile(
                        requisicao_anterior + divisor + file):  # caso requisicao anterior tenha um objeto incorporado
                    print('Objeto Incorporado!')
                    return_file_200(stamp, requisicao_anterior + divisor + file)

                else:  # não encontrou nada
                    return_code_404(stamp, requisicao)

                os.chdir(curr)

        except IndexError:
            return_code_400(stamp)

    else:
        print('Recebeu req vazia do navagador')

    # Finaliza a conexao com o cliente (HTTP nao persistente)
    socket_cliente.close()
