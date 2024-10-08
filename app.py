from flask import Flask, render_template, request, redirect
import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from forms import DespesaForm 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_secreta'  # Necessário para WTForms

# Conexão simples com o banco de dados SQLite
def conecta_bd():
    return sqlite3.connect('data/balanco.db')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DespesaForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Pegando os dados do formulário e inserindo no banco
        conn = conecta_bd()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO despesas (ano, mes, dia, tipo, descricao, valor, prioridade) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (
                form.ano.data, form.mes.data, form.dia.data, form.tipo.data,
                form.descricao.data, form.valor.data, form.prioridade.data
            )
        )
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
