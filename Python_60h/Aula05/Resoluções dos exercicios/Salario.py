# Solicita os dados de entrada ao usuário
valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcula os descontos
ir = salario_bruto * 0.11  # 11% de Imposto de Renda
inss = salario_bruto * 0.08  # 8% para o INSS
sindicato = salario_bruto * 0.05  # 5% para o Sindicato

# Calcula o salário líquido
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

# Exibe os resultados
print("\nSalário Bruto : R$ {:.2f}".format(salario_bruto))
print("IR (11%) : R$ {:.2f}".format(ir))
print("INSS (8%) : R$ {:.2f}".format(inss))
print("Sindicato (5%) : R$ {:.2f}".format(sindicato))
print("Total de descontos : R$ {:.2f}".format(total_descontos))
print("Salário Líquido : R$ {:.2f}".format(salario_liquido))
