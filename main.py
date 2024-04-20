import json

def carregar_usuarios():
    with open('usuarios.json') as f:
        return json.load(f)

def carregar_permissoes():
    with open('permissoes.json') as f:
        return json.load(f)

def autenticar_usuario(usuarios, username, password):
    if username in usuarios and usuarios[username] == password:
        return True
    else:
        return False

def verificar_permissao(permissoes, username, acao, recurso):
    if username in permissoes:
        if acao in permissoes[username] and recurso in permissoes[username][acao]:
            return True
    return False

def criar_arquivo(permissoes, username, acao, recurso):
    if username in permissoes:
        if acao in permissoes[username] and recurso in permissoes[username][acao]:
            with open(recurso, 'w') as f:
                f.write('')
            return True
    return False

def main():
    usuarios = carregar_usuarios()
    permissoes = carregar_permissoes()

    print("========================================")
    print("Bem Vindo ao nosso Sistema de Permissões")
    print("========================================")

    while True:
        username = input("Digite seu nome de usuário : ")
        password = input("Digite sua senha: ")

        if autenticar_usuario(usuarios, username, password):
            print("Autenticação bem-sucedida! Bem vindo", username)
            break
        else:
            print("Usuário ou senha inválidos.")
        sair = input("Deseja sair? (s/n): ")
        if sair.lower() == 's' or sair.lower() == 'sair':
            return

    while True:
        acao = input("Digite a ação desejada (ler, escrever, apagar, criar): ")
        recurso = input("Digite o nome do recurso: ")

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
            break

if __name__ == "__main__":
    main()
