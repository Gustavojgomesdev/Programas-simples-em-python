'''programa feito para calcular IMC, o usuario pode escolher a quantidade de
pessoas que ele deseja realizar esse procedimento'''

pessoas =int(input('Digite o número de pessoas que você deseja calcular o seu IMC: '))
for p in range(1, pessoas + 1):
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso / (altura * altura)
    if imc < 18.5:
        print('ABAIXO DO PESO NORMAL!! ')
    elif imc >= 18.5 and imc < 25:
        print('FAIXA DE PESO NORMAL !')
    elif 25 <= imc < 30:
        print('SOBREPESO!!')
    elif 30 <= imc < 40:
        print('OBESIDADE!!')
    else:
        print('MORBIDA!!')

