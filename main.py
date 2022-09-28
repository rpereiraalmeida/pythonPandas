## Arquivo de estudo do livro: "Análise de Dados com Python e Pandas"

import pandas as pd

# Por padrão a função read_csv lerá um arquivo separado por virgula
# nossos dados Gapminder estão separados com tabulações
# podemos usar o parâmetro sep e representar uma tabulação \t
df = pd.read_csv('gapminder.tsv', sep='\t')

# Usamos o método head para que Python nos mostre apenas as 5 primeiras linhas
# print(df.head())

# Obtem o número de linhas e de colunas
# print(df.shape)

# Obtem os nomes das colunas
# print(df.columns)

# Obtem o tipo de cada variável
# print(df.dtypes)

# Obtem mais informações sobre nossos dados
# print(df.info())

# Obtem somente a coluna country e a salva em sua própria variável
country_df = df['country']

# Mostra as 5 primeiras observações
# print(country_df.head())

# Mostra as 5 ultimas observações
# print(country_df.tail())

# Observando country, continent e year
# subset = df[['country', 'continent', 'year']]
# print(subset.head())
# print(subset.tail())

# Obtem a primeira linha
# print(df.loc[0])

# Obtem a centésima linha
# print(df.loc[99])

# Obtem a última linha corretamente
# Usa o primeiro valor dado por shape para obter o numero de linhas
number_of_rows = df.shape[0]

# Subtrai 1 do valor pois queremos o valor do último indice
last_row_index = number_of_rows - 1

# Obtem o subconjunto usando o índice da última linha
# print(df.loc[last_row_index])

# Como alternativa podemos utiliza o método tail para devolver a última linha
# há muitos modos de fazer o que você quer
# print(df.tail(n=1))

# Observe que, quando usamos tail() e loc, os resultados foram exibidos de
# modo diferente. Vamos observar o tipo devolvido para cada metodo.
subset_loc = df.loc[0]
subset_iloc = df.iloc[0]
subset_head = df.head(n=1)

# type usando loc para uma linha
# print(type(subset_loc))

# type usando loc para uma linha
# print(type(subset_iloc))

# type usando head para uma linha
# print(type(subset_head))

# seleciona a primeira, a centesima e a milésima linha
# observe os colchetes duplos, semelhante a sintaxe usada
# para obter subconjuntos com várias colunas
# print(df.loc[[0, 99, 999]])

# obtem a segunda linha usando iloc (usa indice das linhas)
# print(df.iloc[1])

# obtem a centesima linha usando iloc
# print(df.iloc[99])

# com iloc podemos passar -1 para obter a última linha
# algo que não era possível com o loc
# print(df.iloc[-1])

# como antes é possível passar uma lista para obter várias linhas
# print(df.iloc[[0, 99, 999]])

# obtendo um subconjunto de colunas com loc
# observe a posição dos dois-pontos
# ele é usado para selecionar todas as linhas
subset = df.loc[:, ['year', 'pop']]
# print(subset.head())

# obtendo um subconjunto de colunas com iloc
# iloc nos permitirá usar inteiros
# -1 selecionará a última coluna
# subset = df.iloc[:, [2, 4, -1]]
# print(subset.head())

# como range devolve um gerador, é preciso convertê-lo em lista
# cria um intervalo de inteiros de 0 a 4 inclusive
# small_range = list(range(5))
# print(small_range)

# obtem um subconjunto do dataframe usando o intervalo
# subset = df.iloc[:, small_range]
# print(subset.head())

# cria um intervalo de 3 a 5 inclusive
# small_range = list(range(3, 6))
# print(small_range)

# subset = df.iloc[:, small_range]
# print(subset.head())

# A sintaxe de fatiamento de Python, :, é semelhante à sintaxe de range.
# Em vez de usar uma função que especifique os valores de inicio, fim e o passo,
# delimitados por vírgula, separamos os valores com dois-pontos.
# Enquanto a função range pode ser usada para criar um gerador que será convertido
# em uma lista de valores, a sintaxe de fatiamento com dois-pontos só fará sentido
# para fatiar e obter subconjuntos de valores, e não terá nunhum significado próprio
# inerente.
# small_range = list(range(3))
# subset = df.iloc[:, small_range]
# print(subset.head())

# fatia as três primeiras colunas
# subset = df.iloc[:, :3]
# print(subset.head())

# small_range = list(range(3, 6))
# subset = df.iloc[:, small_range]
# print(subset.head())

# fatia as colunas de 3 a 5 inclusive
# subset = df.iloc[:, 3:6]
# print(subset.head())

# small_range = list(range(0, 6, 2))
# subset = df.iloc[:, small_range]
# print(subset.head())

# fatia as cinco primeiras colunas alternadamente
# subset = df.iloc[:, 0:6:2]
# print(subset.head())

# subset = df.iloc[:, 0:6:]
# print(subset.head())

# subset = df.iloc[:, 0::2]
# print(subset.head())

# subset = df.iloc[:, :6:2]
# print(subset.head())

# subset = df.iloc[:, ::2]
# print(subset.head())

# subset = df.iloc[:, ::]
# print(subset.head())

# Temos usado dois-pontos, :, em loc e em iloc à esquerda da vírgula. Quando
# fazemos isso, selecionamos todas as linhas de nosso dataframe. No entanto,
# podemos optar por colocar valores à esquerda da vírgula se quisermos selecionar
# linhas específicas, além de colunas específicas.

# usando loc
# print(df.loc[42, 'country'])

# usando iloc
# print(df.iloc[42, 0])

# Podemos combinar a sintaxe de obtenção de subconjuntos de linhas e de colunas
# com a sintaxe de subconjuntos de várias linhas e várias colunas a fim de obter
# diversas fatias de nossos dados.

# obtem a primeira, a centésima e a milésima linha
# da primeira, quarta e sexta colunas;
# as colunas que esperamos obter são
# country, lifeExp e gdpPercap
# print(df.iloc[[0, 99, 999], [0, 3, 5]])

# se usarmos os nomes das colunas diretamente,
# o código será um pouco mais fácil de ler
# observe que agora temos que usar loc em vez de iloc
# print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

# lembre-se de que podemos usar a sintaxe de fatiamento na parte referente
# às linhas dos atributos loc e iloc
# print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])
