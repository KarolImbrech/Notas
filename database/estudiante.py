import sqlite3
from db_notas import connect, consult, update

class Estudiante:
    def __init__(self, id, nombre, web, movil, desktop):
        self.id = id
        self.nombre = nombre
        self.web = web
        self.movil = movil
        self.desktop = desktop

