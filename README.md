# LinearWine
Este repositório contém um projeto de ciência de dados e aprendizado de máquina que utiliza um modelo de regressão linear para prever o teor alcoólico de vinhos com base em seus níveis de açúcar. Usando o conjunto de dados de vinhos da scikit-learn, o modelo busca identificar e visualizar a relação entre essas duas variáveis.

### Objetivo do Projeto
O principal objetivo deste projeto é explorar a relação entre o teor de açúcar e o teor alcoólico em vinhos, construindo um modelo de previsão que, após ser treinado, possa prever o teor alcoólico a partir de um valor de nível de açúcar.

Esse modelo de regressão linear pode ser uma base para estudos mais avançados em análise de vinhos e aplicações em ciência de dados voltadas para o setor de bebidas.

### Funcionalidades
+ Treinamento do Modelo: Um modelo de regressão linear é treinado para encontrar a correlação entre nível de açúcar e teor alcoólico.
+ Previsões: O modelo gera previsões de teor alcoólico para novos valores de nível de açúcar fornecidos pelo usuário.
+ Visualização de Dados: Geração de um gráfico de dispersão para observar a relação entre os dados reais e a linha de regressão criada pelo modelo.

### Dependências
Este projeto utiliza as seguintes bibliotecas Python:

+ matplotlib: Para visualização de gráficos.
+ scikit-learn: Para carregar o conjunto de dados e construir o modelo de regressão linear.

### Para instalar as dependências, execute:
1. pip install matplotlib scikit-learn

### Estrutura do Código
+ Carregamento dos Dados: Os dados de vinho são carregados usando scikit-learn, e as variáveis alvo (teor alcoólico) e característica (nível de açúcar) são definidas.
+ Construção e Treinamento do Modelo: Um modelo de regressão linear é ajustado com base nos dados de treinamento.
+ Previsão e Visualização: O modelo realiza previsões sobre os dados, que são então plotados para mostrar a relação entre nível de açúcar e teor alcoólico.
+ Predição para Novos Dados: É possível fazer uma predição para um novo nível de açúcar fornecido.

### Como Executar
+ Clone o repositório para o seu ambiente local.
+ Navegue até o diretório do projeto.
+ Execute o arquivo Python para treinar o modelo e visualizar os resultados.
1. python nome_do_arquivo.py

### Visualização dos Resultados
O código gera um gráfico com os seguintes elementos:

+ Pontos de Dados (azul): Representam os dados reais do conjunto de dados.
+ Linha de Regressão (vermelho): Representa a previsão do modelo de regressão linear, indicando a relação entre nível de açúcar e teor alcoólico.

### Contribuições
Contribuições para aprimorar o modelo, adicionar novas funcionalidades ou melhorar a visualização dos dados são bem-vindas! Por favor, abra uma issue ou envie um pull request para discutir suas ideias.
