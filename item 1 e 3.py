#VINICIUS YUDI
#DIRCEU CHELIGA

import hashlib
import json
import os
import time
import random
import string

JSON_NAME = 'usuarios.json'
TENTATIVAS_LOGIN = 'tentativas.json'

def gerar_salt(tamanho=16):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def hash_senha(senha, salt):
    return hashlib.sha256((salt + senha).encode()).hexdigest()

def carregar_usuarios():
    if os.path.exists(JSON_NAME):
        with open(JSON_NAME, 'r') as file:
            return json.load(file)
    return {}

def salvar_usuarios(usuarios):
    with open(JSON_NAME, 'w') as file:
        json.dump(usuarios, file, indent=4)

def carregar_tentativas():
    if os.path.exists(TENTATIVAS_LOGIN):
        with open(TENTATIVAS_LOGIN, 'r') as file:
            return json.load(file)
    return {}

def salvar_tentativas(tentativas):
    with open(TENTATIVAS_LOGIN, 'w') as file:
        json.dump(tentativas, file, indent=4)

def cadastrar_usuario(nome, senha):
    if len(nome) != 4 or len(senha) != 4:
        print("Nome e senha devem ter 4 caracteres.")
        return

    usuarios = carregar_usuarios()
    
    if nome in usuarios:
        print("Usuário já cadastrado.")
        return
    
    salt = gerar_salt()
    usuarios[nome] = {'salt': salt, 'hash': hash_senha(senha, salt)}
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def autenticar_usuario(nome, senha):
    if len(nome) != 4 or len(senha) != 4:
        print("Nome e senha devem ter 4 caracteres.")
        return
    
    usuarios = carregar_usuarios()
    tentativas = carregar_tentativas()
    
    if nome not in usuarios:
        print("Usuário não encontrado.")
        return
    
    if nome in tentativas and tentativas[nome]['bloqueado']:
        tempo_restante = tentativas[nome]['bloqueado_ate'] - time.time()
        if tempo_restante > 0:
            print(f"Conta bloqueada. Tente novamente em {int(tempo_restante)} segundos.")
            return
        else:
            tentativas[nome]['bloqueado'] = False
            tentativas[nome]['tentativas'] = 0
    
    salt = usuarios[nome]['salt']
    hash_stored = usuarios[nome]['hash']
    hash_attempt = hash_senha(senha, salt)
    
    if hash_stored == hash_attempt:
        print("Autenticação bem-sucedida!")
        tentativas[nome] = {'tentativas': 0, 'bloqueado': False, 'bloqueado_ate': 0}
    else:
        if nome not in tentativas:
            tentativas[nome] = {'tentativas': 0, 'bloqueado': False, 'bloqueado_ate': 0}
        
        tentativas[nome]['tentativas'] += 1
        if tentativas[nome]['tentativas'] >= 3:
            tentativas[nome]['bloqueado'] = True
            tentativas[nome]['bloqueado_ate'] = time.time() + 60  # Bloqueia por 60 segundos
            print("Muitas tentativas falhas. Conta bloqueada por 60 segundos.")
        else:
            print("Senha incorreta.")
    
    salvar_tentativas(tentativas)

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

# Executar o programa
if __name__ == '__main__':
    main()

#VINICIUS YUDI
#DIRCEU CHELIGA
