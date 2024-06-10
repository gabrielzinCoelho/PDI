# Filtragem no Domínio da Frequência

Os filtros e as técnicas de processamento de imagens abordadas nesse repositório, até então, operavam diretamente sobre as intensidades dos pixels de uma imagem em suas coordenadas $(x, y)$. Assim, essas operações eram denominadas técnicas de **Filtragem no Domínio Espacial**.

Porém, a análise dessas mesmas imagens no domínio da frequência fornece informações valiosas e únicas, as quais são aproveitadas por diversos filtros que operam nesse domínio para produzir algum resultado sobre tais imagens. Essa abordagem é denominada **Filtragem no Domínio da Frequência**. Além disso, diversas operações que são extremamente custosas e complexas de serem realizadas no domínio espacial, se tornam demasiadamente mais simples no domínio da frequência.

As técnicas de filtragem no domínio da frequência buscam modificar a transformada de Fourier obtida, visando atingir um ojetivo específico, e, então, calcular a transformada inversa para retornar ao domínio espacial.

$g(x, y) = T^{-1}\{H(u, v) . F(u, v)\}$

No entanto, antes de abordar essas diversas técnicas, primeiramente é necessário introduzir a ferramenta matemática que nos permite converter uma função no domínio real para uma função no domínio da frequência: [**Tranformada de Fourier**](fourier).

<p align="center">
    <img src="./readmeImg/Fourier_Filtering.png" width="560px" height="330px">
</p>

## Erro de WrapAround

A Transformada de Fourier, por definição matemática, considera de forma implícita a periodicidade da imagem no domínio da frequência. Isso pode levar a distorções na imagem filtrada obtida se não for tratato de maneira correta. Isso é conhecido como [**Erro de WrapAround**](wraparound) e será mais especificado [aqui](wraparound).

## Filtros no Domínio da Frequência

* [Filtro Passa-Baixa](filtroPassaBaixa)
* [Filtro Passa-Alta](filtroPassaAlta)
