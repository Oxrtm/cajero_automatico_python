# Proyecto cajero automatico Python
print('*** Cajero Automatico de Ciudad Gotica ***')
saldo = 3000 # Saldo inical
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar saldo
    2. retirar 
    3. Depositar 
    4. Salir''')
    opcion = int(input('Escoge una opcion: '))
    if opcion == 1:
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))
        # Validacion
        if retiro <= saldo:
            saldo -= retiro # saldo = saldo - retiro
            print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
        else:
            print(f'No cuentas con saldo suficiente. Saldo actual ${saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito # saldo = saldo + deposito
        print(f'Tu nuevo saldfo es: ${saldo:.2f}\n')
    elif opcion == 4:
        print('Saliendo del cajero automatico. Hasta pronto!')
        salir = True
    else:
        print('Opcion invalidad, selecciona otra opcion\n')