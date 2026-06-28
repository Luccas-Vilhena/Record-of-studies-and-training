from time import sleep
agenda = []
while True:
    print('[1] Adicionar Contato:')
    print('[2] Remover contato:')
    print('[3] Renomear contato:')
    print('[4] Listar contato:')
    print('[5] Sair:')
    opcoes = int(input('Selecione uma opção: '))
    if opcoes ==1:
        nome = input('Digite o nome: ').strip().capitalize()
        número = input('Digite o número: ')
        agenda.append({"nome":nome,"telefone":número})
    elif opcoes ==2:
        delete = input('Digite o nome do contato que deseja deletar: ').strip().capitalize()
        for contato in agenda:
            if contato["nome"] == delete:
                agenda.remove(contato)
                print(f'Contato Excluido.')
    elif opcoes ==3:
        atual = input('Digite o nome do contato que deseja renomear: ').strip().capitalize()
        novo = input('Digite o novo nome do contato: ').strip().capitalize()
        for contato in agenda:
            if contato["nome"] == atual:
                contato["nome"] = novo
                print(f'Contato renomeado para |{novo}')
    elif opcoes ==4:
        for contato in agenda:
            print(contato["nome"], contato["telefone"])
    elif opcoes ==5:
        sleep(0.5)
        print('Encerrando programa...')
        break