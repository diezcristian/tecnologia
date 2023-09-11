# La aplicacion debe permitir registrar ingresos y contar saldos de estos.
#debe permitir registar egresos y el saldos 
#si el egreso es mayor que el saldo no debe perimtir el retiro y mostrara un mensaje de saldo insuficiente
# la aplicacion llevara registro de los movimientos indicando el numero de ingresos y de egresos

saldo = 0
acumIngresos = 0
acumEgresos = 0

ison = int (input("ingrese 1  para inicializar el servicio"))

while ison !=0:
    opc = int(input("1. Ingreso:/n 2. Egreso/n 3. Salir"))
    
    if opc ==1:
        ingreso = int(input("Registre el ingreso"))
        
        saldo = saldo + ingreso
        
        print (f"Su saldo es ${saldo}")
        #print ("saldo es : " + saldo)
        #print ("saldo es : ", saldo)
        acumIngresos=+1
        print(acumIngresos)
        #acumIngresos = acumIngresos+1
        
    elif opc==2:
        
        egreso = int(input("Registre el monto a retirar"))
        
        saldo = saldo - egreso
        
        if saldo < 0:
            print("Saldo Insuficiente")
            saldo = saldo + egreso
            print(saldo)
            
        else:
            print(f" Su saldo es: $ {saldo}")
            acumEgresos += 1
            print(acumEgresos)
            
    elif opc==3:
        print("Salir")
        ison=0
    else:
        print ("Ingrese una opcion Valida")
            
            
    
            
        