from domain.entities.user import User

class CreateUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, username, email):
        # Verifica se o e-mail já está cadastrado
        existing_users = self.repository.list_all()
        for user in existing_users:
            if user.email == email:
                return f"Erro: o e-mail '{email}' já está cadastrado."

        # Cria e salva o novo usuário
        user = User(username, email)
        self.repository.save(user)
        return f"Usuário '{username}' criado com sucesso!"
