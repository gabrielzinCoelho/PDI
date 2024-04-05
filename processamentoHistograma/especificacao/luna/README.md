# Exemplo de Especificação de Histograma: Luna

Especificação de histograma é muito útil quando uma determinada imagem apresenta condições de iluminação e/ou outros fatores desfavoráveis e se tem uma imagem de referência, que retrata o mesmo ambiente e elementos, ou similares, porém com características mais propícias.

Especialmente quando se trata de imagens com características intrínsecas de menor contraste, imagens naturalmente mais claras ou escuras, a correção por meio de equalização do histograma pode afetar esse aspecto natural de menor contraste relacionado à imagem e distorcer sua coloração. Dessa forma, a especificação de histograma se torna uma opção atraente para a correção dessas condições da imagem original preservando sua essência.

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

Veja a implementação do algoritmo responsável por aplicar a [especificação do histograma](especificacao.py) nesse exemplo.

Inicialmente, são calculados os histogramas normalizados (ou funções de probabilidade) da imagem de entrada e, também, da imagem de referência. A partir dessas funções de probabilidade, são obtidas as funções de transformação para a equalização de ambos histogramas.

Como abordado, em um mundo contínuo a equalização da imagem de entrada e da imagem de referência tendem a convergir para uma mesma função de distribuição de probabilidade. Assim, a ideia por trás do algoritmo é determinar os valores de intensidade de cada pixel da imagem de saída através de dois passos: 

* Primeiro, aplicando a função de transformação à imagem de entrada e obtendo seus respectivos valores equalizados.

* E segundo, a partir de tais valores equalizados obter por meio da inversa da função de transformação da equalização do histograma especificado, os valores correspondentes de saída.

Tal sequência de passos pode ser melhor entendida pelas seguintes igualdades:

$T(r_k) = s_k = G(z_k)$, onde $r_k$ e $z_k$ são as intensidades da imagem de entrada e de saída, respectivamente, e $s_k$ é o valor para qual ambas convergem.

Assim, o algorimo busca fazer o seguinte caminho:

$r \rightarrow T(r_k) \rightarrow s_k \rightarrow G_{-1}(s_k) \rightarrow z_k$