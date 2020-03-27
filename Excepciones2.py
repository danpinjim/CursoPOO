# Concepto: Modulo try-exception para varios tipos de error, clausula finally
def divide():
    # Este bloque es suceptible de error. ValueError,ZeroDivisionError...
    try:
        op1 = (float(input('Introduce el primer numero: ')))
        op2 = (float(input('Introduce el segundo numero: ')))

        print('La division es: ' + str(op1/op2))
    except ValueError:
        print('El valor introducido es erroneo')
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
    finally: # Lo que se incluye aquí dentro se ejecuta si o si. Especialmente util en conexiones con BBDD para asegurar
    # que ocurra lo que ocurra se cierre la conexión con la base de datos.
    print('Esto se ejecuta si o si')

    # Hay otra posibilidad de generalizar el tipo de error aunque es poco recomendable por que no es capaz de saber
    # que ha pasado el usuario. Para ello simplemente se incluye el excep:

    print('Calculo finalizado')

divide()