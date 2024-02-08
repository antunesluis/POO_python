class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None 
        self._fabricante

    @property 
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor 

    @property 
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor 

    def mostra_carro(self): 
        print(self.nome, self.motor, self.fabricante)

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkwagen = Fabricante('Volkswagen')
motor_2_0 = Motor('2.0')

# teste 

fusca.fabricante = volkwagen
fusca.motor = motor_2_0 

