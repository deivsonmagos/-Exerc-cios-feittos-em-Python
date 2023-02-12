num = int(input('Digite um número interior: '))
print('''Escolha a base para converção :
[ 1 ] Para Binário
[ 2 ] Para Octal
[ 3 ] Para Hexadecimal
''')
selecao = int(input('OPÇÃO: '))
if selecao == 1:
    print('O número {} em converção BINÀRIO séra {}'.format(num, bin(num)[2:]))
elif selecao == 2:
    print('O número {} em converção OCTAL séra {}'.format(num, oct(num)[2:]))
elif selecao == 3:
    print('O número {} em converção HEXADECIMAL séra {}'.format(num, hex(num)[2:]))


