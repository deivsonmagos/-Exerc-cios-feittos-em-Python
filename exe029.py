velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print("Multado! Voçê excedeu o limite permitido que é de 80Km/h")
    multa = (velocidade - 80) * 7
    print("Voçê deve pagar uma multa de R${:.2f}".format(multa))
print("Tenha um bom dia! Diriga com segurança!")
