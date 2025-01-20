"""Exercício desafio Aula 07.

Desafio: Análise de Vendas de Produtos
Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste
em ler os dados, processá-los em um dicionário para análise e, por fim, calcular e
reportar as vendas totais por categoria de produto.

Tarefas:

- Ler um arquivo CSV e carregar os dados.
- Processar os dados em um dicionário, onde a chave é a categoria, e o valor é uma lista
  de dicionários, cada um contendo informações do produto (Produto, Quantidade, Venda).
- Calcular o total de vendas (Quantidade * Venda) por categoria.
"""

import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, List


def ler_csv(filepath: Path) -> List[Dict[str, str]]:
    """
    Lê um arquivo CSV e retorna uma lista de dict.

    Parameters
    ----------
    filepath : Path
        Caminho do arquivo CSV a ser lido.

    Returns
    -------
    List[Dict[str, str]]
        Lista de dicionários representando as linhas do arquivo CSV, onde cada
        chave é uma coluna.
    """
    with open(filepath, newline="\n") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        dados_lidos: List[Dict[str, str]] = list(leitor)

    return dados_lidos


def processar_dados(
    dados_lidos: List[Dict[str, str]]
) -> Dict[str, List[Dict[str, str | float]]]:
    """
    Processa os dados extraídos do CSV.

    Agrupa os dados por categoria, remove a chave 'Categoria' e
    converte os valores de 'Quantidade' e 'Venda' para float.

    Parameters
    ----------
    dados_lidos : List[Dict[str, str]]
        Lista de dicionários representando as linhas do arquivo CSV, com valores ainda
        como strings.

    Returns
    -------
    Dict[str, List[Dict[str, str | float]]]
        Dicionário onde a chave é a categoria e o valor é uma lista de dicionários
        contendo os produtos da respectiva categoria. Os valores de 'Quantidade' e
        'Venda' são convertidos para float.
    """
    dados_agrupados: Dict[str, List[Dict[str, str | float]]] = defaultdict(list)

    for linha in dados_lidos:
        # Criando uma cópia para evitar modificar a estrutura original
        linha_sem_categoria: Dict[str, str | float] = linha.copy()
        del linha_sem_categoria["Categoria"]  # Removendo a chave "Categoria"

        # Convertendo os valores numéricos
        linha_sem_categoria["Quantidade"] = float(linha_sem_categoria["Quantidade"])
        linha_sem_categoria["Venda"] = float(linha_sem_categoria["Venda"])

        # Adicionando ao dicionário agrupado
        dados_agrupados[linha["Categoria"]].append(linha_sem_categoria)

    return dados_agrupados


def calcular_vendas_categoria(
    dados_agrupados: Dict[str, List[Dict[str, str | float]]]
) -> Dict[str, float]:
    """
    Calcula o total de vendas por categoria.

    Multiplica 'Quantidade' por 'Venda' para cada produto e soma os valores
    dentro de cada categoria.

    Parameters
    ----------
    dados_agrupados : Dict[str, List[Dict[str, str | float]]]
        Dicionário onde a chave é a categoria e o valor é uma lista de dicionários
        contendo informações dos produtos, com 'Quantidade' e 'Venda' já convertidos
        para float.

    Returns
    -------
    Dict[str, float]
        Dicionário onde a chave é a categoria e o valor é o total de vendas dessa
        categoria.
    """
    resultado_total_vendas: Dict[str, float] = {}

    for categoria, vendas in dados_agrupados.items():
        total_vendas: float = sum(
            produto["Quantidade"] * produto["Venda"] for produto in vendas
        )
        resultado_total_vendas[categoria] = total_vendas

    return resultado_total_vendas


if __name__ == "__main__":

    filepath = Path("vendas.csv")

    extracao = ler_csv(filepath)

    processamento = processar_dados(extracao)

    calculo = calcular_vendas_categoria(processamento)
    print(calculo)
