# Exemplo de Especificação de Histograma - Luna

Especificação de histograma é muito útil quando uma determinada imagem apresenta condições de iluminação e/ou outros fatores desfavoráveis e se tem uma imagem de referência, que retrata o mesmo ambiente e elementos, ou similares, porém com características mais propícias.

Especialmente quando se trata de imagens com características intrínsecas de menor contraste, imagens naturalmente mais claras ou escuras, a correção por meio de equalização do histograma pode afetar esse aspecto natural de contraste relacionado à imagem e distorcer sua coloração. Dessa forma, a especificação de histograma se torna uma opção atraente para a correção dessas condições da imagem original preservando sua essência.

Observe, abaixo, o resultado da equalização, onde é mostrado a imagem original, a imagem de referência, de onde se obteve o histograma especificado, e a imagem de saída obtida, que, por sinal, se aproxima muito da imagem passada como parâmetro.

<p align="center">
    <img src="../readmeImg/luna.jpg" width="300px" height="200px">
    <img src="../readmeImg/lunaReferencia.jpg" width="300px" height="200px">
    <img src="../readmeImg/luna_output.jpg" width="300px" height="200px">
</p>

Segue, também, a função de equalização da imagem de referência e sua inversa, colocadas em contraposição no mesmo gráfico e destacadas pela função identidade (eixo de simetria), e, além disso, a função de transformação que, a partir dos valores de intensidade da imagem de entrada, determina os valores presentes na imagem de saída.

<p align="center">
    <img src="./readmeImg/funcao_inversa.jpg" width="300px" height="200px">
    <img src="./readmeImg/funcao_transformacao.jpg" width="300px" height="200px">
</p>

O resultado obtido pelo algoritmo pode ser visto de maneira mais clara comparando os histogramas gerados:

<p align="center">
    <img src="./readmeImg/histogramas.jpg" width="400px" height="200px">
    <img src="./readmeImg/histogramas_juntos.jpg" width="400px" height="200px">
</p>

## Detalhes da implementação