def obter_numero_real(label: str):
    entrada = input(label)
    try:
        numero = float(entrada)
        return numero
    except:
        print(f'O valor "{entrada}" não é um numero real')
        return obter_numero_real(label)


def obter_numero_inteiro(label: str):
    entrada = input(label)
    try:
        numero = int(entrada)
        return numero
    except:
        print(f'O valor "{entrada}" não é um numero inteiro')
        return obter_numero_inteiro(label)
    

def obter_numero_inteiro_min(label: str, min: int):
    numero = obter_numero_inteiro(label)

    if numero >= min:
        return numero
    else:
        print(f'O valor é menor que o valor minimo "{min}"')
        return obter_numero_inteiro_min(label, min)
    

def linhas():
    print('-' * 30)