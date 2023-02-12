casa = float(input('Qualo valor do imovel:R$ '))
salario = float(input('Qual é o valor do salário:R$ '))
anos = int(input('Quantos anos para financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação séra de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')