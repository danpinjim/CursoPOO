# Concepto: Uso de los paquetes de python. Como llamarlos.
from calculos_paquete.calculos_generales import dividir,redondear
from calculos_paquete.basicos.operaciones_basicas import multiplicar
from calculos_paquete.redondeo_potencia.operaciones_complejas import potencia

# Paquetes Python. Se generan con el archivo __init__.py. Automaticamente python lo entenderá como paquete esa carpeta.
# Se pueden crear paquetes dentro de paquetes de la misma forma

dividir(5,2)
redondear(5.6)

multiplicar(5,5)
potencia(4,6)