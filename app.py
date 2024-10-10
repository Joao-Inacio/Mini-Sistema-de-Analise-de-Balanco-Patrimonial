import os
import sys

from flask import Flask

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from routes.consulta import consulta_route
from routes.home import home_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(consulta_route)

if __name__ == '__main__':
    app.run(debug=True)
