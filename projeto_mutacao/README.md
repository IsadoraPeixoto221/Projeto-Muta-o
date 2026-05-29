# teste-mutacao

**Nome:** Isadora de Sousa Peixoto

**Aprendizado:** Cobertura de 100% não garante testes bons; só verificar se o código “roda” deixa passar mutantes. Testes com `assert` nos valores esperados e nos limites (ex.: exatamente 2 anos) ajudam a “matar” o mutante.

## Regra de negócio (TechRobot)

- Bônus = **15% do salário** se **anos > 2** e **cargo == `"DESENVOLVEDOR"`**.
- Caso contrário, bônus = **0**.

## Como rodar

```bash
pip install pytest
pytest test_rh.py -v
```

## Relatório (prints no PDF)

### Print 1 — teste fraco + código sabotado

1. Em `rh.py`, troque `>` por `>=` na linha do `if` (mutante).
2. Rode: `pytest test_rh_fraco.py -v` → deve passar (verde), mostrando que o teste é fraco.

### Print 2 — teste robusto mata o mutante

1. Mantenha o `rh.py` sabotado (`>=`).
2. Rode: `pytest test_rh.py -v` → deve falhar (vermelho).
3. Corrija `rh.py` (`>` de novo) e rode de novo → deve passar.

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `rh.py` | Código de produção (versão correta para o GitHub) |
| `test_rh.py` | Testes robustos (entrega) |
| `test_rh_fraco.py` | Apenas para demonstração no relatório |
