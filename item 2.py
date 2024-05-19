#VINICIUS YUDI
#DIRCEU CHELIGA


import hashlib
import json
import itertools
import string
import time


JSON_NAME = 'usuarios.json'

def carregar_usuarios():
    with open(JSON_NAME, 'r') as file:
        return json.load(file)


def gerar_senhas_possiveis():
    caracteres = string.ascii_lowercase + string.digits
    for senha in itertools.product(caracteres, repeat=4):
        yield ''.join(senha)


def forca_bruta_sha256(hash_target):
    for senha in gerar_senhas_possiveis():
        if hashlib.sha256(senha.encode()).hexdigest() == hash_target:
            return senha
    return None

def quebrar_senhas():
    usuarios = carregar_usuarios()
    total_time = 0
    contador = 0

    for nome, hash_senha in usuarios.items():
        contador += 1
        print(f"Quebrando a senha do usuário: {nome}")
        start_time = time.time()
        senha_quebrada = forca_bruta_sha256(hash_senha)
        end_time = time.time()
        tempo_gasto = end_time - start_time
        total_time += tempo_gasto
        print(f"Senha do usuário {nome}: {senha_quebrada}")
        print(f"Tempo para quebrar a senha: {tempo_gasto:.2f} segundos")

        if contador >= 4:  
            break

    print(f"Tempo total para quebrar 4 senhas: {total_time:.2f} segundos")
    print(f"Tempo médio por senha: {total_time / 4:.2f} segundos")


if __name__ == '__main__':
    quebrar_senhas()


#VINICIUS YUDI
#DIRCEU CHELIGA
