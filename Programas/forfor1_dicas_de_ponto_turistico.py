'''programa criado com o objetivo de facilitar a vida de quem está procurando
pontos turisticos pelo Brasil'''

for c in range(1, 6 + 1):
    print('Cite a região que você esteja a procura de pontos turisticos.\nEx: Região Sul')
    print('Para sair do programa digite [0]')
    r = str(input('CITE A REGIÃO: ')).upper()
    if r == '0':
        break
    for i in range(1):

        if r == 'REGIÃO SUL':
            print('''Os três pontos turisticos mais procurados são:
            1° Balneário Camboriú
            2° Cataratas do Iguaçu
            3° Beto Carrero World''')

        elif r == 'REGIÃO CENTRO OESTE':
            print('''Os três pontos turisticos mais procurados são:
            1° Brasília, Distrito Federal
            2° Pirenópolis, Goiás
            3°Parque Nacional da Chapada dos Veadeiros''')

        elif r == 'REGIÃO NORTE':
            print('''Os três pontos turisticos mais procurados são:
            1° Fervedouro, Tocantins
            2° Encontro das Águas, Amazonas
            3° Dunas do Jalapão, Tocantins''')

        elif r == 'REGIÃO NORDESTE':
            print('''Os três pontos turisticos mais procurados são:
            1° Lençóis Maranhenses, Maranhão
            2° Porto de Galinhas
            3° Praia do Sancho, Fernando de Noronha''')

        elif r == 'REGIÃO SUDESTE':
            print('''Os três pontos turisticos mais procurados são:
            1° Praia do Farol, Arraial do cabo, Rio de Janeiro
            2° Janela do céu, Ibitipoca, Minas Gerais
            3° Cristo Redentor, Rio de Janeiro''')

        else:
            print('Essa Região não existe no Brasil...')














