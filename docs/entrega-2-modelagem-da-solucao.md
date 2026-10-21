# Modelagem da solução

**Alunos:**

- Eduardo Santos do Nascimento
- Agnaldo Júnior
- Patrick Silva

Com base no contexto do Sistema de Controle de Estoque, temos abaixo a modelagem da solução estruturada de acordo com os requisitos solicitados:

## 1. Identificação de Dados e Variáveis

Os dados do sistema consistem na entidade **Produto**, contendo as seguintes variáveis:

- **`codigo_produto`** [chave primária][not null] (Inteiro ou String): Identificador único do produto (Ex: `101`, `PROD-001`).
- **`nome_produto`** [not null] (String): Nome ou descrição do produto (Ex: Teclado Mecânico).
- **`categoria_produto`** [not null] (String): Grupo ao qual o produto pertence (Ex: Periféricos).
- **`quantidade_atual`** [not null] (Inteiro): Quantidade disponível no momento. É inicializada com o valor da "Quantidade inicial" fornecida no cadastro.
- **`quantidade_minima`** (Inteiro ou Real): Ponto de pedido ou limite mínimo de segurança estabelecido pelo usuário.

### 1.1 Persistência dos dados

Vamos persistir num documento CSV com granularidade de uma linha por produto.

## 2. Regras de Negócio e Condições

As regras definem como o sistema processa as informações e toma decisões:

- **Regra de Entrada (Soma):** Ao registrar uma entrada, a fórmula aplicada será:

  ```
  quantidade_atual = quantidade_atual + quantidade_entrada
  ```

- **Regra de Saída (Subtração):** Ao registrar uma saída, a fórmula aplicada será:

  ```
  quantidade_atual = quantidade_atual - quantidade_saida
  ```

- **Condição de Validação de Saída:**
  - **SE** `quantidade_saida <= quantidade_atual` **ENTÃO** a operação é permitida e o estoque é atualizado.
  - **SENÃO**, a operação é bloqueada e o sistema exibe o aviso: "Quantidade insuficiente para esta saída".

- **Condição de Alerta de Estoque Baixo:**
  - **SE** `quantidade_atual < quantidade_minima` **ENTÃO** o sistema sinaliza o produto com o status "Estoque Baixo / Necessidade de Reposição".

## 3. Restrições

Limitações do sistema para garantir a integridade dos dados:

- **Unicidade:** Não é permitido cadastrar dois produtos com o mesmo `codigo_produto`.
- **Valores Positivos:** Nenhuma quantidade informada (inicial, mínima, entrada ou saída) pode ser menor que zero. Não existe estoque negativo.
- **Campos Obrigatórios:** O registro de um produto não pode ser concluído se os campos `codigo_produto` e `nome_produto` estiverem vazios.
- **Tipagem:** Entradas e saídas devem aceitar apenas números inteiros. Nossa plataforma não venderá itens fracionados. Caso deseje, o usuário poderá registrar uma unidade de algo não inteiro. Por exemplo, uma unidade de 250g de algo.

## 4. Divisão do Problema em Partes Menores (Modularização)

Para facilitar o desenvolvimento, o sistema pode ser dividido em 4 módulos principais (funções ou rotinas):

### Módulo 1: Gestão de Cadastros

- Receber os dados de entrada (`codigo`, `nome`, `categoria`, `qtd_inicial`, `qtd_minima`).
- Validar restrições (código único, campos não vazios, valores >= 0).
- Salvar o produto na base de dados/lista.

### Módulo 2: Processamento de Movimentações (Entrada e Saída)

- Buscar produto pelo `codigo_produto`.
- Solicitar o tipo de movimentação (Entrada ou Saída) e a quantidade.
- Aplicar as condições de validação (checar se há saldo suficiente para saídas).
- Efetuar o cálculo de atualização da `quantidade_atual`.
- Retornar mensagem de confirmação ou erro.

### Módulo 3: Consultas e Exibição

- Listar todos os produtos com suas respectivas informações.
- Buscar e exibir os detalhes de um produto específico (filtrando por código ou nome).
- Exibir a situação atualizada após qualquer transação.

### Módulo 4: Monitoramento e Relatórios

- Varrer a lista de produtos cadastrados.
- Comparar `quantidade_atual` com `quantidade_minima` de cada item.
- Gerar e exibir uma lista contendo apenas os itens que precisam de reposição.

### Módulo 5: Leitura e escrita no CSV (Banco de dados)

- CRUD.
