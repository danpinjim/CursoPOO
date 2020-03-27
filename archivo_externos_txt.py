# Conceptos: Manipulacion basica de txt, punteros (seek)

from io import open
# Fases de Manipulación: Creacion > Apertura > Manipulación > Cierre

# Open crea el archivo de texto si no esta creado y lo abre si existia previamente
archivo_txt = open('archivo.txt','w')
frase = 'Estupendo dia para estudiar Python \nel sabado'
archivo_txt.write(frase)
# Close. Se refiere a cerrar el archivo que habiamos abierto en memoria en nuestro codigo de python
archivo_txt.close()

archivo_txt = open('archivo.txt','r')
texto = archivo_txt.read()
archivo_txt.close()
print(texto)

archivo_txt = open('archivo.txt','r')
lineas_txt = archivo_txt.readlines()
archivo_txt.close()
print(lineas_txt)

archivo_txt = open('archivo.txt','a')
archivo_txt.write('\nsiempre es una buena ocasion para estudiar python')
archivo_txt.close()

# PUNTERO en .txt
print('************************************************* PUNTERO *****************************************************')
archivo_txt = open('archivo.txt','r')
print(archivo_txt.read())
print('-----------')
archivo_txt.seek(6)
print(archivo_txt.read())
print('-----------')
archivo_txt.seek(0)
print(archivo_txt.read(11))
print(archivo_txt.read())
print('-----------')
archivo_txt.seek(0)
archivo_txt.seek(len(archivo_txt.read())/2)
print(archivo_txt.read())
print('-----------')
archivo_txt.seek(0)
archivo_txt.seek(len(archivo_txt.readline()))
print(archivo_txt.read())
print('-----------')
archivo_txt = open('archivo.txt','r+') # lectura y escritura
archivo_txt.write('Comienzo del texto, ')
print('-----------')
archivo_txt = open('archivo.txt','r+')
lista_texto = archivo_txt.readlines()
lista_texto[1] = ' Esta linea ha sido incluida desde el exterior \n'
archivo_txt.seek(0)
archivo_txt.writelines(lista_texto)
archivo_txt.close()