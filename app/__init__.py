from flask import Flask

import mysql.connector 


# db = list()
db = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='informatica.iesquevedo.es',
    port = 3333,
    ssl_disabled = True,
    user ='root', #USUARIO QUE USAMOS NOSOTROS
    password ='1asir', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='testFlask'
) 



def create_app():
    app = Flask(__name__)
    app.debug = True
    

    

    from .routes import routes
    from .routes import routes_jugadores
    
    app.register_blueprint(routes.rutas_coches)
    app.register_blueprint(routes_jugadores.rutas_jugadores)


    return app
