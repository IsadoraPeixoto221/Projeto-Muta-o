from rh import calcular_bonus


def test_desenvolvedor_mais_de_dois_anos_recebe_bonus():
    assert calcular_bonus(1000, 3, "DESENVOLVEDOR") == 150.0


def test_desenvolvedor_exatamente_dois_anos_nao_recebe_bonus():
    assert calcular_bonus(1000, 2, "DESENVOLVEDOR") == 0.0


def test_desenvolvedor_menos_de_dois_anos_nao_recebe_bonus():
    assert calcular_bonus(1000, 1, "DESENVOLVEDOR") == 0.0


def test_outro_cargo_com_muito_tempo_nao_recebe_bonus():
    assert calcular_bonus(1000, 10, "ANALISTA") == 0.0


def test_desenvolvedor_cargo_diferente_nao_recebe_bonus():
    assert calcular_bonus(2000, 5, "desenvolvedor") == 0.0


def test_salario_zero_bonus_zero():
    assert calcular_bonus(0, 5, "DESENVOLVEDOR") == 0.0
