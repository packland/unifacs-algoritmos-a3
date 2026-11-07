from pathlib import Path

from armazenamento import ArmazenamentoCSV
from estoque import Estoque

ARQUIVO_CSV = Path(__file__).resolve().parent.parent / "dados" / "produtos.csv"


def main():
    estoque = Estoque(ArmazenamentoCSV(ARQUIVO_CSV))
    estoque.carregar_produtos()

    while True:
        print("\n===== CONTROLE DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Remover produto")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        match opcao:
            case "0":
                print("Encerrando o sistema...")
                break
            case "1":
                estoque.cadastrar_produto()
            case "2":
                estoque.remover_produto()
            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
