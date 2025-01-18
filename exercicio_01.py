"""Solução do exercício 01."""

from typing import List

from pydantic import validate_call


@validate_call
def calcular_media(valores: List[float]) -> float:
    """Calcula a média de uma lista de valores."""
    return sum(valores) / len(valores)


if __name__ == "__main__":
    valores = [1, 2, 3, 4, 5]
    media = calcular_media(valores)
    print(media)

    valores = ["a", 2, 3, 4, 5]
    media = calcular_media(valores)
    print(media)
