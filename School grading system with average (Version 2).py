print('=-'*30)
aluno = input('Qual seu nome: ').strip()
print('=-'*30)
nota1 = float(input(f'Qual foi sua primeira nota [{aluno}]:  '))
nota2 = float(input(f'Qual foi sua segunda nota [{aluno}]:  '))
media = (nota1 + nota2) / 2
print(f'Média final: {media:.1f}')
if media >= 7:
    print(f'Você foi aprovado [{aluno}]!')
elif media >= 5:
    print(f'Aluno [{aluno}] você ficou em recuperação.')
else:
    print(f'Você foi reprovado [{aluno}].')
