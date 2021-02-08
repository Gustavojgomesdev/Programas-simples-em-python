for i in range(0, 10):
    print('PARA SAIR DO PROGRAMA DIGITE [0]!')
    r = str(input('''Você deseja receber dicas para ganhar peso ou perder peso ?
                DIGITE: [A] PARA A PERDA DE PESO:
                DIGITE: [B] PARA GANHAR PESO: ''')).upper()
    if r == 'A':
        print('''Siga as dicas abaixo para você perder peso:
              1° Comer devagar e respeitar a saciedade do corpo. Comer devagar permite que o estômago saciado avise ao cérebro que já recebeu comida suficiente.
              2° Beber mais água durante o dia
              3° Fazer exercícios físicos
              4° Comer de tudo, mas pouca quantidade
              5° Evitar ficar com muita fome''')
    elif r == 'B':
        print('''Siga as dicas abaixo para você ganhar peso:
        1° Aumentar a ingestão de líquidos no dia (mínimo de 2L de água).
        2° Diminuir o intervalo entre as refeições.
        3° Consumir alimentos saudáveis.
        4° Praticar exercícios físicos de quatro a cinco vezes por semana.
        5° Ter um bom período de sono (entre 7 e 8 horas de sono). ''')
    elif r == '0':
        break
    else:
        print('ALTERNATIVA INVÁLIDA')

