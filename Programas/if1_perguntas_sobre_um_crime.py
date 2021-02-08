'''programa feito para uma invetigação criminal'''

print('Nós iremos fazer 5 perguntas para você, e com base nessas perguntas iremos analizar e ver qual foi a sua participação no crime.')
print("Você só poderá responder com 'SIM' ou 'NÃO!' ")
print(' DIGITE [S] PARA SIM\n DIGITE [N] PARA NÃO.')

contc = 0
conte = 0

p1 = str(input('Você telefonou para a vitíma ? ')).upper()
if p1 == 'S':
    print('Iremos seguir para a próxima pergunta...')
    contc = contc + 1
else:
    print('Iremos seguir para a próxima pergunta...')
    conte = conte + 1

p2 = str(input('Esteve no local do crime ? ')).upper()
if p2 == 'S':
    print('Iremos seguir para a próxima pergunta...')
    contc = contc + 1
else:
    print('Iremos seguir para a próxima pergunta...')
    conte = conte + 1

p3 = str(input('Mora perto da vítima ? ')).upper()
if p3 == 'S':
    print('Iremos seguir para a próxima pergunta...')
    contc = contc + 1
else:
    print('Iremos seguir para a próxima pergunta...')
    conte = conte + 1

p4 = str(input('Devia para a vítima ? ')).upper()
if p4 == 'S':
    print('Iremos seguir para a próxima pergunta...')
    contc = contc + 1
else:
    print('Iremos seguir para a próxima pergunta...')
    conte = conte + 1

p5 =str(input('Já trabalhou para a vítima ? ')).upper()
if p5 == 'S':
    contc = contc + 1
else:
    conte = conte + 1

if contc == 1:
    print('Você foi classficado(a) como SUSPEITO(A)')
elif contc == 2:
    print('Você foi classficado(a) como SUSPEITO(A)')
elif contc == 3:
    print('Você foi classficado(a) como CÚMPLICE')
elif contc ==4:
    print('Você foi classficado(a) como CÚMPLICE')
elif contc == 5:
    print('Você foi classficado(a) como ASSASINO(A)')
