menu = """Seja Bem-vindo(a) - Para continuar escolha uma opção:
[D] depositar    [S] sacar    [E] extrato    [Q] sair : """

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "D".lower():
        print('\n'+12*'#'+' DEPÓSITO '+'#'*12)
        try:
            valor = float(input("Informe o valor do Depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f'Foram depositados: R$ {valor}\n')
            else: print("Deposito - Valor ivalido. Informa valores positivos maiores de '0'\n")
        except ValueError: print(f'Valor inválido. Digite valores numéricos e inteiros\n')

    elif opcao == "S".lower():
        print('\n'+12*'#'+' SAQUE '+'#'*12)
        try:
            print(f'{numero_saques+1} SAQUE')
            valor = float(input("Informe o valor do Saque: "))
            print(f'Foram retirados: R$ {valor}\n')
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo: print("\nNão tem saldo suficiente")
            elif excedeu_limite: print("Valor excede o limite de R$ 500.00 por SAQUE\n")

            elif excedeu_saques: print("\nVocê atingiu o número máximo de saques")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else: print("Sauque - Valor ivalido. Informe valores positivos e maiores de '0'\n")
        except ValueError: print("\nValor informado é inválido. Digite valores numéricos e inteiros")

    elif opcao == "E".lower():
        print('\n'+8*'#'+' EXTRATO '+'#'*8)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(18*'#'+'\n')

    elif opcao == "Q".lower():
        print(14*'#'+' SAINDO DO SISTEMA '+'#'*14)
        print('\nA Caixa agradece a sua preferença. Volte sempre')
        break

    else: print("Opção Inválida. Selecione una opção (letra) valida.\n")
