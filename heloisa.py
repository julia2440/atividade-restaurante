import os
os.system ("cls || clear")

def selecionar_pratos (cardapio):
    pedidios = []
    while True:
        opcao = input("Digite número do prato que deseja pedir (ou 0 para finalizar: )")
        if opcao == 0:
            break
        if int(opcao) in cardapio:

