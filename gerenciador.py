def add_tarefa(tarefas, nova_tarefa):
    tarefas.append(nova_tarefa)
    print(f'Tarefa "{nova_tarefa}" adicionada com sucesso!')


def marcar_como_concluída(tarefas, indice):
    if indice >= 0 and indice < len(tarefas):
        tarefas[indice] += ' (Concluída)'
        print('Tarefa marcada como concluída!')
    else:
        print('Índice inválido!')


def remover_tarefa(tarefas, indice):
    if indice >= 0 and indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
    else:
        print('Índice inválido!')


def view_tarefas(tarefas):
    print('\nLista de Tarefas:')
    for i, tarefa in enumerate(tarefas):
        print(f'{i + 1}.: {tarefa}')


def main():
    tarefas = []

    while True:
        print('\nMenu:')
        print('1.: Adicionar uma nova tarefa')
        print('2.: Marcar uma tarefa como concluída')
        print('3.: Remover uma tarefa da lista')
        print('4.: Visualizar todas as tarefas')
        print('5.: Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            nova_tarefa = input('Digite a nova tarefa: ')
            add_tarefa(tarefas, nova_tarefa)
        elif escolha == '2':
            view_tarefas(tarefas)
            indice = int(input('Digite o índice da tarefa concluída: ')) - 1
            marcar_como_concluída(tarefas, indice)
        elif escolha == '3':
            view_tarefas(tarefas)
            indice = int(input('Digite a tarefa a ser excluída: ')) - 1
            remover_tarefa(tarefas, indice)
        elif escolha == '4':
            view_tarefas(tarefas)
        elif escolha == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Escolha uma nova opção!')


if __name__ == '__main__':
    main()
