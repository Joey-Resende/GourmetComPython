# from models import Customers
from time import sleep


def title():
    print()
    print(f'{" Gourmet Panificadora ":*^60}')
    print(f'* Desde 2022 garantindo o sabor e a qualidade dos produtos *')
    print(f'{" Ampla variedade em Pães, Bolos e Salgados ":*^60}')
    print(f'{" Encontre um pãozinho quente mais perto de você! ":*^60}')
    print()


def add_customer():
    sleep(0.5)
    title()
    sleep(0.5)
    flag: int = 0
    name: str = input('Nome: ')
    cpf: str = input('Cpf: ')
    birth: str = input('Data de Nascimento: ')
    email: str = input('Email: ')
    phone: str = input('Telefone: ')
    address: str = input('Endereco: ')
    flag = 1
    sleep(0.5)
    choice: int = int(
        input('Quer ver os dados que foram salvos? [1-Sim/2-Não]: '))
    sleep(0.5)
    if choice == 1:
        sleep(0.5)
        print(f'Nome: {name}')
        sleep(0.5)
        print(f'Cpf: {cpf}')
        sleep(0.5)
        print(f'Data de Nascimento: {birth}')
        sleep(0.5)
        print(f'E-mail: {email}')
        sleep(0.5)
        print(f'Telefone: {phone}')
        sleep(0.5)
        print(f'Endereco: {address}')
        sleep(0.5)
    elif choice == 2:
        print('Cadastro do usúario efetuado com sucesso!')
    else:
        print('Opção inválida! Insira a opção 1, 2.')

    return flag


def log_in():
    sleep(0.5)
    title()
    sleep(0.5)
    flag: int = 0
    choice = int(input('1-Login 2-Cadastro 3-Sair do Sistema: '))
    if choice == 1:
        sleep(0.5)
        user: str = input('Usuario: ')
        sleep(0.5)
        pswd: str = input('Senha: ')
        flag = 1
    elif choice == 2:
        sleep(0.5)
        add_customer()
    elif choice == 3:
        print('Saindo do sistema...')
        sleep(0.5)

    return flag


def physical_stores():
    sleep(0.5)
    title()
    sleep(0.5)
    print('Loja Matriz: Avenida da Integração,\nnº 1204,\nbairro Gercino Coelho,\nPetrolina-PE\n')
    sleep(0.5)
    print('Loja 01: rua 1, \nnº 15, \nbairro Cohab Massangano, \nPetrolina-PE\n')
    sleep(0.5)
    print('Loja 02: rua Praça Barão do Rio Branco, \nnº 1204, \nbairro Gercino Coelho, \nJuazeiro-BA\n')
    sleep(0.5)
    print('Loja 03: Avenida São Francisco, \nnº 200, \nbairro Areia Branca, \nPetrolina-PE.\n')
    sleep(0.5)
    print('Loja 04: Avenida Cardoso de Sá, \nnº 1204, \nbairro Alto Cheiroso, \nPetrolina-PE.')
    sleep(0.5)


def support():
    sleep(0.5)
    title()
    print('Meios de contato: ')
    print()
    sleep(0.5)
    print('Email: panificadoragourmet@gmail.com.br')
    sleep(0.5)
    print('Telefone: (87)98812-0522')
    sleep(0.5)
    print('WhatsApp: (87)98845-2145')
    sleep(0.5)


def options():
    choice: int = 0
    sleep(0.5)
    title()
    sleep(0.5)
    print('Escolha uma opção: ')
    choice = int(input('1-Produtos 2-Lojas Físicas 3-Fale Conosco 4-Sair: '))
    print()

    return choice


def products():
    option: int = 0
    price: float = 0
    end_buy: int = 0
    sleep(0.5)
    title()
    sleep(0.5)
    choice = int(input('1-pão, 2-bolo, 3-salgado, 4-Bebidas: '))
    if choice == 1:
        print()
        print(f'{" Escolha o tipo do pão ":*^60}')
        option = int(
            input('1: Francês - R$0.50| 2: Doce - R$0.75| 3: Croissant - R$2.50: '))
        if option == 1:
            un = int(input('Quantos Pães Francês você quer? '))
            price = un * 0.50
            print()
            print(
                f'Sua compra de {un} unidades de Pão Francês ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} unidades de Pão francês a R${price:.2f}')
                print()
            else:
                print()
        elif option == 2:
            un = int(input('Quantos Pães Doce você quer? '))
            price = un * 0.75
            print()
            print(
                f'Sua compra de {un} unidades de Pão Doce ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} unidades de Pão Doce a R${price:.2f}')
                println()
            else:
                print()
        elif option == 3:
            un = int(input('Quantos Croissant você quer? '))
            price = un * 2.50
            print()
            print(
                f'Sua compra de {un} unidades de Croissant ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} unidades de Croissant a R${price:.2f}')
                print()
            else:
                print()
        else:
            print('Opção inválida! Insira a opção 1, 2 ou 3.')
    elif choice == 2:
        print()
        print(f'{" Escolha o tipo de bolo (Bolos Inteiros) ":*^60}')
        option = int(input(
            '1: Milho - R$10.65| 2: Macaxeira - R$12.15| 3: Chocolate - R$4.50(Fatia): '))
        if option == 1:
            un = int(input('Quantos Bolos de Milho você quer? '))
            price = un * 10.65
            print()
            print(
                f'Sua compra de {un} unidades de Bolo de Milho ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} unidades de Bolo de Milho a R${price:.2f}')
                print()
            else:
                print()
        elif option == 2:
            un = int(input('Quantos Bolos de Macaxeira você quer? '))
            price = un * 12.15
            print()
            print(
                f'Sua compra de {un} unidades de Bolos de Macaxeira ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} unidades de Bolo de Macaxeira a R${price:.2f}')
                print()
            else:
                print()
        elif option == 3:
            un = int(input('Quantas fatias de  Bolo de Chocolate você quer? '))
            price = un * 4.50
            print()
            print(
                f'Sua compra de {un} fatias de Bolo de Chocolate ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} fatias de Bolo de Chocolate a R${price:.2f}')
                print()
            else:
                print()
        else:
            print('Opção inválida!Insira a opção 1, 2 ou 3.')
    elif choice == 3:
        print()
        print(f'{" Escolha o tipo de Salgado ":*^60}')
        option = int(input(
            '1: Torta de Frango - R$4.00| 2: Pizza brotinho - R$3.50| 3: Coxinha - R$3.50: '))
        if option == 1:
            un = int(input('Quantos fatias de Torta de Frango você quer? '))
            price = un * 4.00
            print()
            print(
                f'Sua compra de {un} fatias de Torta de Frango ficará no valor R${price:.2f}.')
            end_buy = ('Deseja finalizar a compra? [1:Sim | 2:Não]: ')
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} fatias de Torta de Frango a R${price:.2f}')
                print()
            else:
                print()
        elif option == 2:
            un = int(input('Quantas Pizzas Brotinho você quer? '))
            price = un * 3.50
            print()
            print(
                f'Sua compra de {un} Pizza Brotinho ficará no valor R${price:.2f}.')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} Pizzas Brotinho a R${price:.2f}')
                print()
            else:
                print()
        elif option == 3:
            un = int(input('Quantas Coxinhas você quer? '))
            price = un * 3.50
            print()
            print(
                f'Sua compra de {un} Coxinha(s) ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(f'Parabéns você comprou {un} Coxinha(s) a R${price:.2f}')
                print()
            else:
                print()
        else:
            print('Opção inválida! Insira a opção 1, 2 ou 3.')
    elif choice == 4:
        print()
        print(f'{" Escolha o tipo de Bebida ":*^60}')
        option = int(
            input('1: Café Expresso - R$ 5.99| 2: Capuccino R$ 9.99 | 3: Água - R$3.50: '))
        if option == 1:
            un = int(input('Quantos Cafés Expresso você quer? '))
            price = un * 5.99
            print()
            print(
                f'Sua compra de {un} Café(s) Expresso ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} Café(s) Expresso a R${price:.2f}')
                print()
            else:
                print()
        elif option == 2:
            un = int(input('Quantos Capuccinos você quer? '))
            price = un * 9.99
            print()
            print(
                f'Sua compra de {un} Capuccino(s) ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(
                    f'Parabéns você comprou {un} Capuccino(s) a R${price:.2f}')
                print()
            else:
                print()
        elif option == 3:
            un = int(input('Quantos Águas você quer? '))
            price = un * 3.50
            print()
            print(f'Sua compra de {un} Águas(s) ficará no valor R${price:.2f}')
            end_buy = int(
                input('Deseja finalizar a compra? [1:Sim | 2:Não]: '))
            print()
            if end_buy == 1:
                print(f'Parabéns você comprou %d Águas(s) a R${price:.2f}')
                print()
            else:
                print()
        else:
            print('Opção inválida!Insira a opção 1, 2 ou 3.')
    else:
        print('Opção inválida!Insira a opçao 1, 2, 3 ou 4.')
