senha_correta = 123456 #aqui foi definido uma senha correta
valor_disponivel = 5000#valor quem tem em caixa
#proximo passo e integrar um cadastramento de usuarios

def caixa_eletronico():
    global valor_disponivel
    
    print("Iniciaalizando sistema...")
    senha_digitada = int(input("Digite sua senha: "))

    if senha_digitada != senha_correta:
        print("Senha incorreta...")
        print("Finalizando o sistema...")
        return
    else:
        print("Senha correta ")

    while True:
        print("\n--- CAIXA ELETRONICO ---")
        print("[0] SAQUE")
        print("[1] DEPOSITO")
        print("[2] CONSULTA A SALDO")
        print("[3] SAIR")

        opcao = input("Escolha uma opção: ")
        if opcao == "0":
            valor_escolhido = int(input("Digite o valor: "))
            if valor_escolhido > valor_disponivel:
                print("Saldo insulficiente, finalizando operação...")
            else:
                valor_disponivel -= valor_escolhido
                print("Aguarde a contagem de cédulas... ")
                print("Por favor, retire o dinheiro... ")
                recibo = input("Deseja imprimir recibo? S/N: ")
                if recibo.upper() == "S":
                    print("Imprimindo recibo")
                print("Operação finalizada")
        elif opcao == "1":
            valor_deposito = int(input("Digite o valor do depósito: "))
            valor_disponivel += valor_deposito
            print(f"Depósito realizado. Saldo atual é: {valor_disponivel}")
        elif opcao == "2":
            print(f"O seu saldo é de {valor_disponivel}")
        elif opcao == "3":
            print("Obrigado, volte sempre!")
            break
        else:
            print("Opção invalida. Tente novamente!")
        
caixa_eletronico()

