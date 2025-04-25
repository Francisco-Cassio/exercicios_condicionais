from funcoes import obter_numero_real
from funcoes import linhas

def main():
    peso = obter_numero_real('Peso (kg): ')
    altura = obter_numero_real('Altura (m): ')

    linhas()

    if 10 <= altura < 100:
        altura = altura / 10
    elif altura >= 100:
        altura = altura / 100
    
    imc = calculo_imc(peso, altura)
    classificacao = classificacao_imc(imc)

    print(f'Seu IMC é {imc:.1f}\nE está classificado em: {classificacao}')


def calculo_imc(peso: float, altura: float):
    imc = peso / (altura**2)
    return imc


def classificacao_imc(imc: float):
    if imc < 18.5:
        return 'Abaixo do Peso'
    elif imc < 25:
        return 'Peso Normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obesidade Grau I'
    elif imc < 40:
        return 'Obesidade Grau II'
    else:
        return 'Obesidade Grau III'


main()