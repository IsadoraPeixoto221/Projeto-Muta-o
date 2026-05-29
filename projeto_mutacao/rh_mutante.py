def calcular_bonus(salario: float, anos_servico: int, cargo: str) -> float:
    """Calcula o bônus de Natal (15% do salário) para funcionários da TechRobot.

    Regra: bônus de 15% se tempo de casa > 2 anos E cargo == DESENVOLVEDOR.
    Caso contrário, bônus zero.
    """
    if anos_servico >= 2 and cargo == "DESENVOLVEDOR":
        return salario * 0.15
    return 0.0
