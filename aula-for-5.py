meta = 10000
vendas = [
['João', 15000],
['Julia', 27000],
['Marcus', 9900],
['Maria', 3750],
['Ana', 10300],
['Alon', 7870]
]

acima_meta = []

for venda in vendas:
    if venda[1] >= meta:
        acima_meta.append(venda)

print(acima_meta)
print('{:.0%} dos vendedores bateram a meta'.format(len(acima_meta) / len(vendas)))


melhor_vendendor =''
maior_vendas = 0

for i in vendas:
    if i[1] > maior_vendas:
        maior_vendas = i[1]
        melhor_vendendor = i[0]

print('O melhor vendedor foi {} com {} vendas'.format(melhor_vendendor, maior_vendas))        


