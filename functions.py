import json
from validaciones import insert_monto, insert_text, insert_account_num, movements_reg


def create_account(accounts):
    name = insert_text("Nombre: ")
    surname = insert_text("Apellido :")
    balance = insert_monto("Saldo inicial (min. $100): ")
    
    while balance < 100:
        print("El saldo minimo debe ser mayor a 100.")
        balance = insert_monto("Saldo inicial (min. $100): ")
        
        
    if not accounts:
        account_num = 1001
    else:
        last_account = accounts[-1]
        account_num = last_account["account_num"] + 1
    
    info = {
        "account_num": account_num,
        "name": name,
        "surname": surname,
        "balance": balance,
        "movements": []
    }
    accounts.append(info)
    print("¡Cuenta Creada Exitosamente!\n")
    print(f"Cuenta: {info['account_num']} | {info['name']} | {info['surname']} | Saldo: ${info['balance']:.2f}")
    
    
    
def show_accounts(accounts):
    if not accounts:
        print("No hay usuarios registrados.")
        return
    else:
        for i in accounts:
            print(f"{i['account_num']} | {i['name']} | {i['surname']} | {i['balance']:.2f}")

def deposit(accounts):
    if not accounts:
        print("No hay usuarios registrados.")
        return
    
    num_found = False
    while not num_found:
        
        show_accounts(accounts)
    
        account = insert_account_num("Digita el número de cuenta: ")
    
        for i in accounts:
            if i["account_num"] == account:
                num_found = True
                monto = insert_monto("\nInserta el monto a depositar (min $100): ")
                while monto < 100:
                    print("\nDeposito minimo de $100, intentar nuevamente")
                    monto = insert_monto("\nInserta el monto a depositar (min $100): ")
                i["balance"] += monto
                movements_reg(i, "Deposito", monto, i["balance"])
        
        
        if not num_found:
            print("El número de cuenta ingresado, no existe...")
            
                
            
            

def withdraw(accounts):
    if not accounts:
        print("No hay usuarios registrados.")
        return
    
    
    num_found = False
    while not num_found:
        show_accounts(accounts)
        
        print("Selecciona una cuenta usando el número de cuenta")
        
        account = insert_account_num("Número de cuenta: ")
        
        for i in accounts:
            if i["account_num"] == account:
                monto = insert_monto("\nInserta el monto a retirar: ")
                while monto < 50:
                    print("\nRetiro minimo $50, intente nuevamente")
                    monto = insert_monto("\nInserta el monto a retirar: ")
                if monto > i["balance"]:
                    print("Saldo insuficiente...")
                else: 
                    i["balance"] -= monto
                    movements_reg(i, "Retiro", monto, i["balance"])
                    num_found = True
        
        if not num_found:
            print("El número de cuenta ingresado, no existe...")

def transfer(accounts):
    if not accounts:
        print("No hay usuarios registrados.")
        return
    
    show_accounts(accounts)
    
    origin_found = False
    while not origin_found:
        origin_account = insert_account_num("\nDigita el número de cuenta origen: ")
        for i in accounts:
            if i["account_num"] == origin_account:
                origin_account = i
                origin_found = True
        if not origin_found:
            print("Cuenta no encontrada...")
    
    show_accounts(accounts)
    destination_found = False
    while not destination_found:
        destination_account = insert_account_num("\nDigita el número de cuenta destino: ")
        if destination_account == origin_account["account_num"]:
            print("La cuenta origen y destino no pueden ser iguales.")
            continue
        for i in accounts:
            if i["account_num"] == destination_account:
                destination_account = i
                destination_found = True
        if not destination_found:
            print("Cuenta no encontrada...")
    
    
    sufficient_balance = False
    while not sufficient_balance:
        amount_transfer = insert_monto("Inserta el monto a transferir: ")
        if origin_account["balance"] >= amount_transfer:
            sufficient_balance = True
            origin_account["balance"] -= amount_transfer
            movements_reg(origin_account, "Transferencia Enviada", amount_transfer, origin_account["balance"])
            destination_account["balance"] += amount_transfer
            movements_reg(destination_account, "Transferencia Recibida", amount_transfer, destination_account["balance"])
        else:
            print("Saldo insuficiente en cuenta origen, intente nuevamente")
        
    

def show_movements(accounts):
    if not accounts:
        print("No hay usuarios registrados.")
        return
    
    account_found = False
    while not account_found:
        show_accounts(accounts)
        print("Selecciona una cuenta usando el número de cuenta")    
        account = insert_account_num("Número de cuenta: ")
        for i in accounts:
            if i["account_num"] == account:
                account_found = True
                if not i["movements"]:
                    print("No hay movimientos registrados.")
                else:
                    for b in i["movements"]:
                        print(f"{b['movement_type']} | {b['amount']:.2f} | ${b['new_balance']:.2f}\n")
        
        if not account_found:
            print("Cuenta no encontrada, intente nuevamente...\n")
        
    
    

def cargar_datos():
    try:
        with open("clients.json", "r") as archivo: #Abre archivo en modo lectura
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(accounts):
        with open("clients.json", "w")as archivo: #Abre archivo en modo escritura
            json.dump(accounts, archivo, indent=4)