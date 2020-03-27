# Los errores son clases de error por tanto para crear una excepción propia habria que crear una clase que lance ese
# error personalizado.
def evaluaedad(edad):
    if edad<0:
        raise TypeError('No se permiten edades negativas')

    if edad<20:
        return 'Eres muy joven'
    elif edad<40:
        return 'Eres joven'
    elif edad<65:
        return 'Eres maduro'
    elif edad>100:
        return 'Eres mayor'

print(evaluaedad(-15))


