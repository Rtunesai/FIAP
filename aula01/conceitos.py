print('PYcharm')

nome = 'Ricardo'
# str()

idade = 24
# Integer e int()

altura = 1.70
# Real e float()

maior_idade = True
# Boolean e bool()

# type method
valor = 25
print(valor, type(valor))

valor = '25'
print(valor, type(valor))

valor = 45.90
print(valor, type(valor))

valor = False
print(valor, type(valor))

valor1 = "10"
valor1 = int(valor1)
valor2 = "20"
valor2 = int(valor2)

# Concatenation
resposta = valor1 + valor2

print(resposta)


# Format e f string
print('Resposta = {}'. format(resposta))

print(f"valor de resposta: {resposta} ")


# Decimal
a = 56.7

# https://docs.python.org/2/library/string.html#grammar-token-format-spec
# Referencia formatacao

print("RS {:2.2f}". format(a))

print(f'Valor de a = {a}')
print(f'Valor de a = {a:6}')
print(f'Valor de a = {a:06}')

aula = "python".