def converter_dolar_para_real():
    cotacao_dolar = 5.69 # taxa de cambio fixa para exemplo
    dolares = float(input("digite o valor em dolares (USD): "))
    reais = dolares * cotacao_dolar
    print(f"{dolares} USD equivale a R$ {reais:.2f}")

def converter_real_para_dolar():
        cotacao_dolar = 5.69 # taxa de cambio fixa para exemplo
        reais = float(input("digite o valor em reais (BRL): "))
        dolares = reais / cotacao_dolar 
        print(f"{reais} BRL equivale a US$ {dolares:.2f}")

def menu():
    while True:
        print("\conversor de moedas")
        print("[1] converte dolar para real")
        print("[2] converter real para dolar")
        print("[0] sair")
        opcao = input("escolha uma opcao: ")

        if opcao == "1": 
             converter_dolar_para_real()
        elif opcao == "2":
             converter_real_para_dolar()
        elif opcao == "0":
             print("saindo...")
             break
        else:
             print("---------------------------------------------------")
             print("!!!!!!!!! opcao invalida. tente novamente !!!!!!!!!")
             print("---------------------------------------------------")
        
menu()