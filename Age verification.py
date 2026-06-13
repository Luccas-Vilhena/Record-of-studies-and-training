"""
:param lin() => A custom function aesthetically designed to improve visibility
:param while anos < 0: => Simple checker using 'while' to prevent the user from entering invalid numbers
:param if anos <= 12: => Check if the user is 12 years old or younger, returning that he/she is a child
:param elif anos <= 17: => Check if the user is 17 years old or younger, returning that they are a teenager
:param elif anos <= 59: => Check if the user is under 59 years old, if so, return that he is an adult
:param else: => If the age that the user enters is not in any elif, he is an elderly person
"""
def lin():
    print('-='*30)
lin()
nome = input('Olá, qual seu nome: ').strip()
lin()
anos = int(input('Quantos anos você têm: '))
lin()
while anos < 0:
    print('ERRO! Digite uma idade válida.')
    anos = int(input('Quantos anos você têm: '))
if anos <=12:
    lin()
    print(f'[{nome}]Você tem {anos} anos e é considerado(a) uma criança.')
    lin()
elif anos <= 17:
    lin()
    print(f'[{nome}]Você tem {anos} anos e é considerado(a) um adolescente.')
    lin()
elif anos <=59:
    lin()
    print(f'[{nome}]Você tem {anos} anos e é considerado(a) um adulto.')
    lin()
else:
    lin()
    print(f'[{nome}]Você tem {anos} anos e é considerado(a) um idoso.')
    lin()
