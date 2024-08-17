from services.caixa.lista_produtos import lista_produtos
from services.adm.pesquisa_dados import pesquisa_cliente
from services.adm.pesquisa_dados import pesquisa_funcionario
from services.adm.cadastro import cadastro
from services.caixa.pesquisa import pesquisa
from services.caixa.vendas import venda_produto
from services.adm.reajuste import reajuste_produto
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
                        '\n8- Para pesquisar clientes '
                        '\n9- Para pesquisar funcionario '
                        
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
        elif opcao == 8:
            cliente = pesquisa_cliente(clientes)
            if cliente is not None:
              pesquisa_cliente(clientes, 1)
            else:
                print('cliente não cadastrado')
        elif opcao == 9:
            cliente = pesquisa_funcionario(funcionarios)
            if cliente is not None:
                pesquisa_funcionario(funcionarios,2)
            else:
                print('cliente não cadastrado')
        else:
            print('Opção inválida!')

        sair = input('Digite s para sair ou enter para continuar: ')
        if sair.upper() == 'S':
            break

if __name__ == '__main__':
    main()
