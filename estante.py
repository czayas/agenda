#!/usr/bin/env python3
"""
Módulo Estante: Envoltorio de Shelve (persistencia de datos).

Proyecto de ejemplo - Paradigmas de la Programación
"""
import shelve


class Estante:
    """Envoltorio de Shelve."""

    def __init__(self, archivo='estante.db', wb=False):
        """
        Constructor: Abre el archivo shelve (lo crea si no existe).

        archivo -- Nombre del archivo shelve (str)
        wb      -- Reescritura automática de registros accedidos (bool)
        """
        self.dic = shelve.open(archivo, writeback=wb)

    def __repr__(self):
        """Retorna la representación de la clase (archivo shelve)."""
        return repr(self.dic)

    def __getitem__(self, clave):
        """Retorna el elemento asignado a la clave (None si no existe)."""
        return self.dic.get(clave, None)

    def __setitem__(self, clave, valor):
        """Asigna un valor a una clave en el archivo shelve."""
        self.dic[clave] = valor

    def __delitem__(self, clave):
        """Borra un registro del archivo shelve."""
        del self.dic[clave]

    def __iter__(self):
        """Retorna un iterador en base a las claves del archivo shelve."""
        return iter(self.dic.keys())

    def __contains__(self, clave):
        """Retorna True si existe una clave en el archivo shelve."""
        try:
            return clave in self.dic
        except TypeError:
            return False

    def __del__(self):
        """Destructor: Cierra el archivo shelve."""
        self.dic.close()


def main():
    """Función principal (ejemplo de uso)."""
    estante = Estante(wb=True)

    estante['123'] = ['Un', 'Dos', 'Tres']
    estante['456'] = ['Cuatro', 'Cinco', 'Seis']
    estante['456'].append('Siete')  # Esto no se guarda si wb=False

    for clave in estante:
        print(clave, estante[clave])


if __name__ == '__main__':
    main()
