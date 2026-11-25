def exibir_produto(produto):
    print(f"Código: {produto.codigo_produto}")
    print(f"Nome: {produto.nome_produto}")
    print(f"Categoria: {produto.categoria_produto}")
    print(f"Quantidade atual: {produto.quantidade_atual}")
    print(f"Quantidade mínima: {produto.quantidade_minima}")
    if produto.quantidade_atual < produto.quantidade_minima:
        print("Status: Estoque Baixo / Necessidade de Reposição")
    else:
        print("Status: OK")
    print("-" * 30)


def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    print("===== LISTA DE PRODUTOS =====")
    for produto in produtos:
        exibir_produto(produto)


def consultar_produto(produtos):
    from estoque import buscar_produto

    tipo_busca = input("Buscar por: 1 - Código  2 - Nome: ").strip()

    if tipo_busca == "1":
        try:
            codigo = int(input("Código do produto: "))
        except ValueError:
            print("Código inválido")
            return
        posicao = buscar_produto(produtos, codigo)
        if posicao == -1:
            print("Produto não encontrado")
        else:
            exibir_produto(produtos[posicao])
    elif tipo_busca == "2":
        nome = input("Nome do produto: ").strip()
        encontrou = False
        for produto in produtos:
            if produto.nome_produto == nome:
                exibir_produto(produto)
                encontrou = True
        if not encontrou:
            print("Produto não encontrado")
    else:
        print("Opção inválida.")


def relatorio_estoque_baixo(produtos):
    print("===== RELATÓRIO DE ESTOQUE BAIXO =====")
    total_baixo = 0
    for produto in produtos:
        if produto.quantidade_atual < produto.quantidade_minima:
            exibir_produto(produto)
            total_baixo += 1
    if total_baixo == 0:
        print("Nenhum produto com estoque baixo.")
