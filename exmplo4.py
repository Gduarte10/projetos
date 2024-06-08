'''
Sistema que leai duas notas e o nome do aluno
calcular a média
mostrar se o aluno está aprovado (media >= 6)
reprovado (media <5)
recuperação (media >= 5 e media < 6)

'''

nota1 = float(input('Digite sua primeira nota'))
nota2 = float(input('Digite sua segunda nota'))
media = (nota1 + nota2) /2

if media >= 6:
    print('aprovado')
elif media <5:
    print('reprovado')
else :
    print('recuperação')