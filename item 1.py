#VINICIUS YUDI
#DIRCEU CHELIGA

import hashlib
import json
import os

JSON_NAME = 'usuarios.json'

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
    if os.path.exists(JSON_NAME):
        with open(JSON_NAME, 'r') as file:
            return json.load(file)
    return {}

def salvar_usuarios(usuarios):
    with open(JSON_NAME, 'w') as file:
        json.dump(usuarios, file, indent=4)

def cadastrar_usuario(nome, senha):
    if len(nome) != 4 or len(senha) != 4:
        print("Nome e senha devem ter 4 caracteres.")
        return

    usuarios = carregar_usuarios()
    
    if nome in usuarios:
        print("Usuário já cadastrado.")
        return
    
    usuarios[nome] = hash_senha(senha)
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def autenticar_usuario(nome, senha):
    if len(nome) != 4 or len(senha) != 4:
        print("Nome e senha devem ter 4 caracteres.")
        return
    
    usuarios = carregar_usuarios()
    
    if nome not in usuarios:
        print("Usuário não encontrado.")
        return
    
    if usuarios[nome] == hash_senha(senha):
        print("Autenticação bem-sucedida!")
    else:
        print("Senha incorreta.")

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Usuário")
        print("2. Autenticar Usuário")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do usuário (4 caracteres): ")
            senha = input("Digite a senha do usuário (4 caracteres): ")
            cadastrar_usuario(nome, senha)
        elif escolha == '2':
            nome = input("Digite o nome do usuário (4 caracteres): ")
            senha = input("Digite a senha do usuário (4 caracteres): ")
            autenticar_usuario(nome, senha)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()

#VINICIUS YUDI
#DIRCEU CHELIGA
