print("=== LEILA APP ===")

# Listas do aplicativo
tarefas = []
consultas = []
lembretes = []

# Dados iniciais
nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
nome_filho = input("Qual o nome do seu filho? ")
idade_filho = input("Qual a idade do seu filho? ")

print()
print(f"Olá, {nome}! Seja bem-vinda ao LEILA.")
print(f"Vamos ajudar você a organizar sua rotina com {nome_filho}.")
print()


# Menu principal
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Tarefas")
    print("2 - Consultas")
    print("3 - Lembretes")
    print("4 - Trabalho")
    print("5 - Estudos")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # TAREFAS
    if opcao == "1":
        while True:
            print("\n=== TAREFAS ===")
            print("1 - Adicionar tarefa")
            print("2 - Ver tarefas")
            print("0 - Voltar")

            opcao_tarefa = input("\nEscolha uma opção: ")

            if opcao_tarefa == "1":
                nova_tarefa = input("Digite a nova tarefa: ")
                tarefas.append(nova_tarefa)

                print("Tarefa adicionada com sucesso!")

            elif opcao_tarefa == "2":
                print("\n=== SUAS TAREFAS ===")

                if len(tarefas) == 0:
                    print("Nenhuma tarefa cadastrada.")

                else:
                    for numero, tarefa in enumerate(tarefas, start=1):
                        print(f"{numero} - {tarefa}")

            elif opcao_tarefa == "0":
                break

            else:
                print("Opção inválida.")


    # CONSULTAS
    elif opcao == "2":
        while True:
            print("\n=== CONSULTAS ===")
            print("1 - Adicionar consulta")
            print("2 - Ver consultas")
            print("0 - Voltar")

            opcao_consulta = input("\nEscolha uma opção: ")

            if opcao_consulta == "1":
                especialidade = input("Digite a especialidade: ")
                medico = input("Digite o nome do médico: ")
                data = input("Digite a data da consulta: ")
                horario = input("Digite o horário da consulta: ")
                local = input("Digite o local da consulta: ")

                consulta = {
                    "especialidade": especialidade,
                    "medico": medico,
                    "data": data,
                    "horario": horario,
                    "local": local
                }

                consultas.append(consulta)

                print("Consulta adicionada com sucesso!")

            elif opcao_consulta == "2":
                print("\n=== SUAS CONSULTAS ===")

                if len(consultas) == 0:
                    print("Nenhuma consulta cadastrada.")

                else:
                    for numero, consulta in enumerate(consultas, start=1):
                        print(f"\nConsulta {numero}")
                        print(f"Especialidade: {consulta['especialidade']}")
                        print(f"Médico: {consulta['medico']}")
                        print(f"Data: {consulta['data']}")
                        print(f"Horário: {consulta['horario']}")
                        print(f"Local: {consulta['local']}")

            elif opcao_consulta == "0":
                break

            else:
                print("Opção inválida.")


    # LEMBRETES
    elif opcao == "3":
        while True:
            print("\n=== LEMBRETES ===")
            print("1 - Adicionar lembrete")
            print("2 - Ver lembretes")
            print("0 - Voltar")

            opcao_lembrete = input("\nEscolha uma opção: ")

            if opcao_lembrete == "1":
                descricao = input("Digite o lembrete: ")
                data = input("Digite a data: ")
                horario = input("Digite o horário: ")

                lembrete = {
                    "descricao": descricao,
                    "data": data,
                    "horario": horario
                }

                lembretes.append(lembrete)

                print("Lembrete adicionado com sucesso!")

            elif opcao_lembrete == "2":
                print("\n=== SEUS LEMBRETES ===")

                if len(lembretes) == 0:
                    print("Nenhum lembrete cadastrado.")

                else:
                    for numero, lembrete in enumerate(lembretes, start=1):
                        print(f"\nLembrete {numero}")
                        print(f"Descrição: {lembrete['descricao']}")
                        print(f"Data: {lembrete['data']}")
                        print(f"Horário: {lembrete['horario']}")

            elif opcao_lembrete == "0":
                break

            else:
                print("Opção inválida.")


    # TRABALHO
    elif opcao == "4":
        print("\n=== TRABALHO ===")
        print("Essa função ainda está em desenvolvimento.")


    # ESTUDOS
    elif opcao == "5":
        print("\n=== ESTUDOS ===")
        print("Essa função ainda está em desenvolvimento.")


    # SAIR
    elif opcao == "0":
        print("\nAté logo!")
        print("LEILA encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")