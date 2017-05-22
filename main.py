#!/usr/bin/env python3
"""
Módulo Main: Programa principal (controlador).

Proyecto de ejemplo - Paradigmas de la Programación
Agenda telefónica - Ejecute "ayuda" para más información
"""
from agenda import Agenda
from estante import Estante
from repl import REPL
from repl import strip


class Main:
    """Clase principal."""

    def __init__(self):
        """Constructor: Inicializa propiedades de instancia y ciclo REPL."""
        self.comandos = {
            "agregar": self.agregar,
            "borrar": self.borrar,
            "mostrar": self.mostrar,
            "listar": self.listar,
            "buscar": self.buscar,
            "ayuda": self.ayuda,
            "salir": self.salir
        }
        archivo = "agenda.db"
        introduccion = strip(__doc__)
        self.agenda = Estante(archivo)
        if not self.agenda.esarchivo():
            introduccion += '\nError: No se pudo abrir "{}"'.format(archivo)
        REPL(self.comandos, introduccion).ciclo()

    def agregar(self, nombre, telefono):
        """
        Agrega un registro a la agenda.

        nombre   -- Nombre del contacto. Se usará como clave.
        telefono -- Teléfono del contacto.
        """
        self.agenda[nombre] = Agenda(nombre, telefono)

    def borrar(self, nombre):
        """
        Borra un registro de la agenda.

        nombre -- Nombre del contacto que se desea borrar de la agenda.
        """
        del self.agenda[nombre]

    def mostrar(self, nombre):
        """
        Retorna un registro de la agenda.

        nombre -- Nombre del contacto que se desea mostrar.
        """
        return self.agenda[nombre]

    def listar(self):
        """
        Retorna un generador con todos los registros de la agenda.

        Este comando no requiere de parámetros.
        """
        return (self.agenda[nombre]
                for nombre in sorted(self.agenda))

    def buscar(self, cadena):
        """
        Retorna un generador con los registros que contienen una cadena.

        cadena -- Nombre o parte del nombre que se desea buscar en la agenda.
        """
        return (self.agenda[nombre]
                for nombre in sorted(self.agenda)
                if cadena in nombre)

    def ayuda(self, comando="zzz"):
        """
        Retorna la lista de comandos disponibles.

        comando -- Comando del que se desea obtener ayuda (opcional).
        """
        if comando in self.comandos:
            salida = strip(self.comandos[comando].__doc__)
        else:
            salida = "Sintaxis: comando [parámetro1] [parámetro2] [..]\n" + \
                     "Comandos: " + \
                     ", ".join(sorted(self.comandos.keys()))
        return salida

    def salir(self):
        """
        Sale de la aplicación.

        Este comando no requiere de parámetros.
        """
        quit()


if __name__ == "__main__":
    Main()
