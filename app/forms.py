from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired


class DespesaFrom(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired()])
    valor = DecimalField('Valor', validators=[DataRequired()])
    prioridade = SelectField('Prioridade', choices=[
        ('alta', 'Alta'),
        ('media', 'Média'),
        ('baixa', 'Baixa'),
    ], validators=[DataRequired()])
    submit = SubmitField('Adicionar Despesa')
