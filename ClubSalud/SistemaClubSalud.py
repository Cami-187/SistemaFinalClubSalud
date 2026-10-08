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


class Paciente(Persona):

    def __init__(self, codigo, nombre, dni, direccion, telefono, edad, sexo, fecha_nacimiento, procedencia, grado_instruccion, estado_civil, ocupacion, acompanante, parentesco, telefono_acompanante):
        super().__init__(nombre)
        self.__codigo = codigo
        self.__nombre = nombre
        self.__dni = dni
        self.__direccion = direccion
        self.__telefono = telefono
        self.__edad = edad
        self.__sexo = sexo
        self.__fecha_nacimiento = fecha_nacimiento
        self.__procedencia = procedencia
        self.__grado_instruccion = grado_instruccion
        self.__estado_civil = estado_civil
        self.__ocupacion = ocupacion
        self.__acompanante = acompanante
        self.__parentesco = parentesco
        self.__telefono_acompanante = telefono_acompanante

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_procedencia(self):
        return self.__procedencia

    def get_grado_instruccion(self):
        return self.__grado_instruccion

    def get_estado_civil(self):
        return self.__estado_civil

    def get_ocupacion(self):
        return self.__ocupacion

    def get_acompanante(self):
        return self.__acompanante

    def get_parentesco(self):
        return self.__parentesco

    def get_telefono_acompanante(self):
        return self.__telefono_acompanante

    def mostrar_datos(self):
        return 'Código: ' + self.__codigo + '\nNombre: ' + self.__nombre + '\nDNI: ' + self.__dni + '\nDirección: ' + self.__direccion + '\nTeléfono: ' + self.__telefono + '\nEdad: ' + str(self.__edad) + '\nSexo: ' + self.__sexo + '\nFecha de nacimiento: ' + self.__fecha_nacimiento + '\nProcedencia: ' + self.__procedencia + '\nGrado de instrucción: ' + self.__grado_instruccion + '\nEstado civil: ' + self.__estado_civil + '\nOcupación: ' + self.__ocupacion + '\nAcompañante: ' + self.__acompanante + '\nParentesco: ' + self.__parentesco + '\nTeléfono acompañante: ' + self.__telefono_acompanante

class Medico(Persona):

    def __init__(self, codigo, nombre, especialidad):
        super().__init__(nombre)
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especialidad = especialidad

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_especialidad(self):
        return self.__especialidad

    def mostrar_datos(self):
        return self.__codigo + ' | ' + self.__nombre + ' | ' + self.__especialidad


