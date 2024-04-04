# Especificação de Histogramas

Método utilizado para gerar uma imagem de saída a partir de uma determinada imagem de entrada e um histograma que desejamos que a mesma possua.

O histograma passado como parâmetro pode ser definido de forma manual ou então a partir de uma imagem de referência similar a imagem de entrada mas com melhores condições de iluminação e contraste. Histogramas de imagens arbitrárias com características de coloração e constraste desejadas também podem ser passados como referência para moldar a imagem de saída.

<p align="center">
    <img src="./readmeImg/luna.jpg" width="300px" height="200px">
    <img src="./readmeImg/luna_output.jpg" width="300px" height="200px">
</p>

Veja um exemplo em que a técnica de [especificação de histograma](luna) foi aplicada em uma imagem.

## Definição matemática

A dedução da fórmula da função de transformação responsável pela especificação do histograma se baseia em duas funções de densidade de probabilidade (FDP): $p_r(r)$ e $p_z(z)$.

$r$ denota os níveis de intensidade da imagem de entrada e $z$ os níveis de intensidade da imagem de saída. Assim, $p_r(r)$ e $p_z(z)$ são as funções de probabilidade da imagem de entrada e do resultado esperado da imagem de saída (histograma especificado).

Retomando a definição da fórmula de equalização de histograma, temos:

&nbsp;&nbsp;&nbsp;&nbsp; $s = T(r) = (L - 1) \left(\int_{0}^{r} \ p_r(w)\ dw \right)$

, onde $s$ assume os valores das intensidades da imagem uniforme resultante.

Sendo assim, equalizando também a imagem de referência, podemos definir:

&nbsp;&nbsp;&nbsp;&nbsp; $s = G(z) = (L - 1) \left(\int_{0}^{z} \ p_z(w)\ dw \right)$

, onde $s$ também representa as intensidades da imagem uniforme resultante (equalização de ambos histogramas converge para a mesma função de distribuição de probabilidade). Porém, nesse caso, tem-se a função de transformação $G(z)$, que atua na imagem de referência.

Portanto, como $G(z) = T(r) = s$, $z$ deve satisfazer a seguinte condição:

&nbsp;&nbsp;&nbsp;&nbsp; $z = G^{-1}(s) = G^{-1}[T(r)]$

A forma discreta da função $G(z)$, como visto anteriormente, também resulta em um somatório:

&nbsp;&nbsp;&nbsp;&nbsp; $s_k = T(r_k) = (L - 1) \ \sum ._{j=0}^{k} \ \ p_r(r_j)$

, para $k$ = 0, 1, 2, ... , $L - 1$

&nbsp;&nbsp;&nbsp;&nbsp; $G(z_q) = (L - 1) \ \sum ._{i=0}^{q} \ \ p_z(z_i) = s_k$

, para $q$ = 0, 1, 2, ... , $L - 1$

Assim, o valor desejado de cada pixel da imagem de saída $z_q é dado por$

$z_q = G^{-1}(s_k)$