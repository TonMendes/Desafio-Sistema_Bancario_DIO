menu = '''

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=>
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: RS {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido.")
    
    elif opcao == "S":
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação Falhou! O valor de saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação Falhou! Número máximo de Saques excedido.")  

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação Falhou! O valor informado é invalido.")
    
    elif opcao == "E":
        print("\n============================= EXTRATO =============================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================================")
    
    elif opcao == "Q":
        break

    else:
        print("Operação Inválida! Por favor selecione novamente a operação desejada.")
