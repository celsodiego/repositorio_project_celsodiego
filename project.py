def medidas():
    print("Conversor de Unidades")
    print("1. comprimento")
    print("2. Peso")
    print("3. Volume")
    print("3. Sair")

def converter_comprimento():
    print("Escolha a conversão de comprimento: ")
    print("1. Metros para kilometros")
    print("2. Kilometros para Metros")
    print("3. Centímetros para Metros")
    print("4. Metros para centímetros")
    escolha = int(input("Escolha a opção (1/2/3/4): "))
    
    valor = float(input("Digite o valor para conversão: "))
    if escolha == 1:
        resultado = valor / 1000
        print(f"{valor} metros é igual a {resultado} kilometros")
    elif escolha == 2:
        resultado = valor * 1000
        print(f"{valor} kilometros é igual a {resultado} metros")
    elif escolha == 3:
        resultado = valor / 100
        print(f"{valor} centímetros é igual a {resultado} metros")
    elif escolha == 4:
        resultado = valor * 100
        print(f"{valor} metros é igual a {resultado} centímetros")
    else:
        print("Opção inválida")

def converter_peso():
    print("Escolha a conversão de peso: ")
    print("1. Gramas para kilogramas")
    print("2. kilogrmas para Gramas")
    escolha = int(input("Escolha a opção (1/2): "))

    valor = float(input("Digite o valor para conversão: "))
    if escolha == 1:
        resultado = valor * 1000
        print(f"{valor} gramas é igual a {resultado} kilogramas")
    elif escolha == 2:
        resultado = valor / 1000
        print(f"{valor} kilogramas é igual a {resultado} gramas ")
    else:
        print("Opção inválida")

def converter_volume():
    print("Escolha a conversão de volume: ")
    print("1. Litros para Mililitros")
    print("2. Mililitros para Litros")
    escolha = int(input("Escolha a opção (1/2): "))

    valor = float(input("Digite o valor para conversão: "))
    if escolha == 1:
        resultado = valor * 1000
        print(f"{valor} litros é igual a {resultado} mililitros")
    elif escolha == 2:
        resultado = valor / 1000
        print(f"{valor} mililitros é igual a {resultado} litros")
    else:
        print("Opção inválida")

def main():
    while True:
        medidas()
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            converter_comprimento()
        elif escolha == 2:
            converter_peso()
        elif escolha == 3:
            converter_volume
        elif escolha == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida tente novamente")

if __name__ == "__main__":
    main()           