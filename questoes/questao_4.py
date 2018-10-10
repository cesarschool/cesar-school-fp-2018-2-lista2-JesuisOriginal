## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
## Os anos bissextos são múltiplos de 4, não múltiplos de 100 (1900 não é bissexto) e múltiplos de 400 (2000 é bissexto).

def main():
    yb = False
    calendar = {
                'janeiro': [1, 31],
                'fevereiro': [2, 28],
                'marco': [3, 31],
                'abril': [4, 30],
                'maio': [5, 31],
                'junho': [6, 30],
                'julho': [7, 31],
                'agosto': [8, 31],
                'setembro': [9, 30],
                'outubro': [10, 31],
                'novembro': [11, 30],
                'dezembro': [12,31]
                                }
    m31 = {}
    for month in calendar:
        if month[1] = 31:
            m31.update(month)
    datef = { 'day': 0, 'month': 0, 'year': 0}
    def isoddyear(year):
        if year % 4 == 0 and not(year % 100 == 0) and year % 400 == 0:
            return True
        else:
            return False
    date = input
    time = date.split('-')
    for dat in time:
        dat = int(dat)
    datef['year'] = time[0]
    datef['month'] = time[1]
    datef['day'] = time[2]
    if (dadatef['day'] > 28 and datef['month'] = 2 and not isoddyear(datef['year']) ) or (dadatef['day'] > 30 and datef['month'] in m31):
        month += 1
        datef['day'] = 1
        if datef['month'] = 12:
            datef['year'] += 1
    else:
        day += 1
    for now in datef:
        print(now, end='-')

            


if __name__ == '__main__':
    main()
