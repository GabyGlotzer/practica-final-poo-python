class Inventario:
    def __init__(self):
        self.lista_de_productos = []

    def agregar_productos(self, producto):
        self.lista_de_productos.append(producto)

    def actualizar_inventario(self, producto, cantidad):
        for prod in self.lista_de_productos:
            if prod.nombre == producto.nombre:
                prod.actualizar_cantidad(cantidad)

    def generar_alerta(self, stock_minimo):
        alertas = [
            prod.nombre
            for prod in self.lista_de_productos if prod.cantidad < stock_minimo
        ]
        return (
            f"Productos con bajo stock: {', '.join(alertas)}"
            if alertas
            else "No hay productos por debajo del stock mínimo"
        )
