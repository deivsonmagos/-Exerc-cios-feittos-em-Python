produto = float(input('Informe o valor do produto: '))
print('''Escolhha a forma de pagamento:
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] NO CARTÃO EM 2x
[ 4 ] NO CARTÃO EM X VEZES
''')
selecao = int(input('OPÇÃO: '))
dinheiro = produto - (produto * 10 / 100)
cartao = produto - (produto * 5 / 100)
cartaoprazo = produto + (produto * 20 / 100)
if selecao == 1:
    print('O valor do produto é de R${:.2f}, pagando À VISTA DINHEIRO/CHEQUE o valor será de R${:.2f}.'.format(produto, dinheiro))
elif selecao == 2:
    print('O valor do produto é de R${:.2f}, pagando À VISTA NO CARTÃO o valor será de R${:.2f}.'.format(produto, cartao))
elif selecao == 3:
    print('Pagando em até 2x no CARTÃO o valor será de R${:.2f} é não terá nem acrecimo nem desconto'.format(produto))
elif selecao == 4:
    print('O valor do produto é de R${:.2f}, efetuando o pagamento em parcelas no CARTÃO o valor será de R${:.2f}'.format(produto, cartaoprazo))

