users = {
    37: {
        'nome': 'Rafael',
        'username': 'rafael123',
        'posição': 23
    }
}


def get_user(id_):
    return users.get(id_)
