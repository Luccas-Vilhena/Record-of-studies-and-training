def verificar_senha():
    key = input('Digite uma senha: ').strip()
    cont_minusculas = 0
    cont_maiusculas = 0
    cont_numericas = 0
    cont_especiais = 0
    pontos = 0
    for caractere in key:
        if caractere.islower():
            cont_minusculas += 1
        elif caractere.isupper():
            cont_maiusculas += 1
        elif caractere.isdigit():
            cont_numericas += 1
        else:
            cont_especiais += 1
    if len(key) >=8:
        pontos += 1
    if cont_minusculas >0:
        pontos += 1
    if cont_maiusculas >0:
        pontos += 1
    if cont_especiais >0:
        pontos += 1
    if cont_numericas >0:
        pontos += 1
    if pontos <= 2:
        print('[Senha Fraca]')
    elif pontos <= 4:
        print('[Senha Média]')
    else:
        print('[Senha Forte]')
    print(f'Tamanho da senha {len(key)} caractere(s)')
    print(f'A senha contém caractere(s) [{cont_minusculas}] minúsculas')
    print(f'A senha contém caractere(s) [{cont_maiusculas}] maiúsculas')
    print(f'A senha contém caractere(s) [{cont_numericas}] númericas')
    print(f'A senha contém caractere(s) [{cont_especiais}] especiais')

verificar_senha()
