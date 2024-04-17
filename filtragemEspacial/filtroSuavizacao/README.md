# Filtros Espaciais de Suavização

São utilizados para borrar a imagem de entrada, reduzindo detalhes pequenos e fechando pequenos buracos em linhas ou curvas, e também para redução de ruído.

São classificados em dois tipos:

* [Filtros Lineares de Suavização](linear)

* [Filtros Não-lineares de Suavização](naoLinear)

## Remoção de detalhes pequenos

A aplicação mais importante dos filtros de suavização é obter uma representação grosseira dos objetos de interesse.

O tamanho da máscara define o tamanho dos objetos que ficarão em evidência e aqueles que irão se misturar com o fundo. Os elementos que ocupam uma região maior que a máscara serão pouco impactados pela suavização, enquanto aqueles que são menores que a mesma serão muito impactados. Dessa forma, quanto menor a proporção entre a região ocupada pelo objeto e o tamanho da máscara, maior a tendência dele se camuflar com o fundo da imagem.
