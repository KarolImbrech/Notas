import sqlite3

def connect():
    try:
        conn = sqlite3.connect('notas.db')
        cursor = conn.cursor()

        return conn
    except sqlite3.Error as err:
        print(err)
        return None


def update(id, asignatura, nota):
        conn = sqlite3.connect('notas.db')
        cursor = conn.cursor()
        try:
            instruccion = "UPDATE estudiantes SET " + asignatura + "=" +  str(nota) + " WHERE id=" + str(id) + ";"
            cursor.execute(instruccion)
            conn.commit()
            print("Nota actualizada")
            return True
        except sqlite3.Error as err:
            print("error: " + str(err))
            return False
        
def consult(id): 
        try:
            conn = sqlite3.connect('notas.db')
            cursor = conn.cursor()
            instruction = "SELECT * FROM estudiantes WHERE id=" + str(id) + ";"         
            cursor.execute(instruction)
            notas = cursor.fetchone()
            return notas
        except sqlite3.Error as err:
            print("error: " + str(err))