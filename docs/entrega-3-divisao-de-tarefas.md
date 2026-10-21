# Entrega 3 - Projeto do Algoritmo: Divisão de Tarefas

**Alunos:**

- Eduardo Santos do Nascimento
- Agnaldo Júnior
- Patrick Silva

## Objetivo da entrega

> Projeto do algoritmo - Desenvolver pseudocódigo, fluxograma e explicar a estratégia utilizada para resolver o problema.

A divisão segue os módulos definidos na [Entrega 2 - Modelagem da solução](entrega-2-modelagem-da-solucao.md). Cada pessoa é dona de um conjunto de módulos e entrega, para eles, o **pseudocódigo** e o **fluxograma**. A **explicação da estratégia** e a consolidação final ficam distribuídas entre os três.

## Resumo da divisão

| Responsável | Módulos | Pseudocódigo | Fluxograma | Parte extra |
|---|---|---|---|---|
| Eduardo | Programa principal (menu), Módulo 5 (CSV), Módulo 1 (Cadastro) | Menu, carregar/salvar CSV, cadastrar produto | Fluxograma geral do sistema (menu) e do cadastro | Estratégia: estrutura de dados e persistência |
| Agnaldo | Módulo 2 (Movimentações) | Buscar produto, registrar entrada, registrar saída | Fluxograma de entrada e de saída (com validação de saldo) | Estratégia: regras de negócio e validações |
| Patrick | Módulo 3 (Consultas) e Módulo 4 (Relatórios) | Listar produtos, consultar produto, relatório de estoque baixo | Fluxograma da consulta e do relatório de estoque baixo | Estratégia: visão geral + consolidação do documento final |

## Convenções combinadas

Para que as partes se encaixem no documento final, todos devem seguir:

- **Pseudocódigo:** estilo Portugol (`ALGORITMO`, `VAR`, `INICIO`, `SE ... ENTAO ... SENAO ... FIMSE`, `PARA ... FACA ... FIMPARA`, `FUNCAO ... RETORNE ... FIMFUNCAO`).
- **Nomes de variáveis:** os mesmos da Entrega 2: `codigo_produto`, `nome_produto`, `categoria_produto`, `quantidade_atual`, `quantidade_minima`, `quantidade_entrada`, `quantidade_saida`.
- **Lista de produtos:** um vetor de registros chamado `produtos`, carregado do CSV no início e salvo no CSV após cada alteração.
- **Fluxograma:** símbolos padrão (oval = início/fim, retângulo = processo, losango = decisão, paralelogramo = entrada/saída). Ferramenta sugerida: draw.io, exportando em PNG para `docs/img/`.
- **Mensagens ao usuário:** usar exatamente os textos da Entrega 2, como "Quantidade insuficiente para esta saída" e "Estoque Baixo / Necessidade de Reposição".

### Funções compartilhadas (contrato entre as partes)

Estas funções são usadas por mais de uma pessoa. A assinatura deve ser respeitada por todos:

| Função | Responsável | Descrição |
|---|---|---|
| `carregar_produtos(): vetor de Produto` | Eduardo | Lê o arquivo CSV e retorna a lista de produtos. |
| `salvar_produtos(produtos)` | Eduardo | Grava a lista inteira no arquivo CSV (uma linha por produto). |
| `buscar_produto(produtos, codigo): inteiro` | Agnaldo | Retorna a posição do produto na lista, ou `-1` se não existir. |
| `exibir_produto(produto)` | Patrick | Mostra os dados de um produto, incluindo o alerta de estoque baixo quando aplicável. |

## Tarefas por pessoa

### Eduardo Santos do Nascimento

- [ ] Pseudocódigo do programa principal (menu com as opções: cadastrar, entrada, saída, listar, consultar, relatório de estoque baixo, sair)
- [ ] Pseudocódigo de `carregar_produtos` e `salvar_produtos` (Módulo 5)
- [ ] Pseudocódigo de `cadastrar_produto` com as validações (código único, campos obrigatórios, valores >= 0, inteiros) (Módulo 1)
- [ ] Fluxograma geral do sistema (menu e chamadas dos módulos)
- [ ] Fluxograma do cadastro de produto
- [ ] Texto da estratégia: por que vetor de registros + CSV, e como os dados são carregados e gravados

### Agnaldo Júnior

- [ ] Pseudocódigo de `buscar_produto` (busca sequencial pelo código)
- [ ] Pseudocódigo de `registrar_entrada` (Regra de Entrada)
- [ ] Pseudocódigo de `registrar_saida` (Regra de Saída + Condição de Validação de Saída)
- [ ] Fluxograma da entrada de produtos
- [ ] Fluxograma da saída de produtos, destacando a decisão `quantidade_saida <= quantidade_atual`
- [ ] Texto da estratégia: como as regras de negócio e restrições evitam estoque negativo e dados inconsistentes

### Patrick Silva

- [ ] Pseudocódigo de `listar_produtos` e `exibir_produto` (Módulo 3)
- [ ] Pseudocódigo de `consultar_produto` por código ou nome (Módulo 3)
- [ ] Pseudocódigo de `relatorio_estoque_baixo` (Condição de Alerta de Estoque Baixo) (Módulo 4)
- [ ] Fluxograma da consulta de produto
- [ ] Fluxograma do relatório de estoque baixo
- [ ] Texto da estratégia: visão geral (divisão em módulos, fluxo de uso do sistema)
- [ ] Consolidar as três partes no documento final `entrega-3-projeto-do-algoritmo.md`

## Estrutura do documento final

O arquivo `docs/entrega-3-projeto-do-algoritmo.md` deve seguir esta ordem:

1. Estratégia utilizada (visão geral, estrutura de dados, regras de negócio)
2. Pseudocódigo
   1. Programa principal
   2. Módulo 5: Leitura e escrita no CSV
   3. Módulo 1: Gestão de Cadastros
   4. Módulo 2: Processamento de Movimentações
   5. Módulo 3: Consultas e Exibição
   6. Módulo 4: Monitoramento e Relatórios
3. Fluxogramas (na mesma ordem dos módulos)

## Acompanhamento

| Etapa | Responsável | Prazo | Status |
|---|---|---|---|
| Revisar e aprovar esta divisão | Todos | A definir | Pendente |
| Pseudocódigos individuais prontos | Cada um | A definir | Pendente |
| Fluxogramas individuais prontos | Cada um | A definir | Pendente |
| Textos de estratégia prontos | Cada um | A definir | Pendente |
| Revisão cruzada (cada um revisa a parte de outro) | Eduardo → Agnaldo, Agnaldo → Patrick, Patrick → Eduardo | A definir | Pendente |
| Consolidação do documento final | Patrick | A definir | Pendente |
| Entrega | Todos | A definir | Pendente |
