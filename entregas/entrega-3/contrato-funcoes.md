# Contrato das funções

Assinaturas combinadas na [divisão de tarefas](../../docs/entrega-3-divisao-de-tarefas.md). Quem for implementar deve respeitar nome, parâmetros e retorno, porque o programa principal e os outros módulos já chamam assim.

Todas as funções recebem o mesmo vetor `produtos` (vetor de `Produto`, conforme a Entrega 2). Nenhuma delas grava no CSV: a gravação é feita pelo programa principal com `salvar_produtos`, e só quando a operação retorna `verdadeiro`.

| Função | Responsável | Assinatura | Comportamento |
|---|---|---|---|
| `carregar_produtos` | Eduardo | `carregar_produtos(): vetor de Produto` | Lê o CSV no início do programa. Arquivo inexistente retorna vetor vazio. |
| `salvar_produtos` | Eduardo | `salvar_produtos(produtos)` | Sobrescreve o CSV inteiro, cabeçalho + uma linha por produto. |
| `cadastrar_produto` | Eduardo | `cadastrar_produto(produtos): logico` | Valida e insere. Retorna `falso` se alguma validação falhar. |
| `buscar_produto` | Agnaldo | `buscar_produto(produtos, codigo): inteiro` | Busca sequencial pelo código. Retorna a posição no vetor, ou `-1` se não existir. |
| `registrar_entrada` | Agnaldo | `registrar_entrada(produtos): logico` | Soma a quantidade ao produto. Retorna `verdadeiro` quando aplicou. |
| `registrar_saida` | Agnaldo | `registrar_saida(produtos): logico` | Só subtrai se `quantidade_saida <= quantidade_atual`. Retorna `falso` e exibe "Quantidade insuficiente para esta saída" quando bloqueia. |
| `listar_produtos` | Patrick | `listar_produtos(produtos)` | Percorre o vetor e chama `exibir_produto` para cada item. |
| `consultar_produto` | Patrick | `consultar_produto(produtos)` | Busca por código ou nome e exibe o resultado. |
| `relatorio_estoque_baixo` | Patrick | `relatorio_estoque_baixo(produtos)` | Lista os produtos com `quantidade_atual < quantidade_minima`. |
| `exibir_produto` | Patrick | `exibir_produto(produto)` | Mostra um produto, com o alerta "Estoque Baixo / Necessidade de Reposição" quando aplicável. |

## Pontos de atenção para quem implementar

- **`-1` é o "não encontrado"** de `buscar_produto`. Não usar `0`: a posição 0 não existe no vetor, que é indexado a partir de 1 no pseudocódigo.
- **`logico` controla a gravação.** Se `registrar_entrada`, `registrar_saida` ou `cadastrar_produto` retornarem `falso`, o CSV não pode ser reescrito.
- **`codigo_produto` é inteiro** nesta solução. Códigos como `PROD-001` não são aceitos.
- **Categoria é obrigatória**, além de código e nome.
- **CSV**: separador `;`, sem aspas. Nome e categoria não podem conter `;`.
- **Limite de 100 produtos** (`MAX_PRODUTOS`), coerente com o vetor.

## Regras complementares de validação

Para manter o comportamento igual em todos os módulos:

- `quantidade_atual` e `quantidade_minima` podem ser `0` no cadastro.
- `quantidade_entrada` e `quantidade_saida` devem ser inteiras e maiores que `0`.
- Nenhuma operação pode deixar `quantidade_atual` menor que `0`.
- Uma operação inválida não altera o vetor e não regrava o CSV.
- O alerta de estoque baixo é exibido quando `quantidade_atual < quantidade_minima`.

## Mensagens padronizadas

Quando aplicável, os módulos devem utilizar estas mensagens:

- `Produto cadastrado com sucesso`;
- `Produto não encontrado`;
- `Produto já cadastrado`;
- `Quantidade inválida`;
- `Entrada registrada com sucesso`;
- `Saída registrada com sucesso`;
- `Quantidade insuficiente para esta saída`;
- `Estoque Baixo / Necessidade de Reposição`.

## Fluxo de integração

1. O programa principal chama `carregar_produtos` ao iniciar.
2. O menu chama a função responsável pela operação escolhida.
3. Funções de cadastro e movimentação retornam `verdadeiro` ou `falso`.
4. O programa principal chama `salvar_produtos` somente quando a alteração retorna `verdadeiro`.
5. Funções de consulta e relatório não alteram o vetor nem o arquivo CSV.

## Cenários mínimos de teste

Antes da integração final, devem ser testados:

- cadastro de produto válido;
- tentativa de cadastro com código repetido;
- tentativa de cadastro com campo obrigatório vazio;
- entrada com quantidade válida;
- entrada com quantidade zero ou negativa;
- saída com saldo suficiente;
- saída maior que o saldo disponível;
- consulta de produto existente e inexistente;
- relatório com produto abaixo do estoque mínimo;
- leitura de arquivo inexistente, que deve iniciar com vetor vazio;
- persistência dos dados após salvar e carregar novamente o CSV.
