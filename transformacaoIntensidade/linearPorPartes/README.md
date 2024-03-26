# Transformação Linear Definida por Partes

Transformação Linear Definida por Partes permite definir a forma da função de intensidade de maneira arbitrariamente complexa.

Largamente aplicada para alongamento de contraste e fatiamento de bits.

## Alongamento de Contraste

Utilizado para aumentar o intervalo dos níveis de cinza da imagem sendo processada.

Podemos definir, por exemplo, dois pontos $(r_1, s_1)$ e $(r_2, s_2)$ que vão definir a forma da função de intensidade. Nesse caso, a função passa a ser definida por 3 funções afins, cada qual com determinado coeficiente de angulação.

Vale ressaltar a importância da seguinte condição ser satisfeita visando respeitar a ordem dos níveis de cinza:

$r_1 \leq r_2$ e $s_1 \leq s_2$

Para funções mais complexas, mais parâmetros devem ser definidos.

<p align="center">
    <img src="./readmeImg/transformacaoPartes.jpg" width="200px" height="200px">
    <img src="./readmeImg/alargamentoConstraste.jpg" width="200px" height="200px">
</p>

Veja um exemplo em que a técnica de [alargamento de contraste](alongamentoContraste) foi aplicada para melhorar a visibilidade de uma imagem.

<p align="center">
    <img src="./readmeImg/pollen.jpg" width="200px" height="200px">
    <img src="./readmeImg/pollen_output.jpg" width="200px" height="200px">
</p>