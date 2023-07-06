menu = """

[d] Depoistar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print("Operação inválida. O valor inserido é inválido.")

    elif opcao == "s":
        valor = float(input("Insira o valor do saque: "))

        if valor > saldo:
            print("Operação inválida. Não há saldo suficiente.")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação inválida. O número máximo de saques diários foi excedido.")
        
        elif valor > limite:
            print("Operação inválida. O valor do saque inserido  excede o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque R$ {valor:.2f}\n'
            numero_saques += 1
        
        else:
            print("Operação inválida. O valor inserido é inválido.")
    
    elif opcao == "e":
        print(" EXTRATO ".center(25, '#'))
        print(f'Não foram realizadas operações' if not extrato else extrato)
        print(f'Saldo atual: R$ {saldo:.2f}\n')
        print("#".center(25, '#'))
    
    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida. Por favor selecione novamente uma operação.")