def pesquisa_cliente(clientes):
    print('####### Pesquisa de cliente #######')

    busca = input('Digite o cpf do cliente: ')
    achei = None

    for cliente in clientes:
        if busca == cliente.cpf:
            achei = cliente
            break

    if achei is not None:
        return achei
    else:
        return achei
    

def pesquisa_funcionario(funcionarios):
    print('####### Pesquisa de funcionario #######')

    busca = input('Digite a matricula do funcionario: ')
    achei = None

    for funcionario in funcionarios:
        if busca == funcionario.matricula:
            achei = funcionario
            break
        
    if achei is not None:
        return achei
    else:
        return achei

