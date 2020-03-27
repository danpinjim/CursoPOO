# Conceptos: Modulo try-exception para una única excepción
def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def divide(num1,num2):
    # Modulo try-except. Solución para el error resultado de dividir entre cero. en este caso al llamar a la función
    # vendra aqui ejecutara el codigo pero en caso de no ser correcto devolverá un strin en vez de un valor que seria
    # lo esperado
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        return 'Operacion erronea'
def multiplica(num1,num2):
    return num1*num2

# Modulo try-except. En el caso de necesitar un input de un determinado tipo de variable puede ser una solución el
# bucle while junto con el break en caso de tener inouts correctos.
while True:
    try:
        op1 = (int(input('Introduce el primer número: ')))
        op2 = (int(input('Introduce el primer número: ')))
        break
    except ValueError:
        print('Los inputs no son correctos. Intentalo de nuevo')

operacion = input('Introduce la operacion a realizar (suma,resta,divide,multiplica): ')

if operacion == 'suma':
    print(suma(op1,op2))
elif operacion == 'resta':
    print(resta(op1,op2))
elif operacion == 'divide':
    print(divide(op1,op2))
elif operacion == 'multiplica':
    print(multiplica(op1,op2))
else:
    print('Operacion no especificada')

print('Operacion ejecutada. El programa continua')