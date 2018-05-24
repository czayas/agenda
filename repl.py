#!/usr/bin/env python3
"""
Módulo REPL: Interfaz de usuario en modo consola (vista).

Proyecto de ejemplo - Paradigmas de la Programación
"""
import sys
from traceback import format_exc
from collections import Iterable
try:
    # El módulo readline agrega autocompletado e historial a input().
    from readline import set_completer
    from readline import parse_and_bind
except ImportError:
    # El módulo readline no está disponible en Windows.
    pass


def strip(cadena):
    """Retorna una cadena sin espacios a los lados en cada línea."""
    return "\n".join(linea.strip()
                     for linea in cadena.split("\n") if linea).strip()


def esiterable(objeto):
    """Retorna True si el objeto es un iterador pero no es una cadena."""
    return isinstance(objeto, Iterable) and not isinstance(objeto, str)


def iterable(objeto):
    """Retorna un iterador del objeto (una cadena no debe ser iterable)."""
    return iter([objeto]) if not esiterable(objeto) else objeto


class Completador:
    """Completador para el módulo readline."""

    def __init__(self, opciones):
        """Autocompletado con tabulación."""
        self.opciones = sorted(opciones)
        self.o = self.opciones[:]  # Copia de self.opciones

    def completar(self, texto, estado):
        """Event handler para completer de readline."""
        if estado == 0:
            if texto:
                self.o = [o for o in self.opciones
                          if o and o.startswith(texto)]
            else:
                self.o = self.opciones[:]
        return None if estado >= len(self.o) else self.o[estado] + " "


class REPL:
    """Ciclo de Lectura, Evaluación e Impresión (Read, Eval, Print, Loop)."""

    def __init__(self, comandos, introduccion="¡Bienvenido!", indicador="> "):
        """
        Constructor: Inicializa propiedades de instancia y completador.

        comandos     -- Diccionario de funciones a ejecutar (dict)
        introduccion -- Texto introductorio (str)
        indicador    -- Inductor o 'prompt' (str)
        """
        self.comandos = comandos
        self.introduccion = introduccion
        self.indicador = indicador
        try:
            # Asignación de método de autocompletado para el módulo readline.
            set_completer(Completador(comandos.keys()).completar)
            parse_and_bind('tab:complete')
        except NameError:
            # El módulo readline no está disponible en Windows.
            pass

    def ciclo(self):
        """Ejecuta el ciclo REPL."""
        print(self.introduccion)
        while True:
            try:
                comando, *parametros = input(self.indicador).split()
                salida = self.comandos[comando](*parametros)
                if salida:
                    for linea in iterable(salida):
                        print(linea)
            except ValueError:
                pass
            except (KeyboardInterrupt, EOFError):
                sys.exit(0)
            except KeyError:
                print("{}: Comando desconocido.".format(comando))
            except TypeError:
                print(strip(self.comandos[comando].__doc__))
            except Exception as excepcion:
                print("Error inesperado:\n", type(excepcion), excepcion, "\n",
                      format_exc().strip())


def main():
    """Función principal (ejemplo de uso)."""
    def hola():
        return "Hola, Mundo."

    comandos = {"eval": eval,
                "hola": hola,
                "quit": quit}

    REPL(comandos).ciclo()


if __name__ == "__main__":
    main()
