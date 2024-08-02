# Importação de biblioteca getpass
import getpass as gtp

usuario = input("Nome do usuário: ")
senha = gtp.getpass("Digite sua senha: ")

# Verificação do número de caracteres da senha
if len(senha) >= 6:
    print(f"Usuário cadastrado com sucesso!")
else:
    print("Atenção! A senha deve ter no mínimo 6 dígitos!!")
