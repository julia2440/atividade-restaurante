"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Heloisa Lima de Oliveira
2 - júlia Vitória dos Santos Azevedo Jesus

"""


import os

# Limpa o terminal.
os.system("cls || clear") 

menu = {
    1: {"nome": "Espaguete à Carbonara", "preco": 25.00},
    2: {"nome": "Pizza Margherita", "preco": 30.00},
    3: {"nome": "Sushi Variado", "preco": 50.00},
    4: {"nome": "Salada Caesar", "preco": 20.00},
    5: {"nome": "Bife à Parmegiana", "preco": 40.00},
    6: {"nome": "Lasanha de Berinjela", "preco": 35.00},
    7: {"nome": "Tacos de Frango", "preco": 28.00}
}

def exibir_menu():
    print("Menu:")
    for codigo, prato in menu.items():
        print(f"Código: {codigo} - {prato['nome']} - Preço: R${prato['preco']:.2f}")
    print("Digite 0 para finalizar o pedido.")

def solicitar_codigo():
    while True:
        try:
            codigo = int(input("Digite o código do prato desejado: "))
            if codigo in menu or codigo == 0:
                return codigo
            else:
                print("Código inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def calcular_total(pedidos):
    subtotal = sum(menu[codigo]["preco"] for codigo in pedidos)
    return subtotal

def solicitar_pagamento(subtotal):
    while True:
        forma_pagamento = input("Escolha a forma de pagamento (1 para À vista, 2 para Cartão de crédito): ")
        if forma_pagamento == '1':
            desconto = subtotal * 0.10
            total = subtotal - desconto
            return total, desconto, "À vista"
        elif forma_pagamento == '2':
            acréscimo = subtotal * 0.10
            total = subtotal + acréscimo
            return total, acréscimo, "Cartão de crédito"
        else:
            print("Opção inválida. Tente novamente.")

def exibir_resultados(pedidos, subtotal, total, desconto_ou_acrescimo, forma_pagamento):
    print("\n--- Resultados do Pedido ---")
    print("Pratos escolhidos:")
    for codigo in pedidos:
        print(f"{codigo}: {menu[codigo]['nome']} - R${menu[codigo]['preco']:.2f}")
    print(f"Subtotal: R${subtotal:.2f}")
    print(f"Forma de pagamento: {forma_pagamento}")
    if desconto_ou_acrescimo < 0:
        print(f"Desconto aplicado: R${-desconto_ou_acrescimo:.2f}")
    else:
        print(f"Acréscimo aplicado: R${desconto_ou_acrescimo:.2f}")
    print(f"Total a pagar: R${total:.2f}")

def main():
    pedidos = []
    
    while True:
        exibir_menu()
        codigo = solicitar_codigo()
        
        if codigo == 0:
            break
        
        pedidos.append(codigo)
    
    subtotal = calcular_total(pedidos)
    total, desconto_ou_acrescimo, forma_pagamento = solicitar_pagamento(subtotal)
    exibir_resultados(pedidos, subtotal, total, desconto_ou_acrescimo, forma_pagamento)

if __name__ == "__main__":
    main()