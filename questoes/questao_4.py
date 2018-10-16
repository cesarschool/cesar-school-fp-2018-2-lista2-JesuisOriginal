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
    janeiro = 31  # 1
    fevereiro = 28  # 2
    marco = 31  # 3
    abril = 30  # 4
    maio = 31  # 5
    junho = 30  # 6
    julho = 31  # 7
    agosto = 31  # 8
    setembro = 30  # 9
    outubro = 31  # 10
    novembro = 30  # 11
    dezembro = 31  # 12
    m31 = "janeiro marco maio julho agosto outubro dezembro"
    day = 0
    month = 0
    year = 0

    def isoddyear(year):
        if year % 4 == 0 and not(year % 100 == 0) and year % 400 == 0:
            return True
        else:
            return False

    date = input()
    i = 0
    ver = 0
    while i < len(date):
        if not date[i] == "/":
            if ver == 0:
                day += date[i]
            elif ver == 1:
                month += date[i]
            elif ver == 2:
                month += date[i]
            else:
                break
        if date[i] == "/":
            ver += 1
    day = int(date)
    month = int(month)
    year = int(year)
    dayn = day + 1
    if (dayn > 28 and month=2 and not isoddyear(year)) or (dayn > 30 and month in m31):
        month += 1
        day = 1
        if month = 12:
            year += 1
    else:
        day += 1
    print("{}/{}/{}".format(day, month, year))


if __name__ == '__main__':
    main()
