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
            return 'El coche está en marcha'
        else:
            return 'El coche está parado'

    def estado(self):
        print('El coche tiene ', self.__ruedas, ' ruedas.\n',
              'Un ancho de ', self.__ancho,'\n',
              'Un largo de ',self.__largo)



# Objeto 1:
print('-----------------------------------------------  Coche 1  -----------------------------------------------------')
coche1 = Coche()
print(coche1.arrancar(True))
coche1.estado()

#Objeto 2:
print('------------------------------------------------  Coche 2  ----------------------------------------------------')
coche2 = Coche()
print(coche2.arrancar(False))
coche2.__ancho = 80
coche2.estado()

