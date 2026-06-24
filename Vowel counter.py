from time import sleep
def vogais(palavra):
    cont = 0
    for l in palavra:
        sleep(0.5)
        if l in "AEIOU":
            cont +=1
        print(f'Letra: {l} | Total de vogais até agora: {cont}')
    return cont
entrada = input('Digite algo: ').strip() .upper()
resultado = vogais(entrada)
print(f'Recebi a palavra {entrada}, e ela contém {resultado} vogais ')