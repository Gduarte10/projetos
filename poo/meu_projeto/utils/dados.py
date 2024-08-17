def impressao_dados(dados,op):
    print(f'nome:{dados.nome}')
    print(f'sexo:{dados.sexo}')
    print(f'email:{dados.email}')
    print(f'CPF:{dados.cpf}')
    print(f'telefone:{dados.telefone}')

    if op == 1:
        print(f'Endereço:{dados.endereco}')
        if dados.ativo:
            print(f'Ativo')
        else:
            print(f'Inativo')
    elif op == 2:
        print(f'Matricula: {dados.matricula}')
        print(f'Função: {dados.funcao}')
        print(f'Salario: {dados.salario}')
    else:
        print('Opção inválida!') 
