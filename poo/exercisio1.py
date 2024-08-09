class Aluno:
    def __init__(self, nome='', matricula='', notas=None):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas 
        self.media = 0
        self.conceito = ''
        self.resultado = ''

    def calcular_media(self):
        self.media = sum(self.notas) / len(self.notas) if self.notas else 0

    def conceito_aluno(self):
        if self.media < 4:
            return 'E'
        elif self.media < 6:
            return 'D'
        elif self.media < 7.5:
            return 'C'
        elif self.media < 9:
            return 'B'
        else:
            return 'A'

    def resultado_aluno(self):
        if self.conceito in ['A', 'B', 'C']:
            return 'APROVADO'
        else:
            return 'REPROVADO'

def impressao(aluno):
    print(f'matrícula: {aluno.matricula}')
    print(f'aluno: {aluno.nome}')
    print(f'Notas: {aluno.notas}')
    print(f'média: {round(aluno.media, 1)}')
    print(f'conceito: {aluno.conceito}')
    print(f'resultado: {aluno.resultado}')

alunos = []

while True:
    notas = []
    nome = input('Digite seu nome:')
    matricula = input('Digite sua matricula:')
    
    nota1 = float(input('Digite sua primeira nota: '))
    notas.append(nota1)
    
    nota2 = float(input('Digite sua segunda nota: '))
    notas.append(nota2)
    
    nota3 = float(input('Digite sua terceira nota: '))
    notas.append(nota3)
    
    aluno = Aluno(nome, matricula, notas)
    aluno.calcular_media()
    aluno.conceito = aluno.conceito_aluno()
    aluno.resultado = aluno.resultado_aluno()
    
    alunos.append(aluno)

    sair = input('Digite s para sair ou enter para continuar: ')
    if sair.upper() == 'S':
        break

for aluno in alunos:
    impressao(aluno)
    print('')

busca = input('Digite a matricula do aluno que deseja ver os dados:')
achei = ''
for alunos in alunos:
    if busca == aluno.matricula:
        achei = aluno
        break

if achei != '':
    impressao(achei)
else:
    print('Matricula não encontrada')
