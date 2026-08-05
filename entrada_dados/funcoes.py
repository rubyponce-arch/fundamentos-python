def exibir_mensagem():
    print('Hello Word!')

def somar():
    valor1 = 50
    valor2 = 60
    total = valor1 + valor2
    print(f'O resultado da soma é {total}')

def calcular_media():
    nota1 = float(input('digite o primeiro valor: '))
    nota2 = float(input('digite o segundo valor: '))
    media = (nota1 + nota2) / 2
    return media

exibir_mensagem()
somar()

nota_final = calcular_media()
print(f'a nota final é {nota_final}')