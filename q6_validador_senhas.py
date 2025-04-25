from funcoes import linhas

def main():
    senha = input('Digite sua senha: ')

    linhas()

    if quantidade_caracteres(senha):
        if letra_maiuscula(senha):
            if letra_minuscula(senha):
                if numero(senha):
                    if caractere_especial(senha):
                        print('Sua senha foi validada!')
                    else:
                        print('A senha deve conter ao menos um caractere especial (!@#$%&*)')
                else:
                    print('A senha deve conter ao menos um número')
            else:
                print('A senha deve conter ao menos uma letra minúscula')
        else:
            print('A senha deve conter ao menos uma letra maiúscula')
    else:
        print('A senha deve possuir 8 caracteres')


def quantidade_caracteres(senha: str):
    num = 0
    num_caracteres = 0
    for num_caracteres in senha:
        num += 1
    
    return num >= 8


def letra_maiuscula(senha: str):
    for maiusc in senha:
        if 'A' <= maiusc <= 'Z':
            return True
    return False
    

def letra_minuscula(senha: str):
    for minus in senha:
        if 'a' <= minus <= 'z':
            return True
    return False
    

def numero(senha: str):
    for numero in senha:
        if '0' <= numero <= '9':
            return True
    return False


def caractere_especial(senha: str):
    especiais = '!@#$%&*()'
    for carac in senha:
        if carac in especiais:
            return True
    return False


main() 