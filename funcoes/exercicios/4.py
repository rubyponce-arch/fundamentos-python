def calcular_media():
    nota1 = float(input('digite o primeiro valor: '))
    nota2 = float(input('digite o segundo valor: '))
    nota3 = float(input('digite o terceiro valor: '))
    media = (nota1 + nota2 + nota3) / 3
    return media

nota_final = calcular_media()
print(f'a nota final é {nota_final}')