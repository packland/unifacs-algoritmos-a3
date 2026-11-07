from dataclasses import dataclass


@dataclass
class Produto:
    codigo_produto: int
    nome_produto: str
    categoria_produto: str
    quantidade_atual: int
    quantidade_minima: int
