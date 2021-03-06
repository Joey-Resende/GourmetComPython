from gourmet.core import *
from time import sleep
from typing import Optional

import typer
from rich import print
from rich.console import Console
from rich.table import Table

from gourmet.core import add_users_to_database, get_users_from_database
from gourmet.core import add_products_to_database, get_products_from_database

main = typer.Typer(help='gourmet')

console = Console()


@main.command('addUsers')
def add_users(
    name: str,
    user: str,
    pswd: str,
    cpf: str,
    email: str,
    birth: str,
    phone: str,
    address: str,
):
    """Adiciona um usuario no sistema."""
    if add_users_to_database(name, user, pswd, cpf, email, birth, phone, address):
        print('Usuario adicionado no banco de dados!')
    else:
        print('⛈️ deu ruim')


@main.command('listUsers')
def list_users(style: Optional[str] = None):
    """Lists users from the database."""
    users = get_users_from_database(style)
    table = Table(
        title='Gourmet Panificadora'
        if not style
        else f'Gourmet Panificadora {style}'
    )
    headers = [
        'id',
        'date',
        'name',
        'user',
        'pswd',
        'cpf',
        'email',
        'birth',
        'phone',
        'address',
    ]
    for header in headers:
        table.add_column(header, style='blue')
    for user in users:
        user.date = user.date.strftime('%Y-%m-%d')
        values = [str(getattr(user, header)) for header in headers]
        table.add_row(*values)
    console.print(table)


@main.command('addProducts')
def add_products(
    type_product: str,
    name: str,
    isbn: str,
    description: str,
    price: str,
    quant: str,
):
    """Adiciona um produto no sistema."""
    if add_products_to_database(type_product, name, isbn, description, price, quant):
        print('Produto adicionado no banco de dados!')
    else:
        print('⛈️ deu ruim')


@main.command('listProducts')
def list_products(style: Optional[str] = None):
    """Lists products from the database."""
    products = get_products_from_database(style)
    table = Table(
        title='Gourmet Panificadora'
        if not style
        else f'Gourmet Panificadora {style}'
    )
    headers = [
        'id',
        'date',
        'type_product',
        'name',
        'isbn',
        'description',
        'price',
        'quant',
    ]
    for header in headers:
        table.add_column(header, style='blue')
    for product in products:
        product.date = product.date.strftime('%Y-%m-%d')
        values = [str(getattr(product, header)) for header in headers]
        table.add_row(*values)
    console.print(table)


"""
sleep(0.5)
while True:
    choice = log_in()
    if choice == 3:
        break
    elif choice == 1:
        while True:
            option = options_menu()
            if option == 1:
                products()
            elif option == 2:
                physical_stores()
            elif option == 3:
                support()
            elif option == 4:
                break
            else:
                print('Opção inválida! Insira a opção 1, 2, 3 ou 4.')
    elif choice == 2:
        add_customer()
    else:
        print('Opção inválida! Insira a opção 1, 2 ou 3.')
"""
