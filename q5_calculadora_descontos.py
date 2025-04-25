from funcoes import obter_numero_real
from funcoes import linhas

def main():
    valor_compra = obter_numero_real('Valor da compra: R$ ')
    linhas()
    cliente_vip = input('És um cliente VIP? (S/N): ')
    aniversariante = input('É seu aniversário? (S/N): ')

    linhas()

    valor_desconto = descontos(valor_compra, cliente_vip, aniversariante)

    print(f'Após todos os descontos possíveis, sua compra ficou com um valor de\n===> R$ {valor_desconto:.2f} <===')



def descontos(valor: float, cliente_vip: str, aniversariante: str):
    if eh_vip(cliente_vip) == True and eh_aniversariante(aniversariante) == True:
        valor = desconto_base(valor) - desconto_vip(valor) - desconto_aniversariante(valor)

    elif eh_vip(cliente_vip) == True:
        valor = desconto_base(valor) - desconto_vip(valor)
        
    elif eh_aniversariante(aniversariante) == True:
        valor = desconto_base(valor) - desconto_aniversariante(valor)
    
    else:
        valor = desconto_base(valor)

    return valor

    
def desconto_base(valor: float):
    if valor > 100 and valor < 200:
        valor -= (valor * 0.05)
        return valor
    elif valor >= 200 and valor < 500:
        valor -= (valor * 0.1)
        return valor
    elif valor >= 500:
        valor -= (valor * 0.15)
        return valor
    else:
        return valor


def eh_vip(vip: str):
     return vip == 's' or vip == 'S'


def eh_aniversariante(aniversariante: str):
     return aniversariante == 's' or aniversariante == 'S'


def desconto_vip(valor: float):
    return valor * 0.05


def desconto_aniversariante(valor: float):
    return valor * 0.03


main()