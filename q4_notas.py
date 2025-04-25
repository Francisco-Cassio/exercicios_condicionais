from funcoes import obter_numero_real
from funcoes import linhas

def main():
    n1 = obter_numero_real('Primeira nota: ')
    n2 = obter_numero_real('Segunda nota: ')
    n3 = obter_numero_real('Terceira nota: ')

    linhas()

    media = calcular_media(n1, n2, n3)
    classificacao = classificar_nota(n1, n2, n3, media)

    print(f'Com as seguintes notas: {n1:.1f}, {n2:.1f}, {n3:.1f}\nA média é {media:.1f}')
    linhas()
    print(f'O aluno está {classificacao}')

def calcular_media(n1: float, n2: float, n3: float):
    return (n1 + n2 + n3) / 3


def classificar_nota(n1: float, n2: float, n3: float, media: float):
    if n1 == 0 or n2 == 0 or n3 == 0 or media < 5:
        return 'Reprovado'
    elif media < 7:
        return 'de Recuperação'
    else:
        return 'Aprovado'
    

main()