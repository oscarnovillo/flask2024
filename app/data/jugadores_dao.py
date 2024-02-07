
from app.data.modelo.equipo import Equipo
from app.data.modelo.jugador import Jugador

class JugadoresDao:

    def select_all(self,db,id_equipo) -> list[Jugador]:
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT j.*,e.nombre FROM 
            jugadores j inner join equipos e on j.id_equipo = e.id
            where j.id_equipo = %s
            """,[id_equipo])
        jugadores_en_db = cursor.fetchall()
        jugadores : list[Jugador]= list()
        for jugador_en_db in jugadores_en_db:
            jugadores.append(Jugador(jugador_en_db[0], jugador_en_db[1], jugador_en_db[4]))

        cursor.close()
        return jugadores
    
    def select_uno(self,db,nombre) -> Equipo:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM equipos where nombre = %s',[nombre])
        equipos_en_db = cursor.fetchall()
        if (equipos_en_db == []):
            return None
        equipo_en_db = equipos_en_db[0]        
        equipo = Equipo(equipo_en_db[0], equipo_en_db[1], equipo_en_db[2])
        cursor.close()
        return equipo

    def insert(self,db,nombre,ciudad):
        cursor = db.cursor()
        sql = ("INSERT INTO equipos (nombre,ciudad) values (%s,%s) ")
        data = (nombre,ciudad)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("delete from equipos where id = %s ")
        data = [id]
        cursor.execute(sql, data)
        db.commit()
        
    def update(self,db,id,nombre,ciudad):
        cursor = db.cursor()
        sql = ("update equipos set nombre = %s, ciudad = %s where id = %s ")
        data = [nombre,ciudad,id]
        cursor.execute(sql, data)
        db.commit()   
           
    def updateNombre(self,db,id,nombre):
        cursor = db.cursor()
        sql = ("update equipos set nombre = %s where id = %s ")
        data = [nombre,id]
        cursor.execute(sql, data)
        db.commit()           