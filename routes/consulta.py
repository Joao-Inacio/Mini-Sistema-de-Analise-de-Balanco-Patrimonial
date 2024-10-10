from flask import Blueprint, render_template


consulta_route = Blueprint('consulta', __name__)

@consulta_route.route('/consulta')
def consulta():
    return render_template('consulta.html')
