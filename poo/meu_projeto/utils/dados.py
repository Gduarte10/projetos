def impressao_dados(dado,op):
    print(f'nome:{dado.nome}')
    print(f'sexo:{dado.sexo}')
    print(f'email:{dado.email}')
    print(f'CPF:{dado.cpf}')
    print(f'telefone:{dado.telefone}')

    if op == 1:
        print(f'Endereço:{dado.endereco}')
        if dado.ativo:
            print(f'Ativo')
        else:
            print(f'Inativo')
    elif op == 2:
        print(f'Matricula: {dado.matricula}')
        print(f'Função: {dado.funcao}')
        print(f'Salario: {dado.salario}')
    else:
        print('Opção inválida!') 
