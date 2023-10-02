#Importa a função date
from datetime import date

#A função compara as duas datas, exibindo na tela
#a mais recente.
def f_data_recente(data_1, data_2):
    if data_1 > data_2:
        print(data_1.strftime("%-d/%-m/%Y"))
    elif data_1 < data_2:
        print(data_2.strftime("%-d/%-m/%Y"))
    elif data_1 == data_2:
        print(data_1.strftime("%-d/%-m/%Y"))

def main():

    #Entrada de Dados
    dia = int(input("").strip())
    mes = int(input("").strip())
    ano = int(input("").strip())
    data_1 = date(ano, mes, dia)
    
    dia_2 = int(input("").strip())
    mes_2 = int(input("").strip())
    ano_2 = int(input("").strip())
    data_2 = date(ano_2, mes_2, dia_2)

    #Chama a execução da função.
    f_data_recente(data_1, data_2)


if __name__ == '__main__':
    main()


