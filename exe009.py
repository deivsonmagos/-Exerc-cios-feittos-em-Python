print("====== EXE 09 ======")
nu = int(input("Digite um número para saber sua tabuada: "))

for i in range(1, 11):
    r = i * nu
    print("{} X {} = {}".format(nu, i, r))
    i = i + 1
print("\n")
# ou
print("-" * 12)
print("{} x {:2} = {}".format(nu, 1, nu*1))
print("{} x {:2} = {}".format(nu, 2, nu*2))
print("{} x {:2} = {}".format(nu, 3, nu*3))
print("{} x {:2} = {}".format(nu, 4, nu*4))
print("{} x {:2} = {}".format(nu, 5, nu*5))
print("{} x {:2} = {}".format(nu, 6, nu*6))
print("{} x {:2} = {}".format(nu, 7, nu*7))
print("{} x {:2} = {}".format(nu, 8, nu*8))
print("{} x {:2} = {}".format(nu, 9, nu*9))
print("{} x {:2} = {}".format(nu, 10, nu*10))
print("-" * 12)



