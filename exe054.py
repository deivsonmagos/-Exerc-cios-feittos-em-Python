from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    num = int(input('Em que ano a {} pessoa nasceu?  '.format(c)))
    idade = atual - num
    if idade >= 20:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao total tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))
