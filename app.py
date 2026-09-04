# Nome do aparelho
aparelho = input(" Digite o nome do aparelho ")


# Potencia em watts (w)
potencia = float(input(" potencia em watts "))


# tempo de uso em horas
tempo_horas = float(input(" uso em horas "))


# Calculo de consumo mensal
consumo_mensal = (potencia* tempo_horas* 30) / 1000


# Exibindo o resultado
print(f"\nAparelho: {aparelho}")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
