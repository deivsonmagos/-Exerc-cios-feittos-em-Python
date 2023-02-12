n1 = float(input('Informe á primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print("Sua nota média foi de {}, voçê está, REPROVADO! ".format(media))
elif 5 <= media <= 6.9:
    print('Sua nota média foi de {}, voçê está, em RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Sua nota média foi de {}, PARABÉNS voçê foi APROVADO!'.format(media))

