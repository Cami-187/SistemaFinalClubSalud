import tkinter as tk
from tkinter import messagebox
from functools import reduce
from datetime import datetime
import re
import logging

def validar_dni(dni):
    return bool(re.fullmatch('[0-9]{8}', dni))

def validar_telefono(telefono):
    return bool(re.fullmatch('[0-9]{9}', telefono))

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validar_hora(hora):
    try:
        datetime.strptime(hora, '%H:%M')
        return bool(re.fullmatch('[0-9]{2}:[0-9]{2}', hora))
    except ValueError:
        return False

def ocultar_dni(dni):
    return '****' + dni[-4:]
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')

# HERENCIA: Paciente y Medico comparten los datos basicos de Persona.
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre



