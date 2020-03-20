# Conceptos: super(), isinstance()
class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print('Nombre: ',self.nombre, ' Edad: ', self.edad, ' Residencia: ', self.residencia)


class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        # super(). La instrucción llama a un método de la clase padre, en este caso al método __init__ de la superclase
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print('Salario: ',self.salario, ' Antiguedad: ', self.antiguedad)

print('-----------------------------------------------  Antonio  -----------------------------------------------------')
antonio = Persona('Antonio',55,'España')
antonio.descripcion()

print('-----------------------------------------------  Manuel  ------------------------------------------------------')
manuel = Empleado(1500,15,'Manuel',50,'Colombia')
manuel.descripcion()
# Principio de sustitución: 'es siempre un/una'. Un objeto de la subclase será siempre un objeto de la superclase
print(isinstance(manuel,Empleado))
print(isinstance(manuel,Persona))
print(isinstance(antonio,Empleado))
print(isinstance(antonio,Persona))
