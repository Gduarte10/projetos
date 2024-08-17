class Pizza:
    def __init__(self, nome: str, tamanho: str):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = 0
    
    def valor(self):
        if self.tamanho.upper() == 'P':
             self.preco ='$50'
        elif self.tamanho.upper() == 'M' :
            self.preco = '$60'
        elif self.tamanho.upper() == 'G':
            self.preco = '$70'
        return self.preco
    
   
            
