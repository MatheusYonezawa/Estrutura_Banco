menu = """

[d] Deposito
[s] Saque ("limite de saque diario  (3) ")
[e] Extrato
[q] Sair

=> """

deposito = 0
saque = 0
extrato = 0
numero_saques = 0
valor_saque = 0
continuar_saque = ""


while True:
    
    escolha=input(menu)

    if escolha == "d": 
        deposito = float(input("digite o valor de deposito: "))
        extrato += deposito
   
    elif escolha == "s":
        valor_saque = float(input("digite o valor do saque: "))
        if valor_saque > extrato:
            print("valor indisponivel")
            continue

        elif valor_saque <= extrato:
            
            print("Saque realizado", valor_saque)
            extrato = extrato - valor_saque
            continuar_saque = input("Gostaria refazer a operação ? [s] ou [n] ")

            if continuar_saque == "s" and valor_saque <= deposito:
                continue
            else:
                print("Obrigado por usar o BANCO: ")
                break    

    elif escolha == "e":
        print("valor da conta: ", extrato)

    elif escolha == "q":
        print("Obrigado por usar o BANCO ")
        break        

    else:
        print("Comando inexistente. \nTente de novo ")
        continue
