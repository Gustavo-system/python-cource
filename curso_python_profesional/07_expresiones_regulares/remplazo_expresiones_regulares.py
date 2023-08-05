import re


# remplaza todos los numeros por el segundo paremetro que se le envie en la cadena del tercer parametro
# 1 (a buscar), 2 (valor remplazo) 3 (valor a remplazar)
print(re.sub(r'\d', '-', 'parro123@gmail.com.mx1')) # output = parro---@gmail.com.mx-

# se puede agregar un cuarto parametro que indica cuantos valores quieres remplazar
print(re.sub(r'\d', '-', 'parro123@gmail.com.mx1', 2)) # -> output = parro--3@gmail.com.mx1