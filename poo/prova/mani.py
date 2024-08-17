from models.pizza import Pizza
from models.pizzaEspeciais import PizzaEspecial


adicionais = []
def main ():

    nome = input('Qual o sabor da pizza: ')
    tamanho = input('Qual o tamanho (P, M, G):')
    

    while True:
        adicional = input('Qual será seu adicional:')

        adicionais.append(adicional)

        sair = input('Digite s para sair ou enter para continuar: ')
        if sair.upper() == 'S':
            break
    pizza = PizzaEspecial(nome, tamanho, adicionais)
       

    pizza.detalhes()

            
main()      