'''
class Aluno :
    nome = ''
    matricula = ''
    notas = []
    conceito = ''
    media = 0
    resultado = ''

    def conceitoAL(self):
        if self.media < 40:
            self.conseito = 'E'
        elif self.media <60:
            self.conceito = 'D'
        elif self.media <75:
            self.conceito = 'C'
        elif self.media <90:
            self.conceito = 'B'
        elif self.media >=90:
            self.conceito = 'A'
        

aluno1 = Aluno()
aluno1.nome = 'gabriel'
aluno1.matricula = '220231001'
aluno1.notas = [8, 7, 9]

aluno1.media = sum(aluno1.notas) / len(aluno1.notas)

aluno1.conceito = aluno1.conceitoAL()
print(f'matrícula:{aluno1.matricula}')
print(f'Aluno:{aluno1.nome}')
print(f'Notas:{aluno1.notas}')
print(f'média:{round(aluno1.media, 1)}')
print(f'conceito: {aluno1.conceito}')

'''
class Aluno:
    def __init__(self,nome,matricula,notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        self.media = 0
        self.conseito = ''
        self.resultado = ''

    def conceitoAL(self):
        if self.media < 4:
            return 'E'
        elif self.media <6:
            return 'D'
        elif self.media <7.5:
            return 'C'
        elif self.media <9:
            return 'B'
        elif self.media >=9:
            return 'A'
        
    def resultadoAL(self):
        if self.conceito == 'A' or self.conceito == 'B' or self.conceito == 'C':
            return 'APROVADO'
        else:
            return 'REPROVADO'
        
def impressao (aluno):
    print(f'matrícula:{aluno.matricula}')
    print(f'Aluno:{aluno.nome}')
    print(f'Notas:{aluno.notas}')
    print(f'média:{round(aluno.media, 1)}')
    print(f'conceito: {aluno.conceito}')
    print(f'resultado: {aluno.resultado}')



aluno = Aluno('gabriel','220231001',[10, 10, 10])
aluno.media = sum(aluno.notas) / len(aluno.notas)
aluno.conceito = aluno.conceitoAL()
aluno.resultado = aluno.resultadoAL()

aluno2 = Aluno('ian','1234567890',[4.5, 3, 2])
aluno2.media = sum(aluno2.notas) / len(aluno2.notas)
aluno2.conceito = aluno2.conceitoAL()
aluno2.resultado = aluno2.resultadoAL()

aluno.conceito = aluno.conceitoAL()

impressao(aluno)
print('')
impressao(aluno2)


    