print('Vamos calcular a sua taxa de metabolismo basal (TBM)')

# Validação de entrada de peso
while True:
    try:
        kg = float(input('Digite o seu peso = '))
        break
    except ValueError:
        print("Por favor, digite um número válido para o peso.")

# Validação de entrada de altura
while True:
    try:
        cm = float(input('Digite a sua altura = '))
        break
    except ValueError:
        print("Por favor, digite um número válido para a altura.")

# Validação de entrada de idade
while True:
    try:
        idade = int(input('Digite a sua idade = '))
        break
    except ValueError:
        print("Por favor, digite um número válido para a idade.")

# Validação de entrada de sexo
while True:
    s = input('Digite a sua sexualidade [M ou F] = ').lower()
    if s == 'm':
        tbm = 66 + (13.7 * kg) + (5.0 * cm) - (6.8 * idade)
        print(f'[MASCULINO]: Seu gasto calórico basal diário é = {tbm:.2f}')
        break
    elif s == 'f':
        tbm = 665 + (9.6 * kg) + (1.8 * cm) - (4.7 * idade)
        print(f'[FEMININO]: Seu gasto calórico basal diário é = {tbm:.2f}')
        break
    else:
        print("Por favor, digite 'M' para masculino ou 'F' para feminino.")

print('=' * 50)

# Validação de entrada de calorias consumidas com atividades diárias
while True:
    try:
        cad = float(input('Digite o seu consumo de calorias com atividades diárias = '))
        break
    except ValueError:
        print("Por favor, digite um número válido para o consumo de calorias.")
print(f'Registrado com sucesso = {cad}')

print('=' * 50)

# Validação de entrada de tempo de treino
while True:
    try:
        m = float(input('Digite o tempo do seu TREINO (MINUTOS) = '))
        break
    except ValueError:
        print("Por favor, digite um número válido para o tempo de treino.")
print(f'Registrado com sucesso = {m}')

print('=' * 50)

met = input('Escolha a opção da intensidade do seu treino. Média [01] ou Alta intensidade [02]:  ')

while met != '1' and met != '2':
    met = input('Opção inválida. Escolha a opção da intensidade do seu treino. Média [01] ou Alta intensidade [02]:  ')

if met == '1':
    atv1 = (6.0 * kg * m) / 60
    print(f'[01]: medida que estima o gasto energético com atividade física é de = {atv1}')
    total = tbm + cad + atv1
    print(f'O seu gasto calórico energético total = {total} ')
else:
    atv2 = (4.5 * kg * m) / 60
    print(f'[02]: medida que estima o gasto energético com atividade física é de = {atv2}')
    total = tbm + cad + atv2
    print(f'O seu gasto calórico energético total = {total} ')

