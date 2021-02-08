'''Faça um programa para quem tem até de 5 carros
e quer saber se ainda tem que pagar o ipva'''
for c in range(1,6):
    carro = int(input("Informe o ano de fabricação de seu carro :"))
    id = 2020 - carro
    print("Seu carro tem {} ano que foi fabricado".format(id))
    for i in range(1):
        if carro < 2000:
            print("Não precisa pagar o IPVA")
        elif carro >2020:
            print("Esse carro não existe")
        else:
            print("Precisa pagar o IPVA")


