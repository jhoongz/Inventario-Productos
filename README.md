<h1 align="center">Sistema de Gestión de Productos</h1>

Este es el **Proyecto Final de Programación con Python** para Talento Tech. Se trata de un programa desarrollado en Python que permite gestionar un inventario de productos almacenados en una base de datos SQLite. El sistema incluye funcionalidades como registrar, consultar, actualizar, eliminar productos, generar reportes de bajo stock, y listar el inventario completo.

## Funcionalidades

- **Registrar productos:** Permite añadir un producto con detalles como nombre, cantidad, precio, marca, peso/litros y unidad (Kg/Lt).
- **Consultar producto:** Busca un producto específico por su código único.
- **Actualizar producto:** Modifica los datos de un producto existente.
- **Eliminar producto:** Elimina un producto del inventario.
- **Listado completo:** Muestra todos los productos registrados en la base de datos.
- **Reporte de bajo stock:** Genera un informe de los productos cuya cantidad está por debajo de un límite definido.
- **Volver al menú:** En todas las opciones (excepto registrar unidad), el usuario puede volver al menú principal ingresando `0`.

## Tecnologías y Librerías

El programa utiliza las siguientes tecnologías y librerías:

- **[Python](https://www.python.org/):** Lenguaje de programación principal.
- **[SQLite3](https://docs.python.org/3/library/sqlite3.html):** Base de datos integrada para almacenar información de los productos.
- **[Colorama](https://pypi.org/project/colorama/):** Permite agregar colores y estilos en la consola para mejorar la experiencia del usuario.
- **[Tabulate](https://pypi.org/project/tabulate/):** Facilita la representación de datos en formato tabular en la consola.

## Requisitos Previos

Antes de ejecutar el programa, asegúrate de cumplir con los siguientes requisitos:

1. Tener instalado Python 3. 
2. Instalar las librerías necesarias ejecutando:
    ```bash
    pip install colorama tabulate
    ```

## Estructura de la Base de Datos

La base de datos contiene una tabla llamada productos con los siguientes campos:

- **Codigo:** Identificador único autoincremental.
- **Producto:** Nombre del producto (único).
- **Cantidad:** Cantidad disponible en inventario.
- **Precio:** Precio unitario (en pesos argentinos).
- **Marca:** Marca del producto.
- **Peso_Litros:** Peso o volumen por unidad (Kg o Lt).
- **Unidad:** Unidad de medida (Kg para sólidos, Lt para líquidos).
- **FechaCreacion:** Fecha y hora en la que se creó el producto.

## Cómo Usar el Programa

1. **Ejecuta el programa:**

    ```bash
    python InventarioFinal_conDB.py
    ```

2. **Selecciona una opción del menú:**

El menú principal ofrece opciones numeradas para realizar diferentes acciones.
Puedes volver al menú principal ingresando 0 en cualquier momento.

## Ejemplo de Uso

1. **Registrar un producto:**
    - Ingrese el nombre, cantidad, precio, marca, peso/litros y si el producto es líquido o sólido.

2. **Consultar producto:**
    - Ingrese el código del producto que desea consultar.

3. **Reporte de bajo stock:**
    - Ingrese el límite de cantidad para identificar productos con bajo inventario.
    - Las cantidades bajas se resaltarán en rojo (gracias a Colorama).

## Autor
- **Nombre:** Jonathan Antonio Gomez
- **Curso:** Talento Tech - Programación con Python

**Este proyecto fue creado como un ejercicio práctico para demostrar habilidades en Python, manejo de bases de datos y librerías complementarias. Si deseas realizar mejoras, no dudes en contactarme o realizar un pull request en el repositorio de GitHub.**
