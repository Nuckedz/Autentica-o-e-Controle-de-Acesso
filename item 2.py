import hashlib
import json
import itertools
import string
import time

# Nome do arquivo onde os usuários estão armazenados
JSON_NAME = 'usuarios.json'

# Carregar os usuários do arquivo
def carregar_usuarios():
    with open(JSON_NAME, 'r') as file:
        return json.load(file)

# Gerar todas as combinações possíveis de senhas de 4 caracteres
def gerar_senhas_possiveis():
    caracteres = string.ascii_lowercase + string.digits
    for senha in itertools.product(caracteres, repeat=4):
        yield ''.join(senha)

# Função de força bruta para encontrar a senha original a partir do hash
def forca_bruta_sha256(hash_target):
    for senha in gerar_senhas_possiveis():
        if hashlib.sha256(senha.encode()).hexdigest() == hash_target:
            return senha
    return None

# Função principal para quebrar as senhas de 4 usuários e calcular o tempo necessário
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

        if contador >= 4:  # Limitar a quebra de senha a 4 usuários
            break

    print(f"Tempo total para quebrar 4 senhas: {total_time:.2f} segundos")
    print(f"Tempo médio por senha: {total_time / 4:.2f} segundos")

# Executar a função de quebra de senhas
if __name__ == '__main__':
    quebrar_senhas()
