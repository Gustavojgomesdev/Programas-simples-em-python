'''programa para criação de login, e o usúario tem uma tentativa
para repetir a mesma senha'''

print('Seja Bem vindo ao nosso programa de criação de login.')

nome =str(input('Crie um nome de usúario: '))
senha =str(input('Crie uma senha: '))
confirmação =str(input('Para a confirmação, digite a sua senha novamente: '))

conte = 0
if confirmação == senha:
    print('Seja Bem-vindo, login efetuado com sucesso! ')
elif confirmação != senha:
    novamente = str(input('Ultima tentativa, digite sua senha novamente: '))
    conte  = conte + 1

    if novamente == senha:
        print('Login efetuado com sucesso! ')
    else:
        print('Senha incoreta, entre em contato com um de nossos suportes!! ')
        conte = conte + 1

print('Número de tentativas {}'.format(conte))
