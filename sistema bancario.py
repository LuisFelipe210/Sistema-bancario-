menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação negada! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe  valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação inválida! Número máximo de saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_de_saques += 1

        else: print("Operação inválida! O valor informado é inválido.")

    elif opcao == "e":
        print("\n************** EXTRATO **************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:R$ {saldo:.2f}")
        print("***************************************")

    elif opcao =="x":
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada.")