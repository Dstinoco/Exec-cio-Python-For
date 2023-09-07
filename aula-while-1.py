vendas = input('Cadastre um produto, ou aperte enter para finalizar: ')
produtos = []


while vendas != '':
    produtos.append(vendas)
    vendas = input('Cadastre um produto, ou aperte enter para finalizar: ')
print(produtos)
