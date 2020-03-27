# Serialization collections (Pickle): Almacenamos y leemos coleciones de python en archivos bonarios mediante pickle
import pickle
from io import open

list = ['Carlos', 'Sofia', 'Pablo', 'Irene']

bfile = open('binary_file','wb')

pickle.dump(list,bfile)

bfile.close()

del (bfile)

bfile_read = open('binary_file','rb')
list_read = pickle.load(bfile_read)
print(list_read)