"""Teste fraco (falsa segurança) — use apenas para o print 1 do relatório."""

from rh import calcular_bonus


def test_calcular_bonus_executa_sem_erro():
    calcular_bonus(1000, 3, "DESENVOLVEDOR")
