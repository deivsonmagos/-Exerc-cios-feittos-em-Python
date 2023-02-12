from random import randint
from time import sleep
computador = randint(0, 5) # sortei um numero
print("=!=" * 20)
print("Vou pensar em um número de 0 á 5, tente adivinhar.... ")
print("=!=" *20)
jogador = int(input("Em que número eu pensei ? ")) # tenta adivinhar
print("PROCESSANDO....>")
sleep(3)
if jogador == computador:
    print("PARABÉNS! Voçê conseguiu me vencer! ")
else:
    print("GANHEI! Eu pensei no número {} e não no número {}!".format(computador, jogador))


