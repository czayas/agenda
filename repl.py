#!/usr/bin/env python3
"""
Módulo REPL: Interfaz de usuario en modo consola (vista).

Proyecto de ejemplo - Paradigmas de la Programación
"""
from sys import exit
from traceback import format_exc
from collections import Iterable


def esiterable(objeto):
    """Retorna True si el objeto es un iterador pero no es una cadena."""
    return isinstance(objeto, Iterable) and not isinstance(objeto, str)


def iterable(objeto):
    """Retorna un iterador del objeto (una cadena no debe ser iterable)."""
    return iter([objeto]) if not esiterable(objeto) else objeto


class REPL:
    """Ciclo de Lectura, Evaluación e Impresión (Read, Eval, Print, Loop)."""

    def __init__(self, comandos, indicador="> "):
        """
        Constructor: Inicializa propiedades de instancia.

        comandos  -- Diccionario de funciones a ejecutar (dict)
        indicador -- Inductor o 'prompt' (str)
        """
        self.comandos = comandos
        self.indicador = indicador

    def ciclo(self):
        """Ejecuta el ciclo REPL."""
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
                exit(0)
            except KeyError:
                print("{}: Comando desconocido.".format(comando))
            except Exception as excepcion:
                print("Error inesperado:")
                print(type(excepcion), excepcion)
                print(format_exc().strip())


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
