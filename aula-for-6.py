vendas = [100, 150, 1500, 2000, 120, 300, 80, 420, 220, 110, 98, 3000]
meta1 = 110
meta2 = 130


for venda in vendas:
    if venda < meta1:
        print("O valor {} é a baixo da meta".format(venda))
        break #irá parar de percorrer a lista quando achar o valor.


print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")

for i in vendas:
    if i > meta2:
        continue
        
    print(i)    