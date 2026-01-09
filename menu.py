import os

def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Tabuada")
    print("2 - Calculadora (somar)")
    print("0 - Sair")

def tabuada():
    from matematica.tabuada import tabuada
    n = int(input("Digite um número para ver a tabuada: "))
    tabuada(n)

def calculadora():
    from calculadora import somar
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print("Resultado da soma:", somar(a, b))

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tabuada()
    elif opcao == "2":
        calculadora()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
