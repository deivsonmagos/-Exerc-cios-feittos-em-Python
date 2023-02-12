print("====== EXE 12 ======")
print("\n")
v = float(input("Digite o valor do produto: "))
vd = v * 5
vp = vd / 100
vt = v - vp


print("O valor final do produto do com desconto é {:.2f}.".format(vt))

print("\n")
vt = v - (v * 5 / 100)
print("O valor com desconto é {:.2f}R$".format(vt))
