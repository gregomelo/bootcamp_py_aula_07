"""Solução do exercício 01."""

from typing import List, Optional

from pydantic import ValidationError, validate_call


def calcular_media(valores: List[float]) -> Optional[float]:
    """
    Calcula a média aritmética de uma lista de números.

    Parameters
    ----------
    valores : List[float]
        Lista contendo os valores numéricos para o cálculo da média.

    Returns
    -------
    float or None
        Retorna a média dos valores da lista se os dados forem válidos.
        Caso contrário, retorna None e exibe uma mensagem de erro.

    Notes
    -----
    A função `executar` está encapsulada dentro de `calcular_media` e decorada com
    `@validate_call` do Pydantic. Isso é feito para evitar que a função decorada seja
    acessada diretamente pelo usuário, mantendo a interface de uso mais simples e
    controlada. Além disso, essa abordagem garante que a validação ocorra sempre que a
    função principal for chamada, sem expor um método separado.

    Examples
    --------
    >>> calcular_media([1, 2, 3, 4, 5])
    3.0

    >>> calcular_media(["a", 2, 3, 4, 5])
    Erro: valores deve ser uma lista de números.
    None
    """

    @validate_call
    def executar(valores: List[float]) -> float:
        return sum(valores) / len(valores)

    try:
        return executar(valores)
    except ValidationError:
        print("Erro: valores deve ser uma lista de números.")
        return None


if __name__ == "__main__":
    valores = [1, 2, 3, 4, 5]
    print(calcular_media(valores))

    valores = ["a", 2, 3, 4, 5]
    print(calcular_media(valores))
