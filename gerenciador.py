import os


def add_tarefa(tarefas, nova_tarefa):
    tarefas.append(nova_tarefa)
    print(f'Tarefa "{nova_tarefa}" adicionada com sucesso!')
    esperar()


def marcar_como_concluída(tarefas, indice):
    if indice >= 0 and indice < len(tarefas):
        tarefas[indice] += ' (Concluída)'
        print('Tarefa marcada como concluída!')
        esperar()
    else:
        print('Índice inválido!')
        esperar()


def remover_tarefa(tarefas, indice):
    if indice >= 0 and indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
        esperar()
    else:
        print('Índice inválido!')
        esperar()


def view_tarefas(tarefas):
    print('\nLista de Tarefas:')
    for i, tarefa in enumerate(tarefas):
        print(f'{i + 1}.: {tarefa}')
    esperar()


def limpar():
    os.system('cls')


def esperar():
    print()
    os.system('pause')


def menu():
    print('GERENCIADOR DE TARFEAS\n')
    print('\nMenu:')
    print('1.: Adicionar uma nova tarefa')
    print('2.: Marcar uma tarefa como concluída')
    print('3.: Remover uma tarefa da lista')
    print('4.: Visualizar todas as tarefas')
    print('5.: Sair\n')


def main():
    tarefas = []

    limpar()

    while True:
        menu()
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            nova_tarefa = input('\nDigite a nova tarefa: ')
            add_tarefa(tarefas, nova_tarefa)
            limpar()
        elif escolha == '2':
            view_tarefas(tarefas)
            indice = int(input('\nDigite o índice da tarefa concluída: ')) - 1
            marcar_como_concluída(tarefas, indice)
            limpar()
        elif escolha == '3':
            view_tarefas(tarefas)
            indice = int(input('\nDigite a tarefa a ser excluída: ')) - 1
            remover_tarefa(tarefas, indice)
            limpar()
        elif escolha == '4':
            view_tarefas(tarefas)
            limpar()
        elif escolha == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Escolha uma nova opção!')


if __name__ == '__main__':
    main()
