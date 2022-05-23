from core import *
from time import sleep


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
