
print('-='*30)
print("        Seja Bem Vindo(a)\n      A calculadora básica      ")
print('-='*30)
n1=0
n2=0
s=0
escolha=0
while True:
    n1=int(input("Digite o 1º número a ser calculado: "))
    n2=int(input("Digite o 1º número a ser calculado: "))
    print("[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir\n[5] Potência")
    escolha=int(input("Oque você Deseja fazer com estes numeros? "))
    if escolha==1:
        s=n1+n2
        print(f"A soma entre {n1} e {n2} vale {s}")
    if escolha==2:
        s=n1-n2
        print(f"A substração entre {n1} e {n2} vale {s}")
    if escolha==3:
        s=n1*n2
        print(f"A multiplicação entre {n1} e {n2} vale {s}")
    if escolha==4:
        s=n1/n2
        print(f"A divisão entre {n1} e {n2} vale {s}")
    if escolha==5:
        s=n1**n2
        print(f"O numero {n1} elevado a {n2} vale {s}")
    E=str(input("Deseja Continuar[S/N]? ")).upper()
    if E in "Nn":
        break
    if E != 'S':
        break
print("-="*30)
print("        Fim Do programa        ")
print("-="*30)