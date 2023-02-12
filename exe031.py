d = float(input("Qual é a distância da sua viagem? "))
print("Voçê esta prestes a começar uma viagem de {}Km.".format(d))
da = d * 0.50
db = d * 0.45
if d <= 200:
    print("O preço da sua pasagem será de R${:.2f}".format(da))
else:
    print("O preço da sua pasagem será de R${:.2f}".format(db))
