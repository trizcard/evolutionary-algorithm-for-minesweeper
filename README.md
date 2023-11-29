# Algoritmo Evolutivo para Campo Minado

Este projeto implementa um algoritmo evolutivo para resolver o jogo de Campo Minado. Utiliza conceitos de algoritmos genéticos para evoluir soluções eficazes ao longo do tempo, de maneira didática.

## Autores

- [Beatriz Aimée Teixeira Furtado Braga] (https://github.com/BeatrizAimee)
- [Beatriz Cardoso] (https://github.com/trizcard)

## Pré-requisitos

Antes de iniciar, certifique-se de que você tem Python instalado em sua máquina. Este projeto foi desenvolvido usando Python 3.10.12, mas deve funcionar pelo menos com a versão Python 3.8

## Instalação

Para usar este projeto, siga estas etapas:

1. Clone o repositório:

git clone https://github.com/trizcard/evolutionary-algorithm-for-minesweeper.git

2. Navegue até a pasta do projeto:

cd evolutionary-algorithm-for-minesweeper

3. Garanta que você tenha tkinter instalada, para Debian:

sudo apt-get install python3-tk

## Uso

Para executar o algoritmo, rode o arquivo main.py, em uma IDE ou pelo terminal. 

Isso iniciará o processo evolutivo, onde o algoritmo tentará resolver o jogo de Campo Minado.

- Após iniciar o algorítimo, será criado um arquivo **minesweeper_solver.py**

Ao executar minesweeper_solver.py, será apresentada de maneira gráfica a evolução das jogadas

## Como Funciona

Este projeto aplica algoritmos genéticos da seguinte maneira:

- **Representação do Genoma**: Cada indivíduo na população representa uma possível solução para o jogo, com um genoma consistindo em uma sequência de movimentos.
- **Avaliação de Aptidão**: A aptidão de cada indivíduo é avaliada com base em seu desempenho no jogo.
- **Seleção**: Os indivíduos com melhor desempenho são selecionados para reprodução. (Fitness-Based Selection)
- **Mutação**: Pequenas mutações aleatórias são introduzidas para manter a diversidade genética. (Random Mutation)
- **Nova Geração**: Uma nova geração de indivíduos é criada a partir dos melhores da geração atual, com a introdução de mutações.(Reproduction with Elitism)
- **Crossover**: Dois genomas pais são combinados para criar descendentes (One-point crossover).

## Configurações

É possível mudar as configurações do Campo Minado em **config.py**, vendo o que acontece com o agorítimo evolutivo ao modificar cada parâmetro.

## Contribuições

Contribuições são sempre bem-vindas! Para contribuir, por favor, crie um fork do repositório, faça suas alterações e envie um pull request.






