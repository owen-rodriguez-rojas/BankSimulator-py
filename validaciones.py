#Refactorizacion

def insert_text(mensaje: str):
    valor = input(mensaje).strip()
    while not valor.isalpha() or valor == "":
        print("Caracteres incorrectos, intente nuevamente...")
        valor = input(mensaje).strip()
    return valor

def insert_monto(mensaje: str):
    while True:
        valor = input(mensaje).strip()
        try:
            valor = float(valor)  
            if valor <= 0:       
                print("El monto debe ser mayor a $0.")
            else:
                return valor
        except ValueError:        
            print("Valor inválido, ingresa un número.")

def insert_account_num(mensaje: str):
    valor = input(mensaje).strip()
    while not valor.isdigit():
        print("Valor invalido, intente nuevamente...")
        valor = input(mensaje).strip()

    return int(valor)


def movements_reg(account: dict, movement_type: str, amount: float, new_balance: float):
    
    movements = {
        "movement_type": movement_type,
        "amount": amount,
        "new_balance": new_balance
    }
    account["movements"].append(movements)



