
#Função que determina a maior variável.
def f_maior(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        return a
    if b > a and b > c and b > d and b > e:
        return b
    if c > a and c > b and c > d and c > e:
        return c
    if d > a and d > b and d > c and d > e:
        return d
    if e > a and e > b and e > c and e > d:
        return e

    
#Função que determina a menor variável.
def f_menor(a, b, c, d, e):
    if a < b and a < c and a < d and a < e:
        return a
    if b < a and b < c and b < d and b < e:
        return b
    if c < a and c < b and c < d and c < e:
        return c
    if d < a and d < b and d < c and d < e:
        return d
    if e < a and e < b and e < c and e < d:
        return e
        

def main():

    print("Digite 5 números.")
    #Entrada de Dados.
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    d = int(input(""))
    e = int(input(""))
    
    #Exibição de Dados.
    print(f'Maior: {f_maior(a, b, c, d, e)}')
    print(f'Menor: {f_menor(a, b, c, d, e)}')

if __name__ == '__main__':
    main()
