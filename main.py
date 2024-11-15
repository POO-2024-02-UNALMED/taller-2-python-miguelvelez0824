class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if color == "rojo" or color == "amarillo" or color == "verde" or color == "negro" or color == "blanco":
            self.color = color

class Auto:
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, Asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = Asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        numasientos = 0
        for i in self.asientos:
            if i is not None:
                numasientos +=1
        return numasientos
    
    def verificarIntegridad(self):
        if(self.registro == self.motor.registro):
            for i in self.asientos:
                if i is not None:
                    if self.registro != i.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"
        

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo (self, tipo):
        if tipo == "gasolina" or tipo == "electrico":
            self.tipo = tipo