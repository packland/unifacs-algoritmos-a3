from produto import Produto

MAX_PRODUTOS = 100


class Estoque:
    def __init__(self, armazenamento):
        self.__armazenamento = armazenamento

    def carregar_produtos(self):
        self.__armazenamento.carregar()

    def cadastrar_produto(self):
        if len(self.__armazenamento.produtos) >= MAX_PRODUTOS:
            print("Limite de produtos atingido")
            return False

        try:
            codigo_produto = int(input("Código do produto: "))
        except (ValueError, EOFError):
            print("Código inválido")
            return False

        if codigo_produto <= 0:
            print("Código inválido")
            return False

        if self.__armazenamento.buscar(codigo_produto) is not None:
            print("Produto já cadastrado")
            return False

        nome_produto = input("Nome do produto: ").strip()
        if not nome_produto or ";" in nome_produto:
            print("Nome do produto inválido")
            return False

        categoria_produto = input("Categoria do produto: ").strip()
        if not categoria_produto or ";" in categoria_produto:
            print("Categoria do produto inválida")
            return False

        try:
            quantidade_atual = int(input("Quantidade inicial: "))
            quantidade_minima = int(input("Quantidade mínima: "))
        except (ValueError, EOFError):
            print("Quantidade inválida")
            return False

        if quantidade_atual < 0 or quantidade_minima < 0:
            print("Quantidade inválida")
            return False

        self.__armazenamento.adicionar(
            Produto(
                codigo_produto=codigo_produto,
                nome_produto=nome_produto,
                categoria_produto=categoria_produto,
                quantidade_atual=quantidade_atual,
                quantidade_minima=quantidade_minima,
            )
        )
        self.__armazenamento.salvar()
        print("Produto cadastrado com sucesso")
        return True

    def remover_produto(self):
        try:
            codigo = int(input("Código do produto: "))
        except (ValueError, EOFError):
            print("Código inválido")
            return False

        produto = self.__armazenamento.buscar(codigo)
        if produto is None:
            print("Produto não encontrado")
            return False

        resposta = input(
            f"Remover {produto.codigo_produto} - {produto.nome_produto}? (s/n): "
        )
        if resposta.strip().lower() != "s":
            print("Operação cancelada")
            return False

        self.__armazenamento.remover(codigo)
        self.__armazenamento.salvar()
        print("Produto removido com sucesso")
        return True
