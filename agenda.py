#!/usr/bin/env python3
"""
Módulo agenda: Clase principal (modelo).

Proyecto de ejemplo - Paradigmas de la Programación
Autor: Carlos Zayas (czayas en gmail)
"""


class Contacto:
    """Contacto de agenda telefónica."""

    def __init__(self, nombre, telefono):
        """Constructor: Inicializa propiedades de instancia."""
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        """Cadena de representación."""
        return "{}: {}".format(self.nombre, self.telefono)


def main():
    """Función principal (ejemplo de uso)."""
    agenda = {}

    agenda["carlos"] = Contacto("Carlos", "222-333")
    agenda["sergio"] = Contacto("Sergio", "444-555")
    agenda["estela"] = Contacto("Estela", "666-777")

    for clave in agenda:
        print(agenda[clave])


if __name__ == "__main__":
    main()
