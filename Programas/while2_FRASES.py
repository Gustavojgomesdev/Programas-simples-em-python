'''Crie um programa onde o usuario informara um numero
e saira uma frase motivacional'''
n1=str(input("Informe seu nome:"))
print("Bem vindo {}".format(n1))
while True:
    n1 = int(input("Digite um numero ate 10, caso queira sair digite [0]:"))
    if n1 == 1:
        print("Os problemas são oportunidades para se mostrar o que sabe.")
    elif n1 == 2:
        print("Nossos fracassos, às vezes, são mais frutíferos do que os êxitos.")
    elif n1 == 3:
        print("É costume de um tolo, quando erra, queixar-se dos outros. É costume de um sábio queixar-se de si mesmo.")
    elif n1 == 4:
        print("Mesmo que já tenhas feito uma longa caminhada, há sempre um novo caminho a fazer.")
    elif n1 == 5:
        print("Experiência é o nome que cada um dá a seus erros.")
    elif n1 == 6:
        print("Seja corajoso. Mesmo que você não seja, finja ser. Ninguém nota a diferença.")
    elif n1 == 7:
        print("Um objetivo nada mais é do que um sonho com limite de tempo.")
    elif n1 == 8:
        print("Grandes mentes estão prontas não apenas para explorar oportunidades, mas para criá-las.")
    elif n1 == 9:
        print("A persistência é o caminho do êxito.")
    elif n1 == 10:
        print("Lute. Acredite. Conquiste. Perca. Deseje. Espere. Alcance. Invada. Caia. Seja tudo o quiser ser, mas acima de tudo, seja você sempre.")
    else:
        break