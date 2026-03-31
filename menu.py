from functions import cargar_datos, guardar_datos, create_account, show_accounts, deposit, transfer, show_movements, withdraw

accounts = cargar_datos()

while True:
    print("\n- - - BankSimulator - - -")
    print("1. Crear cuenta")
    print("2. Mostrar cuentas")
    print("3. Depositar")
    print("4. Transferir")
    print("5. Retirar")
    print("6. Mostrar movimientos")
    print("7. Salir")
    
    opc = input("Digite la opcion deseada: \n")
    while not opc.isdigit() or int(opc) < 1 or int(opc) > 7:
        print("Valor invalido, intentar nuevamente...")
        opc = input("Digite la opcion deseada: \n")
    opc = int(opc)
    
    if opc == 1:
        create_account(accounts)
    elif opc == 2:
        show_accounts(accounts)
    elif opc == 3:
        deposit(accounts)
    elif opc == 4:
        transfer(accounts)
    elif opc == 5:
        withdraw(accounts)
    elif opc == 6:
        show_movements(accounts)
    elif opc == 7:
        guardar_datos(accounts)  
        print("Guardando datos y cerrando...")
        break