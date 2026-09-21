print("=== LEILA APP ===")

# Lista de tarefas
# Ela fica fora dos loops para não ser apagada durante a execução.
tarefas = []

# Dados iniciais
nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
nome_filho = input("Qual o nome do seu filho? ")
idade_filho = input("Qual a idade do seu filho? ")

print(f"\nOlá, {nome}!")
print("Marque sua necessidade atual:")


# MENU PRINCIPAL
while True:

    print("\n=== MENU PRINCIPAL ===")
    print("1 - Consultas Médicas")
    print("2 - Tarefas Domésticas")
    print("3 - Lembretes")
    print("4 - Trabalho")
    print("5 - Estudos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")


    # CONSULTAS MÉDICAS
    if opcao == "1":

        print("\n=== CONSULTAS MÉDICAS ===")
        print("Funcionalidade em desenvolvimento.")


    # TAREFAS DOMÉSTICAS
    elif opcao == "2":

        # Menu próprio das tarefas
        while True:

            print("\n=== TAREFAS DOMÉSTICAS ===")
            print("1 - Cadastrar tarefa")
            print("2 - Ver tarefas cadastradas")
            print("0 - Voltar")

            opcao_tarefa = input("Escolha uma opção: ")


            # CADASTRAR TAREFA
            if opcao_tarefa == "1":

                tarefa = input("Digite a tarefa doméstica: ")

                tarefas.append(tarefa)

                print(f"\nTarefa cadastrada com sucesso: {tarefa}")


            # VER TAREFAS
            elif opcao_tarefa == "2":

                if len(tarefas) == 0:

                    print("\nNenhuma tarefa cadastrada.")

                else:

                    print("\n=== SUAS TAREFAS ===")

                    for numero, tarefa in enumerate(tarefas, start=1):

                        print(f"{numero} - {tarefa}")


            # VOLTAR AO MENU PRINCIPAL
            elif opcao_tarefa == "0":

                print("\nVoltando ao menu principal...")

                break


            # OPÇÃO INVÁLIDA
            else:

                print("\nOpção inválida. Tente novamente.")


    # LEMBRETES
    elif opcao == "3":

        print("\n=== LEMBRETES ===")
        print("Funcionalidade em desenvolvimento.")


    # TRABALHO
    elif opcao == "4":

        print("\n=== TRABALHO ===")
        print("Funcionalidade em desenvolvimento.")


    # ESTUDOS
    elif opcao == "5":

        print("\n=== ESTUDOS ===")
        print("Funcionalidade em desenvolvimento.")


    # SAIR DO LEILA
    elif opcao == "0":

        print(f"\nAté logo, {nome}!")
        print("Encerrando o LEILA...")

        break


    # OPÇÃO INVÁLIDA
    else:

        print("\nOpção inválida. Tente novamente.")