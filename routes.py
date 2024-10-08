from flask import render_template, request, redirect, url_for
from app import app
 # Alterado para importação absoluta
from  forms import DespesaForm

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_despesa', methods=['GET', 'POST'])
def add_despesa():
    form = DespesaForm()
    if form.validate_on_submit():
        # Aqui você pode salvar os dados no banco de dados
        # Exemplo: nova_despesa = Despesa(...)
        # db.session.add(nova_despesa)
        # db.session.commit()
        return redirect(url_for('home'))  # Redireciona para a página inicial após salvar
    return render_template('index.html', form=form)
