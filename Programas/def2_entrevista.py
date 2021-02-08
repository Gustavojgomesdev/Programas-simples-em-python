def entrevista (pessoa = '<desconhecido(a)>', empresas=0):

    print(f'O interessado {pessoa} ja trabalhou em {empresas} empresas')

p = str(input('Nome do interessado na vaga de emprego: '))
e = str(input('Número de empresas que ja trabalhou: '))

if e.isnumeric():
    e = int(e)
else:
    e = 0
if p.strip() == '':
    entrevista(empresas=e)
else:
    entrevista(p, e)
