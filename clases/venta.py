from datetime import datetime

class Venta:
    def __init__(self, cliente, lista_de_productos):
        self.cliente = cliente
        self.lista_de_productos = lista_de_productos
        self.fecha = datetime.now()
        self.total = self.calcular_total()     # Un método interno a definir debajo

    def calcular_total(self):
        return sum(producto.precio for producto in self.lista_de_productos)  #  Notable
    
    def registrar_venta(self):
        self.cliente.registrar_compra(self)
        return f"Venta registrada: {self.mostrar_info()}"      # Método definido debajo
    
    def mostrar_info(self):
        productos = ", ".join([producto.nombre for producto in self.lista_de_productos])

                    # El join retorna un string de "nombres" separados por "," (en este caso)

        return f"Cliente: {self.cliente.nombre}, Productos: {productos}, Total: {self.total}"
    
    
    

