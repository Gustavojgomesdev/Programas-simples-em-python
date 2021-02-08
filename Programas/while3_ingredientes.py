'''Crie um programa onde o cliente irá escolher
quanto e ingredientes que ele quer colocar na sua
comida'''
soma = 0
print('Carne = 5 reais cada\nQueijo = 1 real cada\nBacon = 2 reais cada.')
print("Para sair digite [90]")
print("faça seu pedido")
while True:
    n1=int(input("Quer quantas carnes:"))
    if n1 !=90 :
        c1=int(input("Deseja quantos queijo ?"))
        if c1 != 90:
            c2=int(input("Deseja quantos bacon ?"))
            if c2 !=90:
                n9= (n1*5)+(c1*1)+(c2*2)
                soma = n9 + soma
                print("Seu pedido ficou com {} carnes, {} queijo e {} bacon. Custou {} reais, e o total é {} reias. ".format(n1,c1,c2,n9,soma))
    else:
        break



