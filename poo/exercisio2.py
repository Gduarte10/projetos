class Produto:
     def __init__(self, cod, preço, quant, nome ):
          self.cod = cod
          self.preço = preço
          self.quant = quant 
          self.nome = nome 

def impressao(item):
     print(f'nome: {item.nome}')
     print(f'preço: {item.preço}')
     print(f'quant: {item.quant}')
     print(f'cod: {item.cod}')

produtos = []
while True:
     nome = input('Digite o nome do produto:')
     preço = float(input('Digite o preço do produto:'))
     quant = int(input('Digite a quantidade do protudo:'))
     cod = int(input('DIgite a cod do protudo:'))  

     pro = Produto(cod, preço, quant, nome)
     produtos.append(pro) 

     sair = input('Digite s para sair ou enter para continuar: ')
     if sair.upper() == 'S':
          break 
for produto in produtos:
 impressao(produto)  

busca = input('Digite o nome do produto que deseja ver os dados:')
achei = ''
for produto in produtos:
    if busca == produto.nome:
        achei = produto
        break

if achei != '':
    impressao(achei)
else:
    print('Matricula não encontrada')