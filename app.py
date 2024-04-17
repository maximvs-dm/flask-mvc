from flask import Flask, render_template

from users import get_user

app = Flask(__name__)


@app.get('/home')
def index():
    d = {'nome': 'Rafael',
         'senha': 23}
    return render_template('index.html', **d)


@app.get('/user/<int:id_>')
def user(id_):
    d = get_user(id_)

    if d is None:
        return 'usuário não encontrado', 404

    dados = {
        'user': d,
        'pedidos': [
            {'descrição': 'Produto 1', 'valor': 10.5},
            {'descrição': 'Produto 2', 'valor': 28.99},
            {'descrição': 'Produto 3', 'valor': 231.1},
            {'descrição': 'Produto 4', 'valor': 95.4}
        ]
    }

    return render_template('users.html', **dados)


if __name__ == '__main__':
    app.run(debug=True)
