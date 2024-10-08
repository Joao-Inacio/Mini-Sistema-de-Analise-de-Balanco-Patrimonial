from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class DespesaForm(FlaskForm):
    ano = SelectField(
        'Ano', choices=[
            ('2021', '2021'), ('2022', '2022'), ('2023', '2023'),
            ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), 
            ('2027', '2027'), ('2028', '2028'), ('2029', '2029')
            ], 
        validators=[DataRequired()]
    )
    mes = SelectField(
        'Mês', choices=[
            ('01', 'Janeiro'), ('02', 'Fevereiro'), ('03', 'Março'),
            ('04', 'Abril'), ('05', 'Maio'), ('06', 'Junho'),
            ('07', 'Julho'), ('08', 'Agosto'), ('09', 'Setembro'), 
            ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')
        ], validators=[DataRequired()])
    dia = IntegerField(
        'Dia', validators=[DataRequired(), NumberRange(min=1, max=31)]
    )
    tipo = SelectField(
        'Tipo', choices=[
            ('1', 'Alimentação'), ('2', 'Educação'), ('3', 'Lazer'), 
            ('4', 'Saúde'), ('5', 'Transporte')
            ], validators=[DataRequired()])
    descricao = StringField('Descrição')
    valor = DecimalField('Valor', validators=[DataRequired()])
    prioridade = SelectField(
        'Prioridade', choices=[
            ('alta', 'Alta'), ('media', 'Média'), ('baixa', 'Baixa')
            ], validators=[DataRequired()])
    submit = SubmitField('Adicionar')
