# Entrega 3 - Projeto do Algoritmo (parte de Eduardo)

## 1. Estratégia utilizada

O estado do sistema é uma **lista de registros** (`produtos`), mantida em memória durante toda a execução. Cada elemento é um registro do tipo `Produto`, com os campos da Entrega 2. O vetor foi escolhido porque as operações exigidas são simples e o volume de dados é pequeno: percorrer a lista para listar, relatar estoque baixo ou localizar um código é suficiente e não justifica estruturas mais complexas.

O **arquivo CSV** é a persistência. Ele não é lido a cada operação: o fluxo é sempre

1. `carregar_produtos()` uma única vez, na abertura do programa, montando o vetor em memória;
2. todas as consultas e validações trabalham apenas sobre o vetor;
3. `salvar_produtos(produtos)` sobrescreve o arquivo inteiro após cada alteração concluída com sucesso.

Essa ordem evita inconsistência entre memória e disco: o arquivo só é reescrito quando a operação terminou válida, então uma saída bloqueada por saldo insuficiente não altera nada. Como o arquivo inteiro é regravado, não existe risco de duas versões parciais do mesmo produto; o custo é reescrever a lista completa a cada movimentação, aceitável para o tamanho do problema.

Formato adotado (cabeçalho obrigatório, separador `;`, uma linha por produto):

```
codigo_produto;nome_produto;categoria_produto;quantidade_atual;quantidade_minima
101;Teclado Mecanico;Perifericos;25;10
```

## 2. Pseudocódigo

### Tipo de dado

```
TIPO Produto
    codigo_produto: inteiro
    nome_produto: cadeia
    categoria_produto: cadeia
    quantidade_atual: inteiro
    quantidade_minima: inteiro
FIMTIPO

CONSTANTE
    MAX_PRODUTOS = 100
    ARQUIVO_CSV = "produtos.csv"
```

### 2.1 Programa principal

```
ALGORITMO ControleDeEstoque

VAR
    produtos: vetor[1..MAX_PRODUTOS] de Produto
    opcao: inteiro

INICIO
    produtos <- carregar_produtos()

    REPITA
        ESCREVA "===== CONTROLE DE ESTOQUE ====="
        ESCREVA "1 - Cadastrar produto"
        ESCREVA "2 - Registrar entrada"
        ESCREVA "3 - Registrar saida"
        ESCREVA "4 - Listar produtos"
        ESCREVA "5 - Consultar produto"
        ESCREVA "6 - Relatorio de estoque baixo"
        ESCREVA "7 - Sair"
        ESCREVA "Escolha uma opcao: "
        LEIA opcao

        ESCOLHA opcao
            CASO 1
                SE cadastrar_produto(produtos) ENTAO
                    salvar_produtos(produtos)
                FIMSE
            CASO 2
                SE registrar_entrada(produtos) ENTAO
                    salvar_produtos(produtos)
                FIMSE
            CASO 3
                SE registrar_saida(produtos) ENTAO
                    salvar_produtos(produtos)
                FIMSE
            CASO 4
                listar_produtos(produtos)
            CASO 5
                consultar_produto(produtos)
            CASO 6
                relatorio_estoque_baixo(produtos)
            CASO 7
                ESCREVA "Encerrando o sistema..."
            SENAO
                ESCREVA "Opcao invalida. Tente novamente."
        FIMESCOLHA
    ATE opcao = 7
FIMALGORITMO
```

O menu só grava no CSV quando a operação retorna verdadeiro. `cadastrar_produto`, `registrar_entrada` e `registrar_saida` retornam `logico` por esse motivo.

### 2.2 Módulo 5: leitura e escrita no CSV

```
FUNCAO carregar_produtos(): vetor de Produto
VAR
    produtos: vetor[1..MAX_PRODUTOS] de Produto
    linha: cadeia
    campos: vetor de cadeia
    total: inteiro

INICIO
    total <- 0

    SE NAO existe_arquivo(ARQUIVO_CSV) ENTAO
        RETORNE produtos
    FIMSE

    abrir_arquivo(ARQUIVO_CSV, leitura)

    SE NAO fim_arquivo(ARQUIVO_CSV) ENTAO
        LEIA_LINHA(ARQUIVO_CSV, linha)
    FIMSE

    ENQUANTO NAO fim_arquivo(ARQUIVO_CSV) E total < MAX_PRODUTOS FACA
        LEIA_LINHA(ARQUIVO_CSV, linha)
        SE linha <> "" ENTAO
            campos <- dividir(linha, ";")
            total <- total + 1
            produtos[total].codigo_produto    <- inteiro(campos[1])
            produtos[total].nome_produto      <- campos[2]
            produtos[total].categoria_produto <- campos[3]
            produtos[total].quantidade_atual  <- inteiro(campos[4])
            produtos[total].quantidade_minima <- inteiro(campos[5])
        FIMSE
    FIMENQUANTO

    fechar_arquivo(ARQUIVO_CSV)
    RETORNE produtos
FIMFUNCAO
```

```
PROCEDIMENTO salvar_produtos(produtos)
VAR
    i: inteiro

INICIO
    abrir_arquivo(ARQUIVO_CSV, escrita)
    ESCREVA_LINHA(ARQUIVO_CSV, "codigo_produto;nome_produto;categoria_produto;quantidade_atual;quantidade_minima")

    PARA i DE 1 ATE tamanho(produtos) FACA
        ESCREVA_LINHA(ARQUIVO_CSV,
            produtos[i].codigo_produto + ";" +
            produtos[i].nome_produto + ";" +
            produtos[i].categoria_produto + ";" +
            produtos[i].quantidade_atual + ";" +
            produtos[i].quantidade_minima)
    FIMPARA

    fechar_arquivo(ARQUIVO_CSV)
FIMPROCEDIMENTO
```

### 2.3 Módulo 1: cadastro de produto

```
FUNCAO cadastrar_produto(produtos): logico
VAR
    codigo_produto: inteiro
    nome_produto: cadeia
    categoria_produto: cadeia
    quantidade_atual: inteiro
    quantidade_minima: inteiro

INICIO
    SE tamanho(produtos) >= MAX_PRODUTOS ENTAO
        ESCREVA "Limite de produtos atingido."
        RETORNE falso
    FIMSE

    ESCREVA "Codigo do produto: "
    LEIA codigo_produto
    SE codigo_produto <= 0 ENTAO
        ESCREVA "Codigo invalido."
        RETORNE falso
    FIMSE

    SE buscar_produto(produtos, codigo_produto) <> -1 ENTAO
        ESCREVA "Ja existe um produto com este codigo."
        RETORNE falso
    FIMSE

    ESCREVA "Nome do produto: "
    LEIA nome_produto
    SE nome_produto = "" ENTAO
        ESCREVA "O nome do produto e obrigatorio."
        RETORNE falso
    FIMSE

    ESCREVA "Categoria do produto: "
    LEIA categoria_produto
    SE categoria_produto = "" ENTAO
        ESCREVA "A categoria do produto e obrigatoria."
        RETORNE falso
    FIMSE

    ESCREVA "Quantidade inicial: "
    LEIA quantidade_atual
    SE quantidade_atual < 0 ENTAO
        ESCREVA "A quantidade inicial nao pode ser negativa."
        RETORNE falso
    FIMSE

    ESCREVA "Quantidade minima: "
    LEIA quantidade_minima
    SE quantidade_minima < 0 ENTAO
        ESCREVA "A quantidade minima nao pode ser negativa."
        RETORNE falso
    FIMSE

    adicionar(produtos, Produto{codigo_produto, nome_produto, categoria_produto,
                                quantidade_atual, quantidade_minima})
    ESCREVA "Produto cadastrado com sucesso."
    RETORNE verdadeiro
FIMFUNCAO
```

As validações acontecem antes de qualquer escrita: se uma delas falhar, o vetor e o CSV permanecem como estavam. As quantidades são declaradas como `inteiro`, então a própria leitura já recusa valores fracionários; a verificação explícita cobre apenas valores negativos.

O fluxograma do sistema está em `fluxograma.png`.

