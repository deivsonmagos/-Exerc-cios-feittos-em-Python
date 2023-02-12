print("====== EXE 15 ======")
km = float(input("Informe a quilometragem rodada: Km "))
dia = int(input("Informe quantidade de dias: "))
da = dia * 60
kmr = km * 0.15
prf = da + kmr
print("O valor total a para ser R${:.2f}.".format(prf))