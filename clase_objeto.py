# Conceptos: Método constructor,Encapsulamiento de atribútos y métodos
import numpy as np

class Coche():
    # Método constructor. En python __init__ es el nétodo constructor que crea el estdo inicial de los objetos que
    # pertenecen a una clase.
    def __init__(self):
        # Encapsulamiento de variables. Se incluye de la forma __varname para hacer que la variable no sea modificable
        # desde fuera de la clase
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__enmarcha = False


    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return 'El coche está en marcha'
        elif (self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no es posible arrancar"
        else:
            return 'El coche está parado'


    def __chequeo_interno(self):
        # Encapsulamiento de métodos. Se incluye de la forma __method para hacer que el método solo sea accesible desde
        # dentro de la clase. se utiliza principalmente para chequeos internos.
        print('Realizando el chequeo interno')

        self.gasolina = np.random.rand(1)
        self.aceite = np.random.rand(1)
        self.puertas = np.random.rand(1)

        if(self.gasolina<=0.95 and self.aceite<=0.98 and self.puertas<=0.8):
            return True
        else:
            return False


    def estado(self):
        print('El coche tiene ', self.__ruedas, ' ruedas.\n',
              'Un ancho de ', self.__ancho,'\n',
              'Un largo de ',self.__largo,'\n',
              'Gasolina: ',self.gasolina,' Aceite: ',self.aceite, ' Puertas: ', self.puertas)



# Objeto 1:
print('-----------------------------------------------  Coche 1  -----------------------------------------------------')
coche1 = Coche()
print(coche1.arrancar(True))
coche1.estado()

#Objeto 2:
print('------------------------------------------------  Coche 2  ----------------------------------------------------')
coche2 = Coche()
print(coche2.arrancar(True))
coche2.__ancho = 80
coche2.estado()

