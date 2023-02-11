print('Vamos calcular a sua taxa de metabolismo basal (TBM)')


# Função para validar a entrada de dados numéricos
def validate_input(prompt, error_message):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(error_message)

# Validação de entrada de peso
kg = validate_input("Digite o seu peso (em kg) = ", "Por favor, digite um número válido para o peso.")

# Validação de entrada de altura
cm = validate_input("Digite a sua altura (em cm) = ", "Por favor, digite um número válido para a altura.")

# Validação de entrada de idade
idade = validate_input("Digite a sua idade = ", "Por favor, digite um número válido para idade.")

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
m = validate_input("Digite o tempo do seu TREINO (em minutos) = ", "Por favor, digite um número válido para o tempo de treino.")
print(f'Registrado com sucesso = {m} minutos')

print('=' * 50)

met = input('Escolha a opção da intensidade do seu treino: [01] Média Intensidade / [02] Alta intensidade:  ')

# Validação de entrada de intensidade de treino

while met != '1' and met != '2':
    print('Opção inválida, escolha apenas [01] ou [02].')
    met = input('Escolha a opção da intensidade do seu treino: [01] Média Intensidade / [02] Alta intensidade:  ')

if met == '1':
    atv1 = (6.0 * kg * m) / 60
    print(f'[01]: medida que estima o gasto energético com atividade física é de = {atv1}')
    total = tbm + cad + atv1
    print(f'O seu gasto calórico energético total = {total} ')
else:
    atv2 = (4.5 * kg * m) / 60
    print(f'[02]: medida que estima o gasto energético com atividade física é de = {atv2}')
    total = tbm + cad + atv2
    print('='*50)
    print(f'O seu gasto calórico energético total = {total} ')

print('=' * 50)

opcao = input('Escolha uma opção: [01] Ganhar peso / [02] Perder peso:  ')

# Validação de entrada de ganho ou perca de peso
while opcao != '1' and opcao != '2':
    print('Opção inválida, escolha apenas [01] ou [02].')
    opcao = input('Escolha uma opção: [01] Ganhar peso / [02] Perder peso:  ')

while True:
    try:
        porcento = validate_input("Digite quantos porcentos você deseja perder ou ganhar de peso = ", "Por favor, digite um número.")
        break
    except ValueError:
        print("Por favor, digite um número.")

if opcao == '1':
    aumento_peso = ((porcento/100) * total) + total
    print('=' * 50)
    print(f'Para você aumentar o seu peso você precisa consumir = {aumento_peso:.2f}')
    print('=' * 50)

else:
    perda_peso = total - ((porcento/100) * total)
    print('=' * 50)
    print(f'Para você perder o seu peso você precisa consumir = {perda_peso:.2f}')
    print('=' * 50)
