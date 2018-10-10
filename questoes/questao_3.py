## QUESTÃO 3 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
# 
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição 
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. 
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg 
#          Saída: trl
#	Entrada: ROT0 c 
#          Saída: c
#	Entrada: ROT26 Cool 
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem 
# deve ser impressa: 'Erro'. 
# Entradas inválidas podem ser entradas que contém códigos de rotações 
# inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', 
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    valid = ['ROT', True]
    key = input()
    value = 0
    keys = key.split()
    tam = len(keys[0])
    i =0
    while i < 5:
        if i < 3:
            if (keys[0][i] == valid[0][i]):
                if (keys[0][3] + keys[0][4]).isdigit() and (value >= 0 and value <= 26):
                    value =  int((keys[0][3] + keys[0][4]))
                if not(keys[0][3] + keys[0][4]).isdigit() and (value >= 0 and value <= 26):
                    print('c eh burro mano')
        else:
            temp = []
            for char in keys[1]:
                temp.append(chr(ord(char) + value))
            key = temp
            for element in temp:
                print("{}".format(element), end='')
        i += 1
    key = input()
    # if key == '':
    #     break
        
    # while valid[1]:
        # value = 0
        # keys = key.split()
        # tam = len(keys[0])
        # while i < 5:
        #     if i < 3:
        #         if (keys[0][i] == valid[0][i]):
        #             if (keys[0][3] + keys[0][4]).isdigit() and (value >= 0 and value <= 26):
        #                 value =  int((keys[0][3] + keys[0][4])
        #             # if not(keys[0][3] + keys[0][4]).isdigit() and (value >= 0 and value <= 26):
        #             #     print('c eh burro mano')
        #     # else:
        #     #     temp = []
        #     #     for char in keys[1]:
        #     #         temp.append(chr(ord(char) + value))
        #     #     key = temp
        #     #     for element in temp:
        #     #         print("{}".format(element), end='')
        # key = input()
        # if key == '':
        #     break
                    

if __name__ == '__main__':
    main()
