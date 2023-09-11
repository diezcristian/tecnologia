import os
import datetime

password="cdiez"
user=1234

password=input("Digite su Usuario")
user=int(input("Digite su Contraseña"))

if password=="cdiez" and user==1234:
    print("Registro Exitoso")
else:
    print("Vuelve a intentar")


# Definir las funciones necesarias
def registrar_usuario(nombre, apellido, correo, tarjeta):
  # Agregar el usuario a la lista de usuarios
  usuarios.append({
    "nombre": nombre,
    "apellido": apellido,
    "correo": correo,
    "tarjeta": tarjeta
  })

def tomar_bicicleta(tarjeta, origen, destino):
  # Buscar al usuario en la lista de usuarios
  usuario = next((u for u in usuarios if u["tarjeta"] == tarjeta), None)

  # Si el usuario no existe, mostrar un error
  if usuario is None:
    print("El usuario no existe vuelve a intertarlo.")
    return

  # Crear un préstamo nuevo
  prestamo = {
    "usuario": usuario["nombre"],
    "tarjeta": tarjeta,
    "origen": origen,
    "destino": destino,
    "fecha_inicio": datetime.datetime.now()
  }

  # Agregar el préstamo a la lista de préstamos
  prestamos.append(prestamo)

def consultar_usuarios():
  # Imprimir la lista de usuarios
  for usuario in usuarios:
    print(f"Nombre: {usuario['nombre']} | Apellido: {usuario['apellido']} | Correo: {usuario['correo']} | Tarjeta: {usuario['tarjeta']}")

def consultar_prestamos():
  # Imprimir la lista de préstamos
  for prestamo in prestamos:
    print(f"Usuario: {prestamo['usuario']} | Tarjeta: {prestamo['tarjeta']} | Origen: {prestamo['origen']} | Destino: {prestamo['destino']} | Fecha de inicio: {prestamo['fecha_inicio']}")

# Definir las variables globales
usuarios = []
prestamos = []

# Inicializar la aplicación
print("Bienvenido al sistema de préstamos de bicicletas Medellin CESDE.")

# Bucle principal
while True:
  # Mostrar el menú de opciones
  print("1. Registrar Usuario")
  print("2. Asignar Bicicleta")
  print("3. Consultar Usuarios")
  print("4. Consultar Préstamos")
  print("5. Exit")

  # Leer la opción del usuario
  opcion = input("Ingrese alguna de las opciónes: ")

  # Procesar la opción del usuario
  if opcion == "1":
    # Registrar un usuario
    nombre = input("Digite Nombre del Usuario: ")
    apellido = input("Digite Apellido del Usuario: ")
    correo = input("Digite Correo del Usuario: ")
    tarjeta = input("Digite el Número de la Tarjeta de Usuario: ")
    registrar_usuario(nombre, apellido,correo, tarjeta)
  elif opcion == "2":
    # Tomar una bicicleta
    tarjeta = input("Digite el Número de Tarjeta del Usuario: ")
    origen = input("Digite el Origen de la Bicicleta: ")
    destino = input("Digite el Destino de la Bicicleta: ")
    tomar_bicicleta(tarjeta, origen, destino)
  elif opcion == "3":
    # Consultar usuarios
    consultar_usuarios()
  elif opcion == "4":
    # Consultar préstamos
    consultar_prestamos()
  elif opcion == "5":
    # Salir de la aplicación
    print("Gracias Por Elegirnos.")
    break

