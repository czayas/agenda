#!/usr/bin/env python3
"""
Módulo Main: Programa principal (controlador).

Proyecto de ejemplo - Paradigmas de la Programación
"""
from agenda import Agenda
from estante import Estante
from repl import REPL


class Main:
    """Clase principal."""

    def __init__(self):
        """Constructor: Inicializa propiedades de instancia y ciclo REPL."""
        self.agenda = Estante("agenda.db")
        self.comandos = {
            "agregar": self.agregar,
            "borrar": self.borrar,
            "mostrar": self.mostrar,
            "listar": self.listar,
            "buscar": self.buscar,
            "ayuda": self.ayuda,
            "salir": quit
        }
        REPL(self.comandos).ciclo()

    def agregar(self, nombre, telefono):
        """Agrega un registro a la agenda."""
        self.agenda[nombre] = Agenda(nombre, telefono)

    def borrar(self, nombre):
        """Borra un registro de la agenda."""
        del self.agenda[nombre]

    def mostrar(self, nombre):
        """Retorna un registro de la agenda."""
        return self.agenda[nombre]

    def listar(self):
        """Retorna un generador con todos los registros de la agenda."""
        return (self.agenda[nombre]
                for nombre in self.agenda)

    def buscar(self, cadena):
        """Retorna un generador con los registros que contienen una cadena."""
        return (self.agenda[nombre]
                for nombre in self.agenda
                if cadena in nombre)

    def ayuda(self):
        """Retorna la lista de comandos disponibles."""
        return self.comandos.keys()


if __name__ == "__main__":
    Main()
