'''Crie um programa onde você informa a idade
das pessoa e ela diga qual foi a maior idade e a menor'''
maior = 0
menor = 0
for i in range(1,6):
    idade=int(input("Idade da {}° pessoa :".format(i)))
    if i == 1:
        maior = i
        menor = i
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
print("A maior idade foi {}".format(maior))
print("A menor idade foi {}".format(menor))