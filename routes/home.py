from flask import Blueprint, render_template


home_route = Blueprint('home', __name__)

@home_route.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@home_route.route('/', methods=['POST'])
def inserir_dados():
    # Inseri dados no banco de dados
    ...

