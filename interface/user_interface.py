from application.use_cases.create_user import CreateUser
from application.use_cases.list_users import ListUsers
from infrastructure.repositories.user_repository import UserRepository

# Instância única do repositório (mantém dados enquanto o sistema está rodando)
repo = UserRepository()

# Casos de uso
create_user_uc = CreateUser(repo)
list_users_uc = ListUsers(repo)

def criar_usuario(username, email):
    result = create_user_uc.execute(username, email)
    print(result)

def listar_usuarios():
    users = list_users_uc.execute()
    if not users:
        print("Nenhum usuário cadastrado ainda.")
        return
    print("\nUsuários cadastrados:")
    for u in users:
        print(f"- {u.username} ({u.email})")
