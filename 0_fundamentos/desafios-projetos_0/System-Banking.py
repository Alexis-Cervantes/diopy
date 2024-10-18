external_menu = """Seja Bem-vindo(a) - Escolha uma Opção:
[C] criar conta    [X] sair : """
internal_menu = """Escolha uma Opção:
[D] depositar    [S] sacar    [E] extrato    [Q] sair : """


saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
user_name = ''
account_number = 260674

while True:
    opcao_e = input(external_menu)

    if opcao_e == "C".lower():
        print('\n'+15*'#'+' CRIAR CONTA '+'#'*15)
        user_name = input("Informe seu nome completo: ")
        if all(c.isalpha() or c.isspace() for c in user_name):
            print(f'Seja Bem-vindo {user_name}')
            print(f'Número de conta: {account_number+1}\n')
        else: print('\033[0;31mDigite valores alfabeticos. Tente de novo\033[m')

    elif opcao_e == "X".lower():
        print('\n'+15*'#'+' SAINDO DO SISTEMA '+'#'*15)
        print(f'Usuario: {user_name} - Número de Conta: {account_number} ')
        print('A Caixa agradece a sua preferença. Volte sempre - SAIDA EXTERNAL\n')
        break

    else: print("\n\033[0;31mOpção Inválida. Selecione una opção (letra do menu) valida.(external_menu)\033[m\n")

    while True:
        opcao_i = input(internal_menu)

        if opcao_i == "D".lower():
            print('\n'+22*'#'+' DEPÓSITO '+'#'*21)
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

        elif opcao_i == "S".lower():
            print('\n'+25*'#'+' SAQUE '+'#'*25)
            print(f'Usuario: {user_name} - Número de Conta: {account_number} ')
            try:
                print(f'{numero_saques+1} SAQUE')
                valor = float(input("Informe o valor do Saque: "))
                print(f'Foram retirados: R$ {valor}')
                print(53*'_'+'\n')
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

        elif opcao_i == "E".lower():
            print('\n'+23*'#'+' EXTRATO '+'#'*22)
            print(f'Usuario: {user_name} - número de Conta: {account_number} ')
            print(30*'-')
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(30*'_')
            print(f"Saldo: R$ {saldo:.2f}")
            print(53*'#'+'\n')

        elif opcao_i == "Q".lower():
            print('\n'+26*'#'+' SAINDO DO SISTEMA '+'#'*26)
            print(f'Usuario: {user_name} - Número de Conta: {account_number} ')
            print('A Caixa agradece a sua preferença. Volte sempre - SAIDA INTERNAL\n')
            break

        else: print("\n\033[0;31mOpção Inválida. Selecione una opção (letra do menu) valida.(internal_menu)\033[m\n")

    # else: print("\n\033[0;31mOpção Inválida. Selecione una opção (letra do menu) valida (external_menu).\033[m\n")
