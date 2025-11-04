from interface.user_interface import criar_usuario, listar_usuarios

def main():
    while True:
        print("\n=== Sistema Clean Architecture - Usuários ===")
        print("1. Criar novo usuário")
        print("2. Listar usuários")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            username = input("Digite o nome de usuário: ")
            email = input("Digite o e-mail: ")
            criar_usuario(username, email)

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
