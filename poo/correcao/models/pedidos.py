from pizza import Pizza
from pizza_especial import PizzaEspecial

class Pedido:
    def __init__(self, numero_pedidos: int):
        self.pizzas = []
        self.numero_pedidos = numero_pedidos

    def adicional_pizza(self, pizza, ):
        self.pizzas.append(pizza)

    def total_pedido(self):
        total = 0
        for pizza in self.pizzas:
                total += pizza.preco
                if isinstance(pizza,PizzaEspecial):
                     total += pizza.calcular_adicional()

        return total
        
    def detalhes_pedido(self):
        print(f'Total do pedido #{self.numero_pedidos}: R${self.total_pedido():.2f}')
        
# pizza1 = Pizza('calaboca', 'M')
#pizza1.calcular_preco()

#izza2 = Pizza('portogoza', 'G')
#pizza2.calcular_preco()

#pizza3 = PizzaEspecial('calabresa', 'M', ['muçarela','cheddar'])
#pizza3.calcular_preco()

#p = Pedido(1011)
# p.adicional_pizza(pizza1)
# p.adicional_pizza(pizza2)
# p.adicional_pizza(pizza3)

# for pizza in p.pizzas:
#     pizza.detalhes()
#     if isinstance(pizza, PizzaEspecial):
#        pizza.detalhes_especiais()

# p.detalhes_pedido()
