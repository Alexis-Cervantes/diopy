external_menu = """Seja Bem-vindo(a) - Escolha uma Opção:
[C] criar conta    [Q] sair : """
internal_menu = """Seja Bem-vindo(a) - Escolha uma Opção:
[D] depositar    [S] sacar    [E] extrato    [Q] sair : """


saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
user_name = ''
account_number = 260674

while True:
    opcao = input(internal_menu)

    if opcao == "C".lower():
        print('\n'+12*'#'+' CRIAR CONTA '+'#'*12)
        user_name = input("Informe seu nome completo: ")
        if all(c.isalpha() or c.isspace() for c in user_name):
            print(f'Seja Bem-vindo {user_name}')
            print(f'Número de conta: {account_number+1}\n')
        else: print('\033[0;31mDigite valores alfabeticos. Tente de novo\033[m')

    elif opcao == "D".lower():
        print('\n'+12*'#'+' DEPÓSITO '+'#'*12)
        print(f'Usuario: {user_name} - Número de Conta: {account_number} ')
        try:
            valor = float(input("Informe o valor do Depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f'Foram depositados: R$ {valor}\n')
            elif user_name == "": print('\033[0;31mCrie uma conta primeiro\033[m')
            else: print("\033[0;31mValor fornecido ivalido. Informe valores positivos e maiores de '0'\033[m\n")
        except ValueError: print(f'\033[0;31mValor inválido. Digite valores numéricos e inteiros\033[m\n')

    elif opcao == "S".lower():
        print('\n'+12*'#'+' SAQUE '+'#'*12)
        print(f'Usuario: {user_name} - Número de Conta: {account_number} ')
        try:
            print(f'{numero_saques+1} SAQUE')
            valor = float(input("Informe o valor do Saque: "))
            print(f'Foram retirados: R$ {valor}')
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo: print("\n\033[0;31mNão tem saldo suficiente\033[m\n")
            elif excedeu_limite: print("\033[0;31mValor excede o limite de R$ 500.00 por SAQUE\033[m\n")
            elif excedeu_saques: print("\n\033[0;31mVocê atingiu o número máximo de saques\033[m\n")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else: print("\033[0;31mValor ivalido. Informe valores positivos e maiores de '0'\033[m\n")
        except ValueError: print("\n\033[0;31mValor informado é inválido. Digite valores numéricos e inteiros.\033[m\n")

    elif opcao == "E".lower():
        print('\n'+25*'#'+' EXTRATO '+'#'*25)
        print(f'Usuario: {user_name} - número de Conta: {account_number} ')
        print(60*'-')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(60*'-')
        print(f"Saldo: R$ {saldo:.2f}")
        print(60*'#'+'\n')

    elif opcao == "Q".lower():
        print(14*'#'+' SAINDO DO SISTEMA '+'#'*14)
        print(f'Usuario: {user_name} - Número de Conta: {account_number} ')
        print('A Caixa agradece a sua preferença. Volte sempre\n')
        break

    else: print("\n\033[0;31mOpção Inválida. Selecione una opção (letra do menu) valida.\033[m\n")
