from models.pizza import Pizza

class PizzaEspecial(Pizza):
    def __init__(self, nome: str, tamanho: str, adicionas: list):
        super().__init__(nome, tamanho)
        self.adicionais = adicionas

    def calcular_adicional(self):
        preco_adicional = 2
        total = 0

        for item in self.adicionais:
            total += preco_adicional


        return total 
    
    def detalhes_especiais(self):
        print(f'Adicionais: {self.adicionais}')
        print(f'preço dos adicionais: {self.calcular_adicional()}')

pizza = PizzaEspecial('calabreso', 'M',  ['musarelo','chedder'] )

pizza.calcular_preco()

pizza.detalhes()
pizza.detalhes_especiais()