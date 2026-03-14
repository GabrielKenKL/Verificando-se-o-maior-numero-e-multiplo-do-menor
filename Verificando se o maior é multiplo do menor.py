#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.
print("Digite o primeiro número inteiro:")
N1 = int(input())
print("Digite o segundo número inteiro:")
N2 = int(input())

if N1 > N2:
    if N1 % N2 == 0:
        print("O maior número é múltiplo do menor.")
    else:
        print("O maior número não é múltiplo do menor.")

elif N2 > N1:
    if N2 % N1 == 0:
        print("O maior número é múltiplo do menor.")
    else:
        print("O maior número não é múltiplo do menor.")