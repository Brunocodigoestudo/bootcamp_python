# 1) Solicita ao usuário que digite seu nome
usuario = input("Digite seu nome:")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite seu salario:"))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
BONUS_CONSTANTE = 1000

bonus = float(input("Digite seu bônus:"))

# 4) Calcule o valor do bônus final

bonus_final = BONUS_CONSTANTE + salario * bonus

# 5) Imprima cálculo do KPI para o usuário


# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
personalizada = print(f" O {usuario}  recebeu o bonus de:  {bonus_final}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?