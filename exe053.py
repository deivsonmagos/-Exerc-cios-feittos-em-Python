frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('Temos um pálindromo!')
else:
    print('A frase digitada não é um pálindromo!')

