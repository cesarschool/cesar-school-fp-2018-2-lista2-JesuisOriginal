# #  QUESTÃO 1 # #                                                        
#                                                        
#  Um site exige que os usuários insiram nome de usuário e senha para se registrarem.                                                        
#  Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.                                                       
#  A seguir estão os critérios para verificar a senha:                                                       
#                                                        
#  1. Pelo menos uma letra entre [a-z]                                                       
#  2. Pelo menos 1 número entre [0-9]                                                       
#  3. Pelo menos uma letra entre [A-Z]                                                       
#  4. Pelo menos 1 caractere de [$ #  @]                                                       
#  5. Comprimento mínimo da senha: 6                                                       
#  6. Comprimento máximo da senha: 12                                                       
#                                                        
#  Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará                                                        
#  de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser                                                        
#  impressas, separadas por uma vírgula.                                                       
#  Exemplo                                                       
#  Se as seguintes senhas forem fornecidas como entrada para o programa:                                                       
#  ABd1234@1, umF1# , 2w3E*, 2We3345                                                       
#  Então, a saída do programa deve ser:                                                       
#  ABd1234@1                                                       
# #                                                        

# #                                                        
#  A sua resposta da questão deve ser desenvolvida dentro da função main()!!!                                                        
#  Deve-se substituir o comado # print existente pelo código da solução.                                                       
#  Para a correta execução do programa, a estrutura atual deve ser mantida,                                                       
#  substituindo apenas o comando # print(questão...) existente.                                                       
# #        

import string
import re

def main():
    senha = input('informe a senha \n senha:  ')
    senhas = []
    senhas = senha.split()
    senhas_validas = []
    # print(senhas)
    i = 0
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

    while i < len(senhas):
        # print('i = ', i)
        # print('tamanho da lista ',len(senhas))
        # print('i < len(senhas)', (i < len(senhas)))
        # print('N: {0} element: {1}'.format(i, senhas[i]))
        if (bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', senhas[i]))):
            # print('{} is alphanum'.format(senhas[i]))
            if (len(senhas[i]) >= 6):
                # print('{} is enought'.format(senhas[i]))
                if not(senhas[i].isupper() or senhas[i].islower()):
                    # print('{} is not all upper/lower'.format(senhas[i]))
                    if (regex.search(senhas[i]) != None):
                        # print('has especial')
                        if (len(senhas[i]) <= 12):
                            # print('not too long')
                            senhas_validas.append(senhas[i])
        i += 1
        # print('##############################################################################################')
        # print('                             PROXIMO                                                            ')
        # print('##############################################################################################')

    print(senhas_validas)


if __name__ == '__main__':
    main()
