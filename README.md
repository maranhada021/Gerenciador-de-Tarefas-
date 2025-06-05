# Gerenciador de Tarefas Simples (Paradigma Estruturado)

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg) 

Um gerenciador de tarefas em linha de comando desenvolvido em Python, aplicando os princípios do paradigma de programação estruturada. Este projeto foi desenvolvido como parte do trabalho da disciplina de Paradigmas de Linguagem de Programação da Universidade Veiga de Almeida (UVA).

## 📋 Sumário

* [Visão Geral do Projeto](#-visão-geral-do-projeto)
* [Conceitos do Paradigma Estruturado Aplicados](#-conceitos-do-paradigma-estruturado-aplicados)
* [Funcionalidades](#-funcionalidades)
* [Como Executar](#-como-executar)


## 💡 Visão Geral do Projeto

Este é um projeto simples, mas funcional, que permite aos usuários gerenciar suas tarefas diárias diretamente pelo terminal. O foco principal do desenvolvimento foi a aplicação prática dos conceitos de programação estruturada, buscando um código claro, modular e de fácil manutenção.

## 💻 Conceitos do Paradigma Estruturado Aplicados

O projeto foi construído seguindo rigorosamente os pilares do paradigma de programação estruturada:

* **Sequência:** O fluxo de execução das instruções é linear e ordenado, garantindo a lógica de cada operação.
* **Seleção (Estruturas Condicionais):** Utilização extensiva de `if`, `elif` e `else` para controle de fluxo baseado em condições, como validação de entradas e navegação no menu.
* **Iteração (Estruturas de Repetição):** Uso de laços `for` e `while` para processamento de coleções (listar tarefas) e para manter o loop principal do menu ativo.
* **Modularização (Funções):** O código é dividido em funções bem definidas (`adicionar_tarefa`, `listar_tarefa`, `editar_tarefa`, etc.), cada uma com uma responsabilidade única, promovendo a reutilização de código e a clareza.

## ✨ Funcionalidades

* **Adicionar Tarefa:** Incluir uma nova tarefa com descrição, prioridade (Baixa, Média, Alta) e tempo restante em dias.
* **Listar Tarefas:** Exibir todas as tarefas cadastradas com seus status (Concluída/Pendente), prioridade e tempo restante.
* **Concluir Tarefa:** Marcar uma tarefa existente como concluída.
* **Remover Tarefa:** Excluir uma tarefa da lista.
* **Editar Tarefa:** Alterar a descrição de uma tarefa.
* **Definir Prioridade:** Modificar a prioridade de uma tarefa.
* **Editar Tempo Restante:** Atualizar o prazo para conclusão de uma tarefa.

## 🚀 Como Executar

Para executar este projeto em seu ambiente local, siga os passos abaixo:

1.  **Pré-requisitos:**
    * Python 3.x instalado em sua máquina.

2.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)[SeuUsuarioDoGitHub]/[NomeDoSeuRepositorio].git
    ```
    ```bash
    cd [NomeDoSeuRepositorio]
    ```

3.  **Execute o script Python:**
    ```bash
    python gerenciador_tarefas.py
    ```
    (Assumindo que o nome do seu arquivo principal é `gerenciador_tarefas.py`)


