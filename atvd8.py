# Imagine que você está em uma viagem para os Estados Unidos e precisa converter o valor em reais para dólares. Crie um programa que receba o valor em reais e a taxa de câmbio atual, e exiba o valor equivalente em dólares.
real = int(input("valor em reais: "))
dolar = real / 5.64

print(f"o seu valor de {real} reais em dólares é U${dolar:.2f}.")