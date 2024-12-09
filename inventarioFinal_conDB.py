import sqlite3
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

def conectar_db():
    return sqlite3.connect("productos.db")

def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            Producto TEXT NOT NULL UNIQUE,
            Cantidad INTEGER NOT NULL,
            Precio REAL NOT NULL,
            Marca TEXT NOT NULL,
            Peso_Litros REAL NOT NULL,
            Unidad TEXT NOT NULL,
            FechaCreacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conexion.commit()
    conexion.close()

# Funcion que pregunta que tipo de unidad tiene el producto, solo usada en Registrar Producto
def solicitar_unidad():
    while True:
        tipo = input("¿El producto es líquido o sólido? (L/S): ").strip().upper()
        if tipo == "L":
            return "Lt"
        elif tipo == "S":
            return "Kg"
        else:
            print("Entrada inválida. Por favor, ingrese 'L' para líquido o 'S' para sólido.")

# Funcion para volver al menu
def volver_menu():
    conexion = conectar_db()
    conexion.close()
    
    print("\nVolviendo al Menu Principal ...")
    return

# Funcion para registrar productos
def registrar_producto():
    back = int(input("Para volver ingrese 0(cero), 1(uno) para continuar: ")) # Para volver al menu por si hubo un error al seleccionar la opcion
    if back == 0:
        volver_menu()
        return
    elif back == 1:
        print("Continuando con la operación...\n")
    
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    try:
        prod = input("Nombre del producto: ")
        cant = int(input("Cantidad: "))
        price = float(input("Precio/unidad en pesos ARS: "))
        brand = input("Marca del producto: ")
        peso_litros = float(input("Peso o Litros por unidad: "))
        unidad = solicitar_unidad()
        
        cursor.execute(
            "INSERT INTO productos (Producto, Cantidad, Precio, Marca, Peso_Litros, Unidad) VALUES (?, ?, ?, ?, ?, ?)",
            (prod, cant, price, brand, peso_litros, unidad)
        )
        conexion.commit()
        print("\nProducto registrado exitosamente.")
    except sqlite3.IntegrityError:
        print("\nError: El nombre del producto ya existe. Intente con otro nombre.")
    finally:
        conexion.close()

# Funcion para consultar producto
def consultar_producto():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cod = int(input("\nIngrese el código del producto a consultar [0 para volver]: "))
    if cod == 0:
        print("\nProducto no encontrado.")
        volver_menu()
        
    cursor.execute("SELECT * FROM productos WHERE Codigo = ?", (cod,))
    producto = cursor.fetchone()
    if producto:
        print(f"""
            Producto encontrado:
                Código     : {producto[0]}
                Nombre     : {producto[1]}
                Cantidad   : {producto[2]}
                Precio     : ${producto[3]:.2f}
                Marca      : {producto[4]}
                Peso/Litros: {producto[5]} {producto[6]}
                Fecha      : {producto[7]}
        """)
    conexion.close()

# Funcion para actualizar o modificar un producto
def actualizar_producto():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cod = int(input("\nIngrese el código del producto a actualizar [0 para volver]: "))
    if cod == 0:
        print("\nProducto no encontrado.")
        volver_menu()
        
    cursor.execute("SELECT * FROM productos WHERE Codigo = ?", (cod,))
    producto = cursor.fetchone()
    
    if producto:
        print(f"\nProducto actual: {producto}")
        prod = input("Nuevo nombre del producto: ")
        cant = int(input("Nueva cantidad: "))
        price = float(input("Nuevo precio/unidad en pesos ARS: "))
        brand = input("Nueva marca: ")
        peso_litros = float(input("Nuevo peso/litros por unidad: "))
        unidad = solicitar_unidad()
        cursor.execute(
            "UPDATE productos SET Producto = ?, Cantidad = ?, Precio = ?, Marca = ?, Peso_Litros = ?, Unidad = ? WHERE Codigo = ?",
            (prod, cant, price, brand, peso_litros, unidad, cod)
        )
        conexion.commit()
        print("\nProducto actualizado exitosamente.")
    conexion.close()

# Funcion para eliminar un registro de un producto
def eliminar_producto():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cod = int(input("\nIngrese el código del producto a eliminar [0 para volver]: "))
    if cod == 0:
        print("\nProducto no encontrado.")
        volver_menu()
    cursor.execute("SELECT * FROM productos WHERE Codigo = ?", (cod,))
    producto = cursor.fetchone()
    if producto:
        cursor.execute("DELETE FROM productos WHERE Codigo = ?", (cod,))
        conexion.commit()
        print(f"\nProducto '{producto[1]}' eliminado exitosamente.")
    conexion.close()

# Funcion para mostrar todos los productos
def mostrar_productos():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        headers = ["Código", "Nombre", "Cantidad", "Precio (ARS)", "Marca", "Peso/Litros", "Unidad", "Fecha de Creación"]
        print(tabulate(productos, headers=headers, tablefmt="grid"))
    else:
        print("\nNo hay productos registrados.")
    conexion.close()

# Funcion para generar un reporte de bajo stock
def reporte_bajo_stock():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    limite_stock = int(input("\nIngrese el límite para considerar bajo stock: "))
    cursor.execute("SELECT * FROM productos WHERE Cantidad < ?", (limite_stock,))
    productos = cursor.fetchall()
    
    if productos:
        print("\nProductos con bajo stock:")
        headers = ["Código", "Nombre", "Cantidad", "Precio", "Marca", "Peso/Litros", "Unidad"]
        
        # Resaltar las cantidades bajas con color rojo
        productos_con_color = []
        for producto in productos:
            cantidad_coloreada = f"{Fore.RED}{producto[2]}{Style.RESET_ALL}"  # Color rojo para cantidad baja
            productos_con_color.append((producto[0], producto[1], cantidad_coloreada, producto[3], producto[4], producto[5], producto[6]))
        
        print(tabulate(productos_con_color, headers=headers, tablefmt="grid"))
    else:
        print("\nNo hay productos con bajo stock.")
    
    conexion.close()

def mostrar_menu():
    print("\n--- Sistema de Gestión de Productos ---\n")
    print("1. Registrar productos")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listado completo de productos")
    print("6. Reporte de Bajo Stock")
    print("0. Salir\n")
    print("---------------------------------------\n")

crear_tabla()

# Menú principal
opc = -1
while opc != 0:
    mostrar_menu()
    opc = int(input("Seleccione una opción: "))
    if opc == 1:
        registrar_producto()
    elif opc == 2:
        consultar_producto()
    elif opc == 3:
        actualizar_producto()
    elif opc == 4:
        eliminar_producto()
    elif opc == 5:
        mostrar_productos()
    elif opc == 6:
        reporte_bajo_stock()
    elif opc == 0:
        print("\n---------------------------------------\n")
        print("Saliendo del sistema...")
        print("\n---------------------------------------\n")
    else:
        print("\nOpción no válida.")