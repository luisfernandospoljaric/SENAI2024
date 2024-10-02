# Solicita o valor ganho por hora e o número de horas trabalhadas no mês
valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Número de horas trabalhadas no mês: "))

# Calcula o salário total do mês
salario_total = valor_hora * horas_trabalhadas

# Exibe o salário total
print("\nO total do seu salário no mês é: R$ {:.2f}".format(salario_total))
