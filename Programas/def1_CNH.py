'''programa que retorna uma função com o objetivo de dizer se tal pessoa
que nasceu em tal ano está apta para tirar a sua CNH'''
def maior(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade > 18:
        return f'Você possui {idade} anos, está apto para tirara a sua CNH!'
    else:
        return f'Você possui {idade} anos, não está apto para tirar a sua CNH'
print(maior(2001))
