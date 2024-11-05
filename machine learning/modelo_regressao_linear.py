import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression

# Carregar o conjunto de dados do vinho disponível na biblioteca sklearn
vinho = datasets.load_wine()

# Extrai as informações sobre os vinhos (características e atributos)
dados = vinho.data

# Define a variável alvo (y) como o teor alcoólico do vinho
# O índice 3 representa a coluna com valores de teor alcoólico
alvo = dados[:, 3] 

# Define a variável de entrada (x) como o nível de açúcar
# O índice 10 representa a coluna com valores de nível de açúcar
nivel_acucar = dados[:, 10]  

# Cria um modelo de regressão linear
modelo = LinearRegression()

# Treina o modelo usando o nível de açúcar como variável independente
# e o teor alcoólico como variável dependente
# Reshape é necessário para adaptar o array em uma única coluna
modelo.fit(nivel_acucar.reshape(-1, 1), alvo)  

# Faz previsões de teor alcoólico com base no nível de açúcar
previsoes = modelo.predict(nivel_acucar.reshape(-1, 1))

# Extrai os coeficientes da regressão: coeficiente angular e intercepto
coef_angular = modelo.coef_[0] # Inclinação da reta
coef_linear = modelo.intercept_ # Ponto onde a reta cruza o eixo y

# Exibe os coeficientes do modelo treinado
print("Coeficiente angular (slope):", coef_angular)
print("Coeficiente linear (intercepto):", coef_linear)

# Visualiza a relação entre o nível de açúcar e o teor alcoólico
plt.figure(figsize=(10, 6))
plt.scatter(nivel_acucar, alvo, color='blue', alpha=0.5, label='Dados reais')
plt.plot(nivel_acucar, previsoes, color='red', label='Linha de Regressão', linewidth=2)
plt.xlabel('Nível de Açúcar')
plt.ylabel('Teor Alcoólico')
plt.title('Comparação entre Nível de Açúcar e Teor Alcoólico')
plt.legend()
plt.grid(True)
plt.show()

# Realiza uma predição para um novo valor de nível de açúcar
novo_valor_acucar = [[12]]  # Nível de açúcar a ser testado
predicao_alcool = modelo.predict(novo_valor_acucar)

# Exibe a predição do teor alcoólico para o novo nível de açúcar fornecido
print(f"\nPara um nível de açúcar de {novo_valor_acucar[0][0]}, o teor alcoólico previsto é: {predicao_alcool[0]}")