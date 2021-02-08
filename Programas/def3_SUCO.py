'''Faça um programa onde a pessoa ira inserir quantos
limões e água colocou e o programa mostre se o suco
esta bom, azedo ou aguado'''
def lim(limão, água):
    if limão > água:
        print("Suco Azedo")
    elif limão == água:
        print("Suco Bom")
    else:
        print("Suco Aguado")
if __name__ == '__main__':
    l = float(input("Quantos limões você colocou ?"))
    a = float(input("Quantos litros de água você colocou ?"))
    v1_return = lim(l,a)