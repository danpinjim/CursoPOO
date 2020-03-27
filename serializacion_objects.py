# Serialización de objetos: Hay que tener en cuenta que al cargar el fichero binario, si se trata de un objeto es
# importante definir en ese fichero su clase, de lo contrario no será posible leer este objeto
import pickle
from io import open

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


coche1 = Vehiculos('Seat','Leon')
coche2 = Vehiculos('Toyota','Corolla')
coche3 = Vehiculos('Opel','Astra')

list_objects = [coche1,coche2,coche3]

bfile = open('bfile_object','wb')
pickle.dump(list_objects,bfile)
bfile.close()

file_read = open('bfile_object','rb')
list_objects_read = pickle.load(file_read)
file_read.close()
del (file_read)

for c in list_objects_read:
    print(c.estado())


