# Conceptos: Polimorfismo
class Coche():
    def desplazamiento(self):
        print('Me desplazo utilizando cuatro ruedas')

class Moto():
    def desplazamiento(self):
        print('Me desplazo utilizando dos ruedas')

class Camion():
    def desplazamiento(self):
        print('Me desplazo utilizando seis ruedas')


vehiculo1 = Moto()
vehiculo1.desplazamiento()

vehiculo2 = Coche()
vehiculo2.desplazamiento()

vehiculo3 = Camion()
vehiculo3.desplazamiento()

# Usamos el polimorfismo para prescindir de tandas instancias. Para ello definimos un método general:
print('*****************************************     Polomorfismo  ***************************************************')
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

# Al pasar un objeto
vehiculo4 = Camion()
desplazamientovehiculo(vehiculo4)

vehiculo5 = Coche()
desplazamientovehiculo(vehiculo5)

vehiculo6 = Moto()
desplazamientovehiculo(vehiculo6)