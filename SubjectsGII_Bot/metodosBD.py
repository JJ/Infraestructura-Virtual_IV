import MySQLdb
import os
import urlparse

db = os.environ["NAME_BD"]
host_db = os.environ["HOST_BD"]
usuario = os.environ["USER_BD"]
pw = os.environ["PW_BD"]

def nombreAsignatura(nombAsig):
    connect_db = MySQLdb.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute(nombAsig)

    num_asig = len(cursor.fetchall())

    if num_asig != 0:
        return True

    connect_db.close()

    return False

def guiaDocenteDisponible(nombAsig):
    connect_db = MySQLdb.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute(SELECT guia_docente FROM Asignaturas WHERE asignatura = nombAsig)

    num_guia = len(cursor.fetchall())

    if num_guia != 0:
        return True

    connect_db.close()

    return False

def fechaExamenDisponible(nombAsig):
    connect_db = MySQLdb.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute(SELECT fecha_examen FROM Asignaturas WHERE asignatura = nombAsig)

    num_fecha = len(cursor.fetchall())

    if num_fecha != 0:
        return True

    connect_db.close()

    return False

def numeroAsigDisponibles():
    connect_db = MySQLdb.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute(SELECT * FROM Asignaturas)

    num_asignaturas = len(cursor.fetchall())

    connect_db.close()

    return num_asignaturas

def mostrarAsigDisponibles():
    connect_db = MySQLdb.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute(SELECT asignatura FROM Asignaturas)

    filas = len(cursor.fetchall())

    for i in filas:
        asigs += str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + "\n"

    connect_db.close()

    return asigs
