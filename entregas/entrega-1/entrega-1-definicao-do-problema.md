# Entrega 1 - Definição do problema

**Alunos:**

- Eduardo Santos do Nascimento
- Agnaldo Júnior
- Patrick Silva

## 1. Contextualização do problema

O controle de estoque é uma atividade essencial para empresas que trabalham com compra, armazenamento e venda de produtos. Quando esse controle é realizado manualmente, por meio de anotações, planilhas não integradas ou registros informais, podem ocorrer erros como divergência entre a quantidade registrada e a quantidade realmente disponível, perda de produtos, dificuldade para identificar itens em falta e demora na atualização das informações.

Diante desse cenário, propõe-se o desenvolvimento de um Sistema de Controle de Estoque, capaz de organizar as principais informações dos produtos e registrar as movimentações realizadas no estoque.

## 2. Problema computacional

O problema consiste em desenvolver um algoritmo capaz de gerenciar os produtos de um estoque e atualizar corretamente suas quantidades a partir das movimentações realizadas.

Para isso, o sistema deverá:

- cadastrar e armazenar produtos;
- localizar produtos a partir de seu identificador;
- registrar entradas e saídas;
- calcular a nova quantidade disponível;
- verificar se uma saída pode ser realizada;
- identificar produtos com estoque baixo.

O sistema deverá impedir operações inconsistentes, principalmente saídas superiores à quantidade disponível, evitando que o estoque apresente valores negativos.

Os dados dos produtos serão armazenados em um arquivo CSV, permitindo que as informações permaneçam disponíveis após o encerramento do programa.

## 3. Importância da solução

A implementação de um sistema de controle de estoque pode tornar o gerenciamento dos produtos mais simples, rápido e seguro. A solução reduz a dependência de controles manuais e facilita a identificação da quantidade disponível de cada item.

Além disso, o sistema poderá ajudar a evitar problemas como falta de mercadorias, registros incorretos e dificuldade para acompanhar as movimentações realizadas.

## 4. Objetivo geral

Desenvolver um sistema computacional para realizar o controle de estoque de produtos, permitindo o cadastro, a consulta e a atualização das quantidades disponíveis por meio do registro de entradas e saídas.

## 5. Objetivos específicos

- Cadastrar produtos no sistema;
- Armazenar informações básicas de cada produto;
- Consultar os produtos cadastrados;
- Registrar a entrada de novas unidades;
- Registrar a saída de unidades;
- Atualizar automaticamente a quantidade disponível;
- Impedir saídas superiores à quantidade existente;
- Permitir a identificação de produtos com estoque baixo;
- Exibir informações atualizadas sobre o estoque.

## 6. Entradas do sistema

As principais informações fornecidas pelo usuário serão:

- Código ou identificador do produto;
- Nome do produto;
- Categoria;
- Quantidade inicial;
- Quantidade de entrada;
- Quantidade de saída;
- Quantidade mínima desejada em estoque.

## 7. Processamento

A partir dos dados fornecidos, o sistema deverá:

1. Ler os produtos armazenados no arquivo CSV;
2. Cadastrar novos produtos;
3. Localizar produtos pelo código;
4. Registrar entradas e atualizar a quantidade disponível;
5. Verificar a disponibilidade antes de registrar uma saída;
6. Registrar saídas e atualizar a quantidade disponível;
7. Identificar produtos com estoque baixo;
8. Gravar as alterações novamente no arquivo CSV.

## 8. Saídas e resultados esperados

O sistema deverá apresentar ao usuário:

- Lista dos produtos cadastrados;
- Quantidade disponível de cada produto;
- Confirmação das entradas realizadas;
- Confirmação das saídas realizadas;
- Aviso quando não houver quantidade suficiente para determinada saída;
- Indicação de produtos com estoque abaixo do mínimo;
- Situação atualizada do estoque após cada movimentação.

## 9. Resultado esperado

Ao final do projeto, espera-se obter um sistema funcional e de fácil utilização, capaz de centralizar as informações do estoque e realizar o controle básico das movimentações de produtos.

A solução deverá proporcionar maior organização, reduzir erros de registro e permitir que o usuário consulte com facilidade quais produtos estão disponíveis e quais precisam de reposição.
