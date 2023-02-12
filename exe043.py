peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é de {:.2f}, ATENÇÃO voçê está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.2f}, PARABÉNS voçê está no peso IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.2f} ATENÇÃO voçê está com SOBREPESO!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.2f}, ATENÇÃO voçê está em OBESIDADE!'.format(imc))
else:
    print('Seu IMC é de {:.2f}, ATENÇÃO voçê está em OBESIDADE MÓRBIDA!'.format(imc))
