import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.jugadores_dao import JugadoresDao
from app.data.equipo_dao import EquipoDao
from app.data.modelo.equipo import Equipo


rutas_jugadores = Blueprint("routes_jugadores", __name__)


@rutas_jugadores.route('/delJugador', methods=['POST'])   
def delEquipo():
    id = request.form['id']
    equipo_dao = EquipoDao()
    equipo_dao.delete(db,id)
   
    return redirect(url_for('routes.verEquipos'))  



@rutas_jugadores.route('/verJugadores', methods=['POST','GET'])   
def verJugadores():
    jugadores = list()
    nombreEquipo = ""
    equipo_dao = EquipoDao()
    equipos = equipo_dao.select_all(db)
    

    if (request.method == 'POST'):
        id_equipo = request.form['id_equipo']
        jugadores_dao = JugadoresDao()
        jugadores = jugadores_dao.select_all(db,id_equipo)
        for equipo in equipos:
            
            if (id_equipo == str(equipo.id)):
               
                nombreEquipo  = equipo.nombre



    return render_template('jugadores.html',
                           jugadores=jugadores,
                           equipos=equipos,
                           nombreEquipo=nombreEquipo)