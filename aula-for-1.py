vendas = [5440, 3307, 3127, 5046, 5061, 9185, 3446, 
2434, 5174, 8517, 4156, 3401, 2592, 4684, 8819, 375, 
425, 211, 135, 592, 441, 870, 43, 359, 220, 822, 401, 454, 40, 833]

meta = 1000

bateu_meta= 0


for venda in vendas:
    if venda >= meta:
        bateu_meta += 1

quant_funcionarios = len(vendas)

percentual_bateu_meta = bateu_meta / quant_funcionarios

print('Quantidade de funcionários que bateram a meta é: {:.2%}'.format(percentual_bateu_meta))

