
senha_correta = 123456
valor_disponivel = 5000

def caixa_eletronico():
    global valor_disponivel
    
    print("Iniciaalizando sistema...")
    senha_digitada = int(input("Digite sua senha: "))

    if senha_digitada != senha_correta:
        print("Senha incorreta ")
        print("Finalizando o sistema ")
    else:
        print("Senha correta ")

    while True:
        print("\n--- CAIXA ELETRONICO ---")
        print("[0] SAQUE")
        print("[1] DEPOSITO")
        print("[3] CONSULTA A SALDO")
        print("[4] SAIR")

        opcao = input("EScolha uma opção: ")
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
            print(f"Saldo atual R$: {valor_disponivel}")
        
   
        


