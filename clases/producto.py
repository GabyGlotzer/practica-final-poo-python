class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_cantidad(self, cantidad):  # seter
        self.cantidad = cantidad

    def mostrar_detalles(self):
        return f"Producto: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}"
