    
#Função que determina qual o IMC da pessoa.
def f_imc(massa, altura):

    #Função que calcula o IMC.
    def f_inner_imc(massa, altura):
        return massa / (altura ** 2)
    imc = f_inner_imc(massa, altura)
    print(f'{imc:.2f}')

    #Condicionais de comparação.
    if imc <= 18.5:
        print(f'Abaixo do peso')
    elif imc <= 25:
        print(f'Peso normal')
    elif imc <= 30:
        print(f'Sobrepeso')
    elif imc <= 35:
        print(f'Obeso leve')
    elif imc <= 40:
        print(f'Obeso moderado')
    elif imc >= 40:
        print(f'Obeso mórbido')
    else:
        raise ValueError("Digite um número.")
        

def main():

    #Entrada de Dados.
    massa = float(input(""))
    altura = float(input(""))
    
    #Exibição de Dados.
    f_imc(massa, altura)
    

if __name__ == '__main__':
    main()
