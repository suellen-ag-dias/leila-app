print ("LEILA APP!")

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
nome_filho = input("Qual o nome do seu filho? ")
idade_filho = input("Qual a idade do seu filho? ")

print(f"Olá, {nome}!")
print("Marque sua necessidade atual:")

print("Para Você:")
print("1 - Consultas Médicas")
print("2 - Tarefas Domésticas")
print("3 - Lembretes")
print("4 - Trabalho")
print("5 - Estudos")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Consultas")
elif opcao =="2":
    print("Tarefas")
elif opcao == "3":
    print('Lembretes')
elif opcao == "4":
    print('Trabalho')
elif opcao == "5":
    print("Estudos")

else:
    print("Escolha uma opção novamente")