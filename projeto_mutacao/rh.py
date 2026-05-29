def calcular_bonus(salario: float, anos_servico: int, cargo: str) -> float:
    if anos_servico > 2 and cargo == "DESENVOLVEDOR":
        return salario * 0.15
    return 0.0
