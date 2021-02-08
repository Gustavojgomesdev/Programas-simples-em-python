'''Crie um programa onde uma pessoa ira fazer compras,
se comprar menos que 6 unidades é no preço de varejo,
se mais é no preço de atacado'''
print('Mercadinho do Tiringa')
print('Banana:\nvarejo = 2 reais\natacado = 1 real')
n1=int(input('Quantas Banana você quer comprar ?'))
if n1 < 6:
    nb = n1*2
else:
    nb = n1 *1
print('Abacate:\nvarejo = 5 reais\natacado = 4 reais')
n2=int(input('Quantos Abacate você quer comprar ?'))
if n2 < 6:
    na = n2 * 5
else:
    na = n2 * 4
print('Maçã:\nvarejo = 3 reais\natacado = 1 reais')
n3=int(input('Quantas Maçã você quer comprar ?'))
if n3 < 6:
    nm = n3 * 3
else:
    nm = n3 * 1
print("Você comprou {} Banana, {} Abacate e {} Maçã. No total deu {} reais".format(n1,n2,n3,nb+na+nm))