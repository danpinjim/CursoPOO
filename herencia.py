# Conceptos: Herencia, Sobreescritura de métodos, Herencia múltiple

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha= True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True
    def estado(self):
        print('Marca: ', self.marca, ' Modelo: ', self.modelo,'\n',
              'En marcha: ', self.enmarcha,'\n',
              'Acelerando: ', self.acelera,'\n',
              'Frenando: ', self.frena,'\n')

# Subclase de la clase padre/ superclase Vehiculo. Hereda todos sus metodos y atributos.
class Moto(Vehiculos):
    hcaballito = ''
    # Método de la subclase. Solo lo puede utilizar la subclase pero no la superclase.
    def caballito(self):
        self.hcaballito = 'Voy haciendo el caballito'
    # Sobrescritura de métodos. En la subclase se puede sobreescribir métodos de la clase padre aunque no es muy común
    # en los lenguajes de programación distintos de python.
    def estado(self):
        print('Marca: ', self.marca, ' Modelo: ', self.modelo, '\n',
              'En marcha: ', self.enmarcha, '\n',
              'Acelerando: ', self.acelera, '\n',
              'Frenando: ', self.frena, '\n',
              self.hcaballito)

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if (self.cargado):
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no esta cargada'

# Clase que no hereda del resto de la clase vehiculos.
class VElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarenergia(self):
        self.cargando = True


# Herencia múltiple. Una clase como BicicletaElectrica puede heredar propiedades y métodos de dos clases diferentes
# como son VElectricos y # Vehiculos. La primera clase de los argumentos tendra preferencia en el caso de que haya
# métodos repetidos como puede ser en este caso el método constructor.
class BicicletaElectrica(VElectricos,Vehiculos):
    pass




# Conceptos: Herencia, Sobreescritura de métodos, Herencia múltiplemoto1 = Moto('Honda','CBR')
moto1 = Moto('Honda','CVR')
moto1.arrancar()
moto1.caballito()
moto1.estado()

print('-----------------------------------------------  Furgo 1  -----------------------------------------------------')
furgo1 = Furgoneta('Renaul','kangoo')
furgo1.arrancar()
print(furgo1.carga(True))
furgo1.estado()

print('---------------------------------------------  BiciElectrica 1  -----------------------------------------------')
miBici = BicicletaElectrica()