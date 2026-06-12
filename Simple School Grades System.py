print('='*30)
nome = input('Olá, qual seu nome: ')
print('='*30)
nota = float(input(f'Digite sua nota [{nome}]: '))
if nota >= 7:
    print(f'Você foi aprovado [{nome}]!')
else:
    print(f'Você foi reprovado [{nome}].')
