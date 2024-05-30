# Filtragem no Domínio da Frequência

Os filtros e as técnicas de processamento de imagens abordadas nesse repositório, até então, operavam diretamente sobre as intensidades dos pixels de uma imagem em suas coordenadas $(x, y)$. Assim, essas operações eram denominadas técnicas de **Filtragem no Domínio Espacial**.

Porém, a análise dessas mesmas imagens no domínio da frequência fornece informações valiosas e únicas, as quais são aproveitadas por diversos filtros que operam nesse domínio para produzir algum resultado sobre tais imagens. Essa abordagem é denominada **Filtragem no Domínio da Frequência**. Além disso, diversas operações que são extremamente custosas e complexas de serem realizadas no domínio espacial, se tornam demasiadamente mais simples no domínio da frequência.

No entanto, antes de abordar essas diversas técnicas, primeiramente é necessário introduzir a ferramenta matemática que nos permite converter uma função no domínio real para uma função no domínio da frequência: [**Tranformada de Fourier**](fourier).

<p align="center">
    <img src="./readmeImg/Fourier_Filtering.png" width="560px" height="330px">
</p>