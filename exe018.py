import math
angulo = float(input("Dige um ângulo que vc deseja: "))
seno = math.sin(math.radians(angulo))
print("O ãngulo de {} tem o SENO de {:.2f}.".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O ãngulo de {} tem o COSSENO de {:.2f}.".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))

