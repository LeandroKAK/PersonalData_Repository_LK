salary = float(input("Insira o salário: "))

# função do cálculo do imposto
def calculoImposto(salary): 
    imposto = 0
# x é uma variável para auxilio no cálculo para não alterar o valor do salário
    x = salary
    if salary > 4500:
        x -= 4500
        imposto += (x * 28/100)
    x = salary
    if salary > 3000:
        x -= 3000
        imposto += (x * 18/100)
    x = salary
    if salary > 2000:
        x -= 2000
        imposto += (x * 8/100)
    return imposto

# Chamar a função para encontrrar o imposto
if salary < 2000 and salary > 0:
    print('Isento')
elif salary > 2000:
    print(f'Seu imposto será R$ {calculoImposto(salary):.2f}')
else:
    print("Salário inválido")