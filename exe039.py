from datetime import date
nascimento = int(input('Informe o ano de nascimento: '))
ano = date.today().year - nascimento
falta = 18 - ano
passou = ano - 18
if ano <= 16:
    print('Voçê tem {} anos, é ainda vai se alistar, faltam  {} anos!  '.format(ano, falta))
elif ano >= 17 or ano <= 22:
    print('Voçê tem {} anos é ESTÁ na hora do seu alistamento! '.format(ano))
elif ano > 23:
    print('Voçê tem {} anos já se passou {} anos para o alistamento!'.format(ano, passou))
