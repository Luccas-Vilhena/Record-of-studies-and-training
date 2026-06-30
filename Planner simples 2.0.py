from time import sleep
agenda = []
while True:
    print('=-'*30)
    print('Selecione uma das opções abaixo.')
    print('[1] Adicionar Contato ')
    print('[2] Remover Contato ')
    print('[3] Renomear Contato ')
    print('[4] Alterar Telefone. ')
    print('[5] Listar Contatos.')
    print('[6] Encerrar Programa.')
    opcoes = int(input('Digite uma opção: '))
    if opcoes == 1:
        print('|Adicionar contato|')
        while True:
            encontrado = False
            nome = input('Digite o nome do contato: ').strip().capitalize()
            for contato in agenda:
                if contato["nome"] == nome:
                    encontrado = True
                    print('Nome ao contato já adicionado. Tente novamente.')
                    break
            if not encontrado:
                numero = int(input('Digite o número: ').strip())
                agenda.append({"nome": nome, "telefone": numero})
                print(f'{nome} Foi adicionado à agenda.')
                break
    elif opcoes == 2:
        delete = input('Digite o nome do contato que deseja deletar: ').strip().capitalize()
        for contato in agenda:
            if contato["nome"] == delete:
                agenda.remove(contato)
                print(f'Contato {delete} excluido com sucesso.')
    elif opcoes == 3:
        atual = input('Digite o nome do contato que deseja renomear: ').strip().capitalize()
        novo = input('Digite o novo nome do contato: ').strip().capitalize()
        for contato in agenda:
            if contato["nome"] == atual:
                contato["nome"] = novo
                print(f'Contato {atual} renomeado para {novo}.')
    elif opcoes == 4:
        actual = int(input('Digite o número do telefone que deseja alterar: ').strip())
        new = int(input(f'Digite o novo número para o telefone {actual}: ').strip())
        for contato in  agenda:
            if contato["telefone"] == actual:
                contato["telefone"] = new
                print(f'Telefone de {contato["nome"]} alterado para {new}')

    elif opcoes == 5:
        print('='*30)
        print('CONTATOS'.center(30))
        print('='*30)
        if len(agenda) ==0:
            print('Nenhum contato salvo.')
        else:
            for contato in agenda:
                print(f'Nome: {contato["nome"]}')
                print(f'Telefone: {contato["telefone"]}')
                print('-'*30)
    elif opcoes == 6:
        sleep(0.5)
        print('Encerando Programa....')
        break
    else:
        print('Opção inválida. Tente novamente.')