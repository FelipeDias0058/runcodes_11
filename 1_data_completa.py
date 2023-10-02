#Importa a função 'date'.
from datetime import date

#Calcula a idade.
def f_idade(data_atual, data_nasc):
    try:
        aniv = data_nasc.replace(year = data_atual.year)

    #Tratamento de erro para cálculo com anos bissextos.
    except ValueError:
        aniv = data_nasc.replace(year = data_atual.year,
                  month = data_nasc.month + 1, day = 1)
        
    if aniv > data_atual:
        return data_atual.year - data_nasc.year - 1
    else:
        return data_atual.year - data_nasc.year

def main():

    #Entrada/formatação de dados.
    dia = int(input(""))
    mes = int(input(""))
    ano = int(input(""))
    data_atual = date(ano, mes, dia)
    
    nasc_dia = int(input(""))
    nasc_mes = int(input(""))
    nasc_ano = int(input(""))
    data_nasc = date(nasc_ano, nasc_mes, nasc_dia)

    #Saída de Dados
    print(f_idade(data_atual, data_nasc))


if __name__ == '__main__':
    main()


