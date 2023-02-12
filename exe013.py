print("====== EXE 13 ======")
sal = float(input("Digite o valor do seu sálario atual: "))
au = 0.15 * sal
sal_final = sal + au
print("Seu sálario final com aumento séra de R${:.2f}. ".format(sal_final))

print("\n")
sal_final = sal + (sal * 15 / 100)
print("Novo sálario é R${:.2f}".format(sal_final))
