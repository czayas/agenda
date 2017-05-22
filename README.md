# agenda

Proyecto de ejemplo para la asignatura Paradigmas de la Programación

## Objetivo

Este pequeño y sencillo proyecto tiene como único objetivo el servir como referencia de implementación de buenas prácticas de programación en Python, que contribuyan al desarrollo de código limpio: compacto, modular, fácil de leer, expresivo, reutilizable y extensible.

## Fundamentos

Se han tomado en cuenta los principios SOLID de diseño orientado a objetos, el patrón de diseño MVC (Modelo/Vista/Controlador) y las propuestas de mejora contenidas en los documentos PEP 8 (Guía de Estilo para Código Python) y PEP 257 (Convenciones para Cadenas de Documentación).

## Características

El proyecto **agenda** implementa una sencilla agenda telefónica.

Los datos de la agenda se guardan en registros que contienen sólo dos datos (nombre y teléfono) donde el primero es utilizado como clave de acceso.

La aplicación funciona en modo consola, y la interfaz de usuario consiste en la típica consola interactiva de línea de comandos, técnicamente conocida como REPL (*Read Eval Print Loop*: ciclo de lectura, evaluación e impresión).

La información de contacto se almacena en un único archivo en formato **shelve**, una especie de diccionario persistente que permite serializar objetos mediante **pickle** y almacenarlos en formato **dbm**. Cada registro en este formato consiste en una clave que representa a una cadena de caracteres.
