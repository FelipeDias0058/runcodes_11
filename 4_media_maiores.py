    
#Função que determina as variáveis acima da média.
def f_maiores(a, b, c, d, e):

    #Função que determina a média.
    def f_media(a, b, c, d, e):
        return (a + b + c + d + e) / 5
    print(f'{f_media(a, b, c, d, e):.2f}')

    #Condicionais de comparação.
    if a > f_media(a, b, c, d, e):
        print(f'{a:.2f}')
    if b > f_media(a, b, c, d, e):
        print(f'{b:.2f}')
    if c > f_media(a, b, c, d, e):
        print(f'{c:.2f}')
    if d > f_media(a, b, c, d, e):
        print(f'{d:.2f}')
    if e > f_media(a, b, c, d, e):
        print(f'{e:.2f}')
    else:
        raise ValueError("Digite um número.")
        

def main():

    #Entrada de Dados.
    a = float(input(""))
    b = float(input(""))
    c = float(input(""))
    d = float(input(""))
    e = float(input(""))
    
    #Exibição de Dados.
    f_maiores(a, b, c, d, e)
    

if __name__ == '__main__':
    main()
