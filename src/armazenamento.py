import csv
from pathlib import Path

from produto import Produto

CABECALHO = [
    "codigo_produto",
    "nome_produto",
    "categoria_produto",
    "quantidade_atual",
    "quantidade_minima",
]


class ArmazenamentoCSV:
    def __init__(self, caminho):
        self.caminho = Path(caminho)
        self.__produtos = {}

    @property
    def produtos(self):
        # lista dos mesmos objetos, para as funções do contrato que recebem o vetor
        return list(self.__produtos.values())

    def carregar(self):
        self.__produtos = {}
        if not self.caminho.exists():
            return
        with self.caminho.open(encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=";")
            for linha in leitor:
                if not linha.get("codigo_produto"):
                    continue
                produto = Produto(
                    codigo_produto=int(linha["codigo_produto"]),
                    nome_produto=linha["nome_produto"],
                    categoria_produto=linha["categoria_produto"],
                    quantidade_atual=int(linha["quantidade_atual"]),
                    quantidade_minima=int(linha["quantidade_minima"]),
                )
                if produto.codigo_produto in self.__produtos:
                    raise ValueError(
                        f"Código duplicado no CSV: {produto.codigo_produto}"
                    )
                self.__produtos[produto.codigo_produto] = produto

    def salvar(self):
        with self.caminho.open("w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";", lineterminator="\n")
            escritor.writerow(CABECALHO)
            for produto in self.__produtos.values():
                escritor.writerow(
                    [
                        produto.codigo_produto,
                        produto.nome_produto,
                        produto.categoria_produto,
                        produto.quantidade_atual,
                        produto.quantidade_minima,
                    ]
                )

    def buscar(self, codigo):
        return self.__produtos.get(codigo)

    def adicionar(self, produto):
        if produto.codigo_produto in self.__produtos:
            return False
        self.__produtos[produto.codigo_produto] = produto
        return True

    def remover(self, codigo):
        return self.__produtos.pop(codigo, None) is not None
