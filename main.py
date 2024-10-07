# Funciones para la interfaz de consola

from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Gato, Perro, Tortuga
from clases.producto import Producto
from clases.venta import Venta


# Registramos mascota

def registrar_mascota():
    tipo = input("Qué mascota es? (Perro/Gato/Tortuga): ").strip().lower()
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salud = input("Estado de Salud: ")
    precio = float(input("Precio: "))

    if tipo == "perro":
        raza = input("Raza del perro: ")
        energia = input("Energía: ")
        mascota = Perro(nombre, edad, salud, precio, raza, energia)
    elif tipo == "gato":
        raza = input("Raza del gato: ")
        independencia = input("Nivel de independencia: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    elif tipo == "tortuga":
        tamanio = input("Tamaño de la tortuga: ")
        caparazon = input("Tipo de caparazón: ")       
        mascota = Tortuga(nombre, edad, salud, precio, tamanio, caparazon)
    else:
        print("Mascota no reconocida")
        return
    return mascota

# Registramos cliente

def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección del cliente: ")
    telefono = input("Teléfono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

# Registramos producto

def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto

# Registramos ventas para lo cual se necesitan los clientes y el inventario

def registrar_venta(clientes, inventario):
    nombre_cliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)   # El next busca
                                                                                # el primer elemento
                                                                                # del iterable que cumpla
                                                                                # con la condición
    if not cliente:
        print("Cliente inexistente")
        return
    
    productos = []

    while True:
        nombre_producto = input("Producto? (Vacío=Fin): ")
        if not nombre_producto:
            break   # Sale
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
            print("Producto inexistente")

    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print("La venta fue un éxito!")
    else: 
        print("No hay productos para la venta")
    
###########################################
#
# Menú Principal
#
###########################################
        
def mostrar_menu():
    print("\n --- Menú de gestión Patas Felices ---")   # el "\n" deja una línea en blanco 
    print("1. Registrar Mascota")
    print("2. Registrar Cliente")
    print("3. Registrar Producto")
    print("4. Registrar Venta")
    print("5. Mostrar detalles de Mascotas")
    print("6. Mostrar detalles de Clientes")
    print("7. Mostrar detalles de Productos")
    print("8. Generar alerta de inventario")
    print("9. Salir")
        
def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

#
# Bucle para pedir las opciones mediante el menú
#
# 

    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("Mascota registrada con éxito")

        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado con éxito")
                print(cliente.mostrar_detalles())  # Esto debería funcionar

        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_productos(producto)   # No se hace con append, se hace con el método
                                                        # que definimos dentro del objeto "producto"
                print("Producto registrado con éxito")

        elif opcion == "4":
            registrar_venta(clientes, inventario)   # para lo cual ya debe haber clientes e inventario

        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_mascota())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato) or isinstance(mascota, Tortuga):
                    print(mascota.mostrar_detalles())   # Para atrapar el error por si no es alguna de las
                                                        # mascotas usadas

        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_detalles())

        elif opcion == "7":
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_detalles())

        elif opcion == "8":
            stock_minimo = int(input("Ingresar stock mínimo para alerta: "))
            print(inventario.generar_alerta(stock_minimo)) 
            
        elif opcion == "9":
            print("Saliendo del sistema, Gracias por usar Patas Felices APP!!!")
            break

        else:
            print("Opción inválida, intente nuevamente")

    #  Y esto para que este código se ejecute exclusivamente desde acá (main) y no desde
    #  otro lado

if __name__ == "__main__":
    main()





            