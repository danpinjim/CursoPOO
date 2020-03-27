# Define la configuración del paquete que va a ser distribuido.
from setuptools import setup

# Hay más argumentos posibles pero son opcionales. Estos argumentos pueden ser author_mail,url
setup(name = 'paquetedistribuiblecalculos',
      version = '1.0',
      description = 'Paquete de redondeo y potencia',
      author = 'Daniel',
      packages = ['calculos_paquete','calculos_paquete.redondeo_potencia'])
      
# Una vez terminado este archivo de setup se lanza desde el cmd ubicado en la carpeta y poner el siguiente comando:
# python setup.py sdist

# Para la instalacion nos vamos con el cmd a la carpeta dist y el comando:
# pip install paquetedistribuiblecalculos-1.0.tar.gz (pa+tab lo pone automaticamente)

# De esta forma ya tendremos accesible dicho paquete desde donde sea (no con el name del setup si no con el de las carpetas

# Para desisnstalar hay que llamarlo por el nombre del paquete:
#pip uninstall <package name>