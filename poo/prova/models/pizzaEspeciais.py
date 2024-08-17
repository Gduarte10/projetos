from models.pizza import Pizza

class PizzaEspecial (Pizza):
    def __init__(self, nome: str, tamanho: str, adicional: str):
        super().__init__(nome, tamanho)
        self.adicional = adicional

    def detalhes(self):
        print(f'Sabor de pizza: {self.nome}')
        print(f'O tamanho da pizza: {self.tamanho}')
        print(f'O valor da sua pizza e : {self.valor()}')
        print(f'Seus adicionais foram: {self.adicional}')

