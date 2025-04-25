from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    num = obter_numero_inteiro('Digite um número: ')

    linhas()

    if num != 0:
        if num > 0:
            if verificar_primo(num):
                print(f'o número {num} é primo')
            else:
                print(f'O número {num} não é primo')
        else:
            print('O valor é negativo')
    else:
        print('O valor é zero')


def verificar_primo(num: int):
    if num == 2:
        return True
    else:
        if num > 1:   
            for i in range(2, num):
                return num % i != 0


main()