from poo.meu_projeto.services.caixa.lista_produtos import lista_produtos
from poo.meu_projeto.services.adm.cadastro import cadastro
from poo.meu_projeto.services.caixa.pesquisa import pesquisa
from poo.meu_projeto.services.caixa.vendas import venda_produto
from poo.meu_projeto.services.adm.reajuste import reajuste_produto
from utils.cadastro_pessoas import cadastro_pessoa
def main():
    produtos = []
    clientes = []
    funcionarios = []
    while True:
        opcao = int(input('Escolha a opção desejada \n'
                        '1- Para cadastrar produto'
                        '\n2- Para pesquisar produto'
                        '\n3- Para impressão da lista de produtos'
                        '\n4- Para venda do produto'
                        '\n5- Para reajuste: '
                        '\n6- Para cadastrar um cliente: '
                        '\n7- Para cadastre um funcionario '
                    ))
        if opcao == 1: 
            produtos.append(cadastro())
        elif opcao == 2:
            pesquisa(produtos)
        elif opcao == 3:
            lista_produtos(produtos)
        elif opcao == 4:
            venda_produto(produtos)
        elif opcao == 5:
            reajuste_produto(produtos)
        elif opcao == 6:
            clientes.append(cadastro_pessoa(1))
        elif opcao == 7:
            funcionarios.append(cadastro_pessoa(2))
        else:
            print('Opção inválida!')

        sair = input('Digite s para sair ou enter para continuar: ')
        if sair.upper() == 'S':
            break

if __name__ == '__main__':
    main()
