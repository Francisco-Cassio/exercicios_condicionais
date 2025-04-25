from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    ano = obter_numero_inteiro('Ano: ')

    linhas()

    if eh_bissexto(ano):
        print(f'O ano {ano} é Bissexto!')
    else:
        print(f'O ano {ano} não é Bissexto')


def eh_bissexto(ano: int):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


main()