
# las listas son estructuras de datos lineales
# se crean usando breakes ej: my_list = []
# las listas son ordenadas (orden de insercion ), esto quiere decir 
# que el ultimo dato ingresado ocupara la ultima posicion
# emplea metodos para manipular los items de la misma 
# oo los array la primera posicion inicia en 0
#  permite items duplicados
# las listas son mutables, es decir podemos agregar, actualizar o remover items 
# pude contenerdistintos tipos de datos

nombres = [ "Cristian", "Pepito", "Natalia", "Luisa"]

print(len(nombres))
print(type(nombres))

listaDatos = ["Pepito", "Perez", 1000100100,1.80,True]

print(f"El numero de Documento es : {listaDatos[2]}")

print(listaDatos[1:4])

print(listaDatos[:-1])
