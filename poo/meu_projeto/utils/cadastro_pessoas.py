from models.clintes import Cliente
from models.funcionario import Funcionario

def cadastro_pessoa(op):
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: ')
    cpf = input('Digite seu cpf: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')

    if op == 1:
        endereco = input('Digite seu endereço: ')
        cliente = Cliente(nome,sexo,cpf,telefone,email)
        cliente.endereco = endereco
        return cliente
    elif op == 2:
        matricula = input('Digite a matricula: ')
        funcao = input('Digite a função: ')
        salario = float(input('Digite o salario: '))
        funcionario = Funcionario(nome,sexo,cpf,telefone,email,matricula,funcao,salario)
        return funcionario
    else:
        return nome

        