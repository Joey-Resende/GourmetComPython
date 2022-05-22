#from models import Customers


def title():
    print()
    print(f'{" Gourmet Panificadora ":*^60}')
    print(f'* Desde 2022 garantindo o sabor e a qualidade dos produtos *')
    print(f'{" Ampla variedade em Pães, Bolos e Salgados ":*^60}')
    print()


def add_customer():
    name: str = input('Nome: ')
    cpf: str = input('Cpf: ')
    birth: str = input('Data de Nascimento: ')
    email: str = input('Email: ')
    phone: str = input('Telefone: ')
    address: str = input('Endereco: ')
    choice: int = int(
        input('Quer ver os dados que foram salvos? [1-Sim/2-Não]: '))
    if choice == 1:
        print(f'{name=}')
        print(f'{cpf=}')
        print(f'{birth=}')
        print(f'{email=}')
        print(f'{phone=}')
        print(f'{address=}')
    elif choice == 2:
        print('Cadastro do usúario efetuado com sucesso!')
    else:
        print('Opção inválida! Insira a opção 1, 2.')


def log_in():
    choice = int(input('1-Login 2-Cadastro 3-Sair do Sistema:'))
    if choice == 1:
        user: str = input('Usuario: ')
        pswd: str = input('Senha: ')
    elif choice == 2:
        add_customer()
    elif choice == 3:
        print('Saindo do sistema...')
