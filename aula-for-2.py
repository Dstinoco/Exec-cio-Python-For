estoque = [5440, 3307, 3127, 5046, 5061, 9185, 3446, 
2434, 5174, 8517, 4156, 3401, 2592, 4684, 8819, 375, 
425, 211, 135, 592, 441, 870, 43, 359, 220, 822, 401, 454, 40, 833]

bebidas = [
    "Água", "Café", "Chá preto", "Chá verde", "Refrigerante de cola",
    "Suco de laranja", "Suco de maçã", "Suco de uva", "Suco de abacaxi",
    "Suco de manga", "Suco de cranberry", "Leite", "Cerveja", "Vinho tinto",
    "Vinho branco", "Tequila","Mojito", "Margarita", "Martini", "Daiquiri",
    "Coquetel de frutas", "Limonada", "Smoothie de morango", "Smoothie de banana",
    "Iced tea", "Milkshake de chocolate","Milkshake de baunilha",  "Shake de proteína",
    "Água com gás",  "Chá de hortelã"
]


nivel_minimo = 60
lista = []

for indice, quantidade in enumerate(estoque):
    if quantidade < nivel_minimo:
        print(bebidas[indice])
        print('{} está a baixo no nível minimo. Temos apenas {} unidades'.format(bebidas[indice], quantidade))
        
       
       
