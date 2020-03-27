# Conceptos : Medotos de los objetos STRING: upper(), lower(),capitalize(),count(),find(),isdigit(),isalum(),isalpha(),
# split(), # strip(),rfind()

usuario = input('Nombre ususario: ')

print(usuario.upper())
print(usuario.capitalize())
print(usuario.lower())

edad = input('Introduce la edad:') # Todo lo introducido en python por input es considerado como un string
while (edad.isdigit() == False):
    print('Por favor introduce un valor numérico')
    edad = input('Introduce la edad:')

if (int(edad)<18):
    print('No puede pasar')
else:
    print('Puedes pasar')