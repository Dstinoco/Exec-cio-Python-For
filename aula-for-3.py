quantidade_pessoas = int(input("Quantas pessoas farão Check-in?"))
quarto = {}

for i in range(quantidade_pessoas):
    nome = input('Qual o nome? ')
    cpf = input('Qual o CPF? ')
    hospede = [nome, 'CPF: {}'.format(cpf)]
    quarto.append(hospede)


    print(quarto)

