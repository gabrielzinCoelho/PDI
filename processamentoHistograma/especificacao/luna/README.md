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

$T(r_k) = s_k = G(z_k)$, onde $r_k$ e $z_k$ são as intensidades da imagem de entrada e de saída, respectivamente, $s_k$ é o valor para qual ambas convergem e $T(r_k)$ e $G(z_k)$ suas relativas funções de transformação. 

Assim, o algorimo busca fazer o seguinte caminho para a construção da imagem de saída:

$r_k \rightarrow T(r_k) \rightarrow s_k \rightarrow G^{-1}(s_k) \rightarrow z_k$

Porém, um ponto que deve ser levado em conta é que a discretização dos níveis de intensidade provoca um pequeno desvio entre os valores $s_k$ resultantes da aplicação de cada função de transformação. Assim, após fazer o mapeamento entre os valores de $r_k$ e $s_k$ e, também, de $z_k$ e $s_k$, o algoritmo busca fazer o mapeamento entre $r_k$ e $z_k$, por meio dos valores $s_k$ que intermediam essa associação. Nesse caso, para cada valor de s_k gerado pela função de transformação $T(r)$, o algoritmo busca assoaciá-lo ao valor de $s_k$ gerado pela função de transformação $G(z)$ mais próximo, e assim fazer o tabelamento entre os valores de intensidade das imagens de entrada e saída.

```
for i in range(256):
    inputValue = i
    eqInputValue = inputEqualization[i]

    while(j < 255 and abs(int(eqInputValue) - int(referenceEqualization[j + 1])) <= abs(int(eqInputValue) - int(referenceEqualization[j]))):
        j+=1
    inputToOutput[inputValue] = j
```

Um aspecto interessante a ser ressaltado é que, como as funções de equalização se tratam de somatórios, o próximo valor da sequência sempre se trata de um valor maior ou igual ao anterior. Baseado nisso, para encontrar os valores de $s_k$ que mais se aproximam, o algoritmo apenas calcula o valor absoluto da diferença entre eles e compara com o valor da diferença calculada utilizando o elemento posterior da sequência, avançando sempre que essa diferença é inferior.

Por fim, os valores de intensidade da imagem de entrada foram substituídos pelos seus respectivos valores apontados pela função de transformação final ($r_k \rightarrow z_k$ ) calculada.