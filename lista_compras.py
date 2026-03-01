# Lista vazia
compras = []

# Laço de repetição, para o menu e opções 
while True:
    print(35 * '-')
    print('> Bem vindo a sua lista de compras <')
    print('> Temos as seguintes opções: ')
    print(35 * '-')
    print('> 1 - Inserir items')
    print('> 2 - Listar items')
    print('> 3 - Apagar itens')
    print('> 4 - Limpar a lista')
    print('> 5 - Sair do programa')

    # Try e except para tratar erro de valor
    try:
        print(25 * '-')
        escolha = int(input('> Qual opção deseja?: '))
    except ValueError:
        print('> X - Aceitamos apenas números')
        continue

    # if para inserir valores
    if escolha == 1:
        print(45 * '-')
        valor = input('> Qual valor deseja inserir na sua lista?: ').lower().strip()
        compras.append(valor)

    # elif com for para listar itens
    elif escolha == 2:
        if not compras:
            print('> Sua lista está vazia')
        for indice, valor in enumerate(compras):
            print('n°:',indice,'|','->', 'Compra:',valor)

    # elif para apagar itens, com verificações de lista vazia ou índices inválidos
    elif escolha == 3:
        if compras == []:
            print('> Não há valores na sua lista.')
            continue
        else:
            print(35 * '-')
            print('> Aqui está sua lista: ')
    
            for indice, valor in enumerate(compras):
                    print('n°:',indice,'|','->', 'Compra:',valor)
            print(35 * '-')
            try:
                apagar = int(input('> Qual indice deseja apagar na sua lista?: '))
            except ValueError:
                print('> X - Erro, aceitamos apenas números')
                continue
            if apagar < 0 or apagar >= len(compras):
                print('> Indice inexistente... Tente novamente')
                continue
            del compras[apagar]
        
    # elif para limpar a lista
    elif escolha == 4:
        if not compras:
            print('> Não há valores na sua lista.')
            continue
        else:
            print(25 * '-')
            print('> Limpando a sua lista...')
            compras.clear()

    # elif caso o usuário queira sair do programa
    elif escolha == 5:
        print('> Obrigado :D! Saindo do programa...')
        break

    # else para tratar opçoes inválidas. 
    else:
        print('> X - Erro, opção inválida')
