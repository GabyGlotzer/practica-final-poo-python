class Mascota:
    def __init__(self, nombre, edad, salud, precio):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio

    def actualizar_mascota(self, edad=None, salud=None, precio=None):
        if edad:
            self.edad = edad
        if salud:
            self.salud = edad
        if precio:
            self.precio = precio

    def mostrar_mascota(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"
    
    
class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.energia = energia

    def mostrar_detalles(self):
        return f"Raza: {self.raza}, Nivel de Energía: {self.energia}"
        
    
class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.independencia = independencia

    def mostrar_detalles(self):
        return f"Raza: {self.raza}, Independencia: {self.independencia}"
        

class Tortuga(Mascota):
    def __init__(self, nombre, edad, salud, precio, tamanio, caparazon):
        super().__init__(nombre, edad, salud, precio)
        self.tamanio = tamanio
        self.caparazon = caparazon

    def mostrar_detalles(self):
        return f"Tamaño: {self.tamanio}, Caparazón: {self.caparazon}"
        