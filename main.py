#VINICIUS YUDI 
#JOAO TANCON

import json
import getpass

def carregar_usuarios():
    try:
        with open('usuarios.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def carregar_permissoes():
    try:
        with open('permissoes.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

def salvar_permissoes(permissoes):
    with open('permissoes.json', 'w') as f:
        json.dump(permissoes, f)

def autenticar_usuario(usuarios, username, password):
    return username in usuarios and usuarios[username] == password

def verificar_permissao(permissoes, username, acao, recurso):
    if username in permissoes:
        return acao in permissoes[username] and recurso in permissoes[username][acao]
    return False

def criar_arquivo(permissoes, username, acao, recurso):
    if username in permissoes and acao == 'criar' and recurso in permissoes[username].get('criar', []):
        with open(recurso, 'w') as f:
            f.write('')
        return True
    return False

def criar_usuario(usuarios, permissoes, username, password):
    if username not in usuarios:
        usuarios[username] = password
        permissoes[username] = {'ler': [], 'escrever': [], 'apagar': [], 'criar': []}
        permissoes[username]['criar'].append(username)  # Permite que o usuário crie arquivos com seu próprio nome
        salvar_usuarios(usuarios)
        salvar_permissoes(permissoes)
        return True
    return False

def menu():
    print("1. Autenticar/Login")
    print("2. Criar novo usuário")
    print("3. Sair")

def main():
    usuarios = carregar_usuarios()
    permissoes = carregar_permissoes()

    print("========================================")
    print("Bem Vindo ao nosso Sistema de Permissões")
    print("========================================")

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            username = input("Digite seu nome de usuário: ")
            password = getpass.getpass("Digite sua senha: ")

            if autenticar_usuario(usuarios, username, password):
                print("Autenticação bem-sucedida! Bem-vindo,", username)
                break
            else:
                print("Usuário ou senha inválidos.")
        elif opcao == '2':
            username = input("Digite o nome de usuário desejado: ")
            password = input("Digite a senha desejada: ")

            if criar_usuario(usuarios, permissoes, username, password):
                print("Usuário criado com sucesso!")
            else:
                print("Usuário já existe.")
        elif opcao == '3':
            print("Até logo.")
            return
        else:
            print("Opção inválida.")

    while True:
        acao = input("Digite a ação desejada (ler, escrever, apagar, criar): ")
        recurso = input("Digite o nome do arquivo: ")

        if acao == 'criar':
            if criar_arquivo(permissoes, username, acao, recurso):
                print("Arquivo criado com sucesso.")
            else:
                print("Você não tem permissão para criar arquivos.")
        else:
            if verificar_permissao(permissoes, username, acao, recurso):
                print("Acesso permitido.")
            else:
                print("Acesso negado.")

        print()
        sair = input("Deseja sair? (s/n): ")
        if sair.lower() == 's' or sair.lower() == 'sair': 

            print("========")
            print("Até logo")
            print("========")
            break

if __name__ == "__main__":
    main()
