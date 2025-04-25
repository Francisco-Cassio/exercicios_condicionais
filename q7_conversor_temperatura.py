from funcoes import obter_numero_real
from funcoes import linhas

def main():
    temperatura = obter_numero_real('Quantos graus deseja? ')
    linhas()

    validacao_conversao(temperatura)


def eh_celsius(tipo: str):
    return tipo == 'c' or tipo == 'C'


def eh_fahrenheit(tipo: str):
    return tipo == 'f' or tipo == 'F'


def eh_kelvin(tipo: str):
    return tipo == 'k' or tipo == 'K'


def conversao_celsius(temperatura: int, convertido: str):
    if eh_fahrenheit(convertido):
        print(f'{temperatura} °C equivale a {((temperatura * 1.8) + 32):.1f} °F')
    elif eh_kelvin(convertido):
        print(f'{temperatura} °C equivale a {(temperatura + 273.15):.1f} K')


def conversao_fahrenheit(temperatura: int, convertido: str):
    if eh_celsius(convertido):
        print(f'{temperatura} °F equivale a {((temperatura - 32) * 1.8):.1f} °C')
    elif eh_kelvin(convertido):
        print(f'{temperatura} °F equivale a {((temperatura + 459.67) * 1.8):.1f} K')
    

def conversao_kelvin(temperatura: int, convertido: str):
    if eh_celsius(convertido):
        print(f'{temperatura} K equivale a {(temperatura - 273.15):.1f} °C')
    elif eh_fahrenheit(convertido):
        print(f'{temperatura} k equivale a {((temperatura * 1.8) - 459.67):.1f} °F')


def validacao_conversao(temperatura: int):
    tipo_temp = input('Qual tipo de temperatura deseja escolher? (C/F/K): ')
    tipo_convert = input('Para qual tipo deseja converter? (C/F/K): ')
    
    linhas()

    if not eh_celsius(tipo_temp) or not eh_fahrenheit(tipo_temp) or not eh_kelvin(tipo_temp) or not eh_celsius(tipo_convert) or not eh_fahrenheit(tipo_convert) or not eh_kelvin(tipo_convert):
        print('As letras digitadas devem corresponder às unidades de temperatura')
        linhas()
        return validacao_conversao(temperatura)
    

    if tipo_temp == tipo_convert:
        print('As unidades de temperatura devem ser diferentes')
        return validacao_conversao(temperatura)


    if eh_celsius(tipo_temp):
        if temperatura >= -273.15:
            conversao_celsius(temperatura, tipo_convert)
        else:
            print('A temperatura em Celsius não pode ser menor que -273.15 °C')

    elif eh_fahrenheit(tipo_temp):
        conversao_fahrenheit(temperatura, tipo_convert)
    
    elif eh_kelvin(tipo_temp):
        if temperatura >= 0:
            conversao_kelvin(temperatura, tipo_convert)
        else:
            print('A temperatura em Kelvin deve ser maior que 0')


main()
    