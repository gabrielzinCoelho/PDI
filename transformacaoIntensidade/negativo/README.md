# Negativo de Imagens

Utilizado para realçar detalhes em brancos ou cinzas cercados de regiões escuras dominantes em uma imagem.

Observe que o olho humano é mais sensível para detectar detalhes brancos em regiões escuras.

<p align="center">
    <img src="./readmeImg/mamografia.jpg" width="300px" height="200px">
    <img src="./readmeImg/mamografia_output.jpg" width="300px" height="200px">
</p>

É a função inversa da identidade.

<p align="center">
    <img src="./readmeImg/func.jpg" width="300px" height="200px">
</p>


## Detalhes da implementação

Veja a implementação do [algoritmo](negativo.py) responsável por criar o negativo de um exame de mamografia.

Para inverter a escala de cinza da imagem a seguinte função é utilizada:

$s(r) = 255 - r$

Essa transformação converterá pixels claros em escuros e pixels escuros em claros.

<p align="center">
    <img src="./readmeImg/hist_mamografia_input.jpg" width="300px" height="200px">
    <img src="./readmeImg/hist_mamografia_output.jpg" width="300px" height="200px">
</p>
