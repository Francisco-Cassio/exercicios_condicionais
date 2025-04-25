from funcoes import obter_numero_inteiro
from funcoes import linhas

def main():
    lado_a = obter_numero_inteiro('Lado A: ')
    lado_b = obter_numero_inteiro('Lado B: ')
    lado_c = obter_numero_inteiro('Lado C: ')
    linhas()
    angulo_a = obter_numero_inteiro('Ângulo Interno A: ')
    angulo_b = obter_numero_inteiro('Ângulo Interno B: ')
    angulo_c = obter_numero_inteiro('Ângulo Interno C: ')

    linhas()

    if tamanho_zero(lado_a, lado_b, lado_c) or angulo_zero(angulo_a, angulo_b, angulo_c):
        print('Lados ou ângulos não podem ser zero!')
        return

    if eh_triangulo_lados(lado_a, lado_b, lado_c):
        print('\n--- CLASSIFICAÇÃO POR LADOS ---')
        print('Os lados formam um triângulo!')
        if eh_degenerado(lado_a, lado_b, lado_c):
            print('Entretanto, ele é um TRIÂNGULO DEGENERADO!')
        else:
            print('Perímetro:', calcular_perimetro(lado_a, lado_b, lado_c))
            print(f'Área: {calcular_area(lado_a, lado_b, lado_c):.2f}')
        
        if eh_equilatero(lado_a, lado_b, lado_c):
            print('Tipo: EQUILÁTERO')
        elif eh_isosceles(lado_a, lado_b, lado_c):
            print('Tipo: ISÓSCELES')
        elif eh_escaleno(lado_a, lado_b, lado_c):
            print('Tipo: ESCALENO')

    else:
        print('\nOs lados NÃO formam um triângulo válido!')

    if eh_triangulo_angulos(angulo_a, angulo_b, angulo_c):
        if not eh_degenerado(lado_a, lado_b, lado_c):
            print('\n--- CLASSIFICAÇÃO POR ÂNGULOS ---')
            print('Os ângulos formam um triângulo!')
            if eh_acutangulo(angulo_a, angulo_b, angulo_c):
                print('Tipo: ACUTÂNGULO')
            elif eh_retangulo(angulo_a, angulo_b, angulo_c):
                print('Tipo: RETÂNGULO')
            elif eh_obtusangulo(angulo_a, angulo_b, angulo_c):
                print('Tipo: OBTUSÂNGULO')
                print('-----------------------------')
        else:
            print('\nÂngulos válidos, mas os lados são degenerados.')
    else:
        print('\nOs ângulos NÃO formam um triângulo!')


def eh_triangulo_lados(a: int, b: int, c: int):
    return a + b > c and a + c > b and b + c > a


def eh_triangulo_angulos(a: int, b: int, c: int):
    return a > 0 and b > 0 and c > 0 and a + b + c == 180


def calcular_perimetro(a: int, b: int, c: int):
    return a + b + c


def calcular_area(a: int, b: int, c: int):
    p = calcular_perimetro(a, b, c) / 2
    valor = p * (p - a) * (p - b) * (p - c)
    if valor <= 0:
        return 0
    return valor ** 0.5


def eh_degenerado(a: int, b: int, c: int):
    return a == b + c or b == a + c or c == a + b


def eh_escaleno(a: int, b: int, c: int):
    return a != b != c


def eh_isosceles(a: int, b: int, c: int):
    return (a == b or a == c or b == c) and not eh_equilatero(a, b, c)


def eh_equilatero(a: int, b: int, c: int):
    return a == b == c


def tamanho_zero(a: int, b: int, c: int):
    return a == 0 or b == 0 or c == 0


def angulo_zero(a: int, b: int, c: int):
    return a == 0 or b == 0 or c == 0


def eh_acutangulo(a: int, b: int, c: int):
    return a < 90 and b < 90 and c < 90


def eh_retangulo(a: int, b: int, c: int):
    return a == 90 or b == 90 or c == 90


def eh_obtusangulo(a: int, b: int, c: int):
    return a > 90 or b > 90 or c > 90


main()