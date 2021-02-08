'''progrma feito com o objetivo de ajudar grandes comerciantes na hora de comprar mercadorias'''

print('Seja Bem-vindo ao nosso programa de compras de mercadorias')
nome =str(input('Nome do comprador: '))

cont = 0
while True:
    mercadoria = str(input('Digite a mercadoria que você deseja comprar: '))
    quantidade = int(input('Digite a quantidade que você deseja comprar: OBS\nAcima de 5 unidades você irá pagar por atacado! '))

    if quantidade >= 5:
        print('Seu produto irá sair com o preço de atacado')
    cont = cont + 1
    fim = str(input('Você deseja comprar mais alguma coisa ? [S/N]')).upper()

    if fim == 'S':
        print('Boas compras...')
    else:
        print('Você comprou {} mercadoria(s)'.format(cont))
        print('Obrigado por comprar conosco, vá até a parte de pagamentos {}!'.format(nome))
        break



