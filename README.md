# agenda

Proyecto de ejemplo para la asignatura Paradigmas de la Programación

## Objetivo

Este pequeño y sencillo proyecto tiene como único objetivo el servir como referencia de implementación de buenas prácticas de programación en Python, que contribuyan al desarrollo de código limpio: compacto, modular, fácil de leer, expresivo, reutilizable y extensible.

## Fundamentos

- Principios SOLID de diseño orientado a objetos
- Patrón de diseño MVC (Modelo/Vista/Controlador)
- Propuestas de mejora contenidas en los documentos:
  - PEP 8 (Guía de Estilo para Código Python)
  - PEP 257 (Convenciones para Cadenas de Documentación)

## Características

El proyecto **agenda** implementa una sencilla agenda telefónica.

Los datos de la agenda se guardan en registros que contienen sólo dos datos (nombre y teléfono) donde el primero es utilizado como clave de acceso.

La aplicación funciona en modo consola, y la interfaz de usuario consiste en la típica consola interactiva de línea de comandos, técnicamente conocida como REPL (*Read Eval Print Loop*: ciclo de lectura, evaluación e impresión).

La información de contacto se almacena en un único archivo en formato **shelve**, una especie de diccionario persistente que permite serializar objetos mediante **pickle** y almacenarlos en formato **dbm**. Cada registro en este formato consiste en una clave que representa a una cadena de caracteres.

## Módulos

- **main.py**: es el módulo principal, es el programa que arranca y maneja la aplicación, por eso cumple la función de *controlador*. Importa los demás módulos, instancia sus clases, es decir, depende completamente de ellos.
- **agenda.py**: es el módulo que contiene la estructura de clases en la que se basa la información que va a manejar la aplicación, por eso cumple la función de *modelo*. Es completamente independiente de los demás módulos.
- **repl.py**: es el módulo encargado de la interacción con el usuario, es decir los "inputs" y "prints", por eso cumple la función de *vista*. Es también completamente independiente de los demás módulos.
- **estante.py**: es un módulo independiente que sirve de apoyo al controlador, es el encargado de proporcionar a la aplicación la funcionalidad de persistencia de datos. Sólo importa lo que necesita, es decir, el módulo *shelve*.

## Ventajas

Las ventajas de un buen diseño en el desarrollo de aplicaciones son más que evidentes, sobre todo en proyectos grandes, que involucran a varios programadores.

Para extender la funcionalidad de esta aplicación de ejemplo, sólo se necesitaría modificar el módulo adecuado. Por ejemplo, para poder guardar más información de contacto, bastaría con extender la clase *Agenda* (modelo) del módulo **agenda.py** y modificar algunos métodos de la clase *Main* en el módulo **main.py** (controlador). Los demás módulos permanecerían intactos.

De igual manera, se podría modificar el módulo de vista (**repl.py**) o el de persistencia (**estante.py**) sin que esto afecte en lo más mínimo a los demás módulos.
