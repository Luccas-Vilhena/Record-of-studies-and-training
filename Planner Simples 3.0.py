import uuid
def menu():
    print('=-' * 30)
    print('Contatos')
    print('=-' * 30)
    print('[1]Adicionar Contato: ')
    print('[2]Deletar Contato da agenda: ')
    print('[3]Alterar Número do Contato: ')
    print('[4]Listar Contatos: ')
    print('[5]Renomear Contato: ')
    print('[6]Sair do Programa: ')
    while True:
        try:
            opcoes = int(input('Digite uma opção: ').strip())
            break
        except ValueError:
            print('Opção invalida. Tenta novamente.')
    if opcoes == 1:
        add_contato()
    elif opcoes == 2:
        deletar()
    elif opcoes == 3:
        alterar_num()
    elif opcoes == 4:
        lista()
    elif opcoes == 5:
        renomear()
    elif opcoes == 6:
        print('Saindo do programa...')
    else:
        print('Opção invalida. Tenta novamente.')
    return opcoes
def add_contato():
    print('=-'*30)
    print('|Adicionar Contato|'.center(60))
    print('=-'*30)
    nome = input('Nome: ').strip()
    sobrenome = input('Sobrenome: ').strip()
    telefone = input("Telefone: ").strip()
    pode_criar = True
    for contato in agenda:
        if contato["telefone"] == telefone:
            pode_criar = False
            print("Esse número ja foi adicionado a agenda.")
            break
    if pode_criar:
        id_contato = uuid.uuid4()
        agenda.append({"id": id_contato, "nome": nome,"sobrenome":sobrenome, "telefone":telefone})
        print(f'{nome} Foi adicionado á agenda.')
    return
def deletar():
    nome_delete = input('Digite o nome do contato que deseja deletar: ').strip()
    sobre_delete = input('Sobrenome: ').strip()
    num_delete = input("Telefone: ").strip()
    if nome_delete == "" and sobre_delete == "" and num_delete == "":
        print('Você precisa informar pelo menos um dado.')
        return
    candidatos = []
    for contato in agenda:
        if (
            (nome_delete == "" or contato["nome"] == nome_delete)
            and (sobre_delete == "" or contato["sobrenome"] == sobre_delete)
            and  (num_delete == "" or contato["telefone"]== num_delete)
        ):
                    candidatos.append(contato)
    if len(candidatos) == 0:
        print('Nenhum Contato Encontrado: ')
    elif len(candidatos) == 1:
        agenda.remove(candidatos[0])
    else:
        print('=-' * 25)
        print(' |  CONTATOS ENCONTRADOS |'.center(25))
        print('=-' * 25)
        for indice, contato in enumerate(candidatos):
            print(f'[{indice}]| Nome|Sobrenome:[{contato["nome"]}]|[{contato["sobrenome"]}]|Telefone:[{contato["telefone"]}]')
        while True:
            try:
                opcao= int(input('Qual Contato Deseja Remover: ').strip())
                id_escolhido = candidatos[opcao]["id"]
                break
            except (ValueError, IndexError):
                print('Opção inválida.')
        for contato in agenda:
            if contato["id"] == id_escolhido:
                agenda.remove(contato)
                break
def alterar_num():
    nome_busca = input('Digite o nome do contato: ').strip()
    sobrenome_busca = input('Digite o sobrenome do contato: ').strip()
    existente = []
    for contato in agenda:
        if contato["nome"] == nome_busca and contato["sobrenome"] == sobrenome_busca:
            existente.append(contato)
    if len(existente) == 0:
        print('Contato não encontrado.')
    elif len(existente) == 1:
        novo_telefone = input('Digite o novo telefone: ').strip()
        existente[0]["telefone"] = novo_telefone
        print(f'Telefone {existente[0]["nome"]} alterado para {novo_telefone}')
    else:
        for indice, contato in enumerate(existente):
            print(f'[{indice}]| Nome|Sobrenome:[{contato["nome"]}]|[{contato["sobrenome"]}]|Telefone:[{contato["telefone"]}]')
        while True:
            try:
                escolha = int(input('Qual contato deseja alterar: ').strip())
                novo_telefone = input('Digite o novo telefone: ').strip()
                existente[escolha]["telefone"] = novo_telefone
                print(f'Telefone de {existente[escolha]["nome"]} alterado para {novo_telefone}')
                break
            except (ValueError, IndexError):
                print("Erro. Tente novamente.")
def lista():
    print('=-'*40)
    print('    CONTATOS    '.center(40))
    print('=-'*40)
    if not agenda:
        print('Nenhum contato salvo.')
    else:
        for contato in agenda:
            print('=-'*40)
            print(f'Nome: {contato["nome"]}')
            print(f'Telefone: {contato["telefone"]}')
            print('=-'*40)
def renomear():
    tel_busca = input('Digite o telefone do contato: ').strip()
    for contato in agenda:
        if contato["telefone"] == tel_busca:
            novo_nome = input('Digite o novo nome: ').strip()
            novo_sobrenome = input('Digite o novo sobrenome: ').strip()
            contato["nome"] = novo_nome
            contato["sobrenome"] = novo_sobrenome
            print(f'Contato renomeado para {novo_nome} {novo_sobrenome}.')
            return
    print('Nenhum contato encontrado.')
agenda = []
while True:
    if menu() == 6:
        break
