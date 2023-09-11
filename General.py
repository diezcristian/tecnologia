#password="cdiez"
#user=1234|

#password=input("ingrese su contraseña")
#user=int(input("ingrese su usuario"))

#if password=="ceballos" and user==123:
    #print("Has ingresado")
#else:
    #print("Vuelve a intentar")
#EJERCICIO 1: # Precio y cantidad, calcular el subtotal, si el subtotal es mayor de 1 millon
# calcular descuento del 25% de lo contrario el descuento es de 0%.
# Calcular el IVA y el neto a pagar.

#precio=int(input("ingrese el precio del articulo"))
#cantidad=int(input("ingrese la cantidad de articulos"))
#subtotal=precio*cantidad
#iva= float(subtotal*0.19)
#neto_pagar= float(subtotal+iva)
#pagar= float (neto_pagar-(neto_pagar*0.25))
#if subtotal>1000000:
    #print(f"El descuento es de 25% {subtotal*0.25}, el valor del IVA es de ${iva} y el valor a pagar es de ${pagar}")
#else:
    #print(f"el descuento es del 0%, el IVA es de ${iva} por lo tanto debe pagar ${neto_pagar}")

#Realizar un programa que me pida el producto, precio, cantidad y a que categoría pertenece para que imprima
# el subtotal su descuento, iva y precio neto.
#De ser categoría1 y que el producto tenga una cantidad mayor a 10 aplicaría un descuento del 15%
#De ser categoría2 y que el producto tenga una cantidad mayor a 20 aplicaría un descuento del 20%
#De ser categoría3 y que el producto tenga una cantidad mayor a 21 aplicaría un descuento del 30%
#Si no entonces todos los productos independientes de la cantidad y su categoría tendrán el 5% de descuento.

#categoria_1=0.15
#categoria_2=0.20
#categoria_3=0.30

#producto=input("ingrese el nombre del producto elegido")
#precio=int(input("ingrese el valor del producto"))
#cantidad=int(input("ingrese la cantidad de productos a llevar"))
#categoria=input("ingrese la clase de categoria: categoria1,categoria2,categoria3")
#subtotal=precio*cantidad
#iva= float(subtotal*0.19)
#neto_pagar= float(subtotal+iva)

#if cantidad>10 and categoria=="categoria1":
    #print(f"Para este caso aplica la categoria 1 con un descuento del 15% {subtotal*categoria_1}, por lo tanto el subtotal es "
          #f"{subtotal} el iva es de {iva} y el precio neto a pagar es de {((subtotal+iva)-(subtotal*categoria_1))}")
#elif cantidad>20 and categoria=="categoria2":
    #print(f"Para este caso aplica la categoria 2 con un descuento del 20%{subtotal*categoria_2}, por lo tanto el subtotal es "
          #f"{subtotal} el iva es de {iva} y el precio neto a pagar es de {((subtotal+iva)-(subtotal*categoria_2))}")
#elif cantidad>21 and categoria=="categoria3":
    #print(f"Para este caso aplica la categoria 3 con un descuento del 30% {subtotal*categoria_3}, por lo tanto el subtotal es "
          #f"{subtotal} el iva es de {iva} y el precio neto a pagar es de {((subtotal+iva)-(subtotal*categoria_3))}")
#else:
    #print(f"Para este caso todos los productos independientes de la cantidad y su categoría tendrán el 5% de descuento ,"
          #f" por lo tanto el subtotal es {subtotal} el iva es de {iva} y el precio neto a pagar es de {neto_pagar}")

import random


#vidas=5
#puntos=0

#Si sale cero pierde una vida
#Si se genera cualquier otro numero dentro un rango rdtsblrcido, gana puntos.




#while vidas !=0:
   #num=random.randint(0,9)
   #if num !=0:
       #puntos+=1
       #print("Tienes ",{puntos},"puntos")
   #else:
       #vidas-=1
       #print("Te quedan", {vidas},"vidas")

#Reciban por consola el valor de una compre
#que puedan ingresar el numero de cuotas
#calcular el valor de la cuota
#usando while queremos que imprima el plan de pago y le muestre el cupo liberado con cada pago


#valor=int(input(f"ingrese el valor total de la compra"))
#cuotas=int(input(f"Ingrese cantidad de cuotas a diferir"))
#interes=valor*0.18
#valor_cuota=(valor+interes)/cuotas
#numcuotas=1

#while cuotas !=0:
    #print(f"El valor de la cuota , {numcuotas} es {valor_cuota}")
    #numcuotas+=1
    #cuotas-=1


#print("1. Registro\n 2.Login\n 3.Salir)"

#opc=0

#if opc==1:
    #print("Registro")
#elif opc==2:
    #print("Login")
#elif opc==3:
    #print("Salir")
#else:
    #print(("Seleccione una opción valida")

#Generar un programa que permita hacer el registro e iniciar sesion dentro de While, debe imprimir el menu usando la
#implementación de if,elif,else (selector multiple).Cuando inicie sesion que implemente la solución del calculo de cuotas
#creada en el reto anterior.




#opc=int(input("1. Registro\n 2.Login\n 3.Salir\n"))


#if opc==1:
    #print("Registro")
#elif opc==2:
    #print("Login")
#elif opc==3:
    #print("Salir")
#else:
    #print("Seleccione una opción valida")

#user="duvacean"
#password=12345

#usuario=input(f"ingrese el usuario")
#contraseña=int(input(f"Ingrese su contraseña"))

"""def valor():
    valor=int(input(f"ingrese el valor total de la compra"))

    cuotas=int(input(f"Ingrese cantidad de cuotas a diferir"))

    interes=valor*0.18
    valor_cuota=(valor+interes)/cuotas
    numcuotas=1

    while cuotas !=0:
        print(f"El valor de la cuota , {numcuotas} es {valor_cuota}")
        numcuotas+=1
        cuotas-=1


if usuario==user and password==contraseña:
     print("Bienvenido");
     valor()
else:
     print("Intente de nuevo porfavor");"""

"""saldo=0

acumIngresos=0
acumEgresos=0

isOn= int(input("ingrese 1 para inicializar el servicio\n"))


while isOn !=0:
    opc= int(input("1.Ingreso:\n 2.Egreso:\n 3.Salir"))

    if opc==1:
        ingreso=int(input("Registre el ingreso:"))

        saldo= saldo+ingreso

        print(f"Su saldo es ${saldo}")

        acumIngresos+=1
        print(acumIngresos)
    elif opc==2:
        egreso=int(input("Registre el monto a retirar"))

        saldo=saldo-egreso

        if saldo<=0:
            print("Saldo insuficiente")
            saldo=saldo+egreso
            print(saldo)

        else:
            print(f"Su saldo es $:{saldo}")
        acumEgresos += 1
        print(acumEgresos)

    elif opc==3:
        print("Salir")
        isOn=0
    else:
        print("Ingrese una opción válida")"""

#---------------------------------------------------------------------


"""Las listas son estructuras de datos lineales se crean usando un brackes,ejemplo: my_list=[]
Las listas son ordenadas (Orden de insersion),es decir que el último dato ingresado ocupara la última posición
Emplea metodos para manipular los items de la misma.
Cómo los arrays la primera posición inicia en 0
Permite item duplicados y los trata como independientes, ejemplo:maria,maria.
Las listas son mutables, es decir podemos agregar,actualizar o remover items.
Pueden contener distintos tipos de datos."""


"""nombres=["Juan","Pepito","Maria","Luis"]
#Metodo len valida el tamaño de la lista
print(len(nombres))
print(type(nombres))

listaDatos=["Pepito","Perez",1000000,1.80,True]

print(f"La estatura es de {listaDatos[3]}")

#Slicing de datos
print(listaDatos[0:2])

print(listaDatos[1:4])

print(listaDatos[:4])

print(listaDatos[2:])

print(listaDatos[:-1])

print(listaDatos[:-2])

print(listaDatos[-4:-1])

print(listaDatos[1:4])"""