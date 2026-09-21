print("=== LEILA APP ===")

# Armazena as tarefas cadastradas durante a execução
tarefas = []

# Dados iniciais
nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
nome_filho = input("Qual o nome do seu filho? ")
idade_filho = input("Qual a idade do seu filho? ")

print(f"\nOlá, {nome}!")
print("Marque sua necessidade atual:")

# Menu principal
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Consultas Médicas")
    print("2 - Tarefas Domésticas")
    print("3 - Lembretes")
    print("4 - Trabalho")
    print("5 - Estudos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n=== CONSULTAS MÉDICAS ===")
        print("Funcionalidade em desenvolvimento.")

    elif opcao == "2":

        # Menu de tarefas domésticas
        while True:
            print("\n=== TAREFAS DOMÉSTICAS ===")
            print("1 - Cadastrar tarefa")
            print("2 - Ver tarefas cadastradas")
            print("3 - Excluir tarefa")
            print("0 - Voltar")

            opcao_tarefa = input("Escolha uma opção: ")

            # Cadastrar uma nova tarefa
            if opcao_tarefa == "1":
                tarefa = input("Digite a tarefa doméstica: ")
                tarefas.append(tarefa)

                print(f"\nTarefa cadastrada com sucesso: {tarefa}")

            # Mostrar tarefas cadastradas
            elif opcao_tarefa == "2":

                if len(tarefas) == 0:
                    print("\nNenhuma tarefa cadastrada.")

                else:
                    print("\n=== SUAS TAREFAS ===")

                    for numero, tarefa in enumerate(tarefas, start=1):
                        print(f"{numero} - {tarefa}")

            # Excluir uma tarefa
            elif opcao_tarefa == "3":

                if len(tarefas) == 0:
                    print("\nNenhuma tarefa para excluir.")

                else:
                    print("\n=== EXCLUIR TAREFA ===")

                    for numero, tarefa in enumerate(tarefas, start=1):
                        print(f"{numero} - {tarefa}")

                    numero_tarefa = input(
                        "Digite o número da tarefa que deseja excluir: "
                    )

                    # Verifica se o usuário digitou um número
                    if numero_tarefa.isdigit():
                        numero_tarefa = int(numero_tarefa)

                        if 1 <= numero_tarefa <= len(tarefas):
                            tarefa_excluida = tarefas.pop(numero_tarefa - 1)

                            print(
                                f"\nTarefa excluída com sucesso: "
                                f"{tarefa_excluida}"
                            )

                        else:
                            print("\nNúmero de tarefa inválido.")

                    else:
                        print("\nDigite apenas números.")

            # Voltar ao menu principal
            elif opcao_tarefa == "0":
                print("\nVoltando ao menu principal...")
                break

            else:
                print("\nOpção inválida. Tente novamente.")

    elif opcao == "3":
        print("\n=== LEMBRETES ===")
        print("Funcionalidade em desenvolvimento.")

    elif opcao == "4":
        print("\n=== TRABALHO ===")
        print("Funcionalidade em desenvolvimento.")

    elif opcao == "5":
        print("\n=== ESTUDOS ===")
        print("Funcionalidade em desenvolvimento.")

    elif opcao == "0":
        print(f"\nAté logo, {nome}!")
        print("Encerrando o LEILA...")
        break

    else:
        print("\nOpção inválida. Tente novamente.")