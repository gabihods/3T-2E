nome = input("Nome do Funcionário: ")
salario_input = input("Salário (use . ou , como separador decimal): ")
salario_input = salario_input.replace(",", ".")
try:
    salario = float(salario_input)
except ValueError:
    print("Valor de salário inválido. Execute novamente e digite um número (ex: 2467.50).")
    exit(1)
salario_formatado = f"{salario:.2f}".replace(".", ",")
mes = "setembro"
print(f"O funcionário {nome} tem um salário de R$ {salario_formatado} em {mes}.")
