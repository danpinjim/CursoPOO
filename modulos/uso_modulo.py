import funciones_matematicas
from funciones_matematicas import sumar
#from funciones_matematicas import *

# El sentido de importar especificamente algunos modulos es una cuestión de optimización. Al importar reservas en
# memoeria todos los modulos y puede que muchos de estos no se utilicen

funciones_matematicas.sumar(7,5)
sumar(9,1)