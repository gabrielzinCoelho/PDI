# Filtro Laplaciano

Utiliza as derivadas de segunda ordem para realçar transições de intensidade.

O filtro Laplaciano é linear (pode ser representado em uma máscara de filtragem linear).

## Definição Matemática

O Filtro Laplaciano é baseado no cálculo do vetor gradiente de segunda ordem.

$\nabla^{2}f = \frac{\partial^{2}f}{\partial x^{2}} + \frac{\partial^{2}f}{\partial y^{2}}$

$\frac{\partial^{2}f}{\partial x^{2}} = f(x + 1, y) + f(x - 1, y) - 2f(x, y)$

$\frac{\partial^{2}f}{\partial y^{2}} = f(x, y + 1) + f(x, y - 1) - 2f(x, y)$

Observe que a equação acima pode ser definida pela seguinte máscara de filtro $3 \ x \ 3$:

| $0$ | $1$ | $0$ |
|:---:|:---:|:---:|
| $1$ | $-4$ | $1$ |
| $0$ | $1$ | $0$ |

No entanto, observe que os pixels nas diagonais da máscara possuem peso 0 e portanto não influenciam no cálculo da intensidade do pixel de saída. Isso signiica que apenas bordas verticais e horizontais seriam detectadas pelo filtro. Sendo assim, o seguinte filtro, também $3 \ x \ 3$ é mais utilizado:

| $1$ | $1$ | $1$ |
|:---:|:---:|:---:|
| $1$ | $-8$ | $1$ |
| $1$ | $1$ | $1$ |

## Aplicação do Filtro

O Filtro Laplaciano tende a produzir imagens com arestas e outras descontinuidades de intensidade na cor cinzenta (quanto maior a discontinuidade, mais próxima de branco) em contraste com um fundo preto sem características (regiões com baixa variação de intensidade na imagem original e portanto derivada próxima de 0).

Sendo assim, uma operação comum é a reconstrução do fundo por meio da soma da imagem original com a imagem de saída do filtro.

$g(x, y) = f(x, y) + c[\nabla^{2}f(x, y)]$

onde $c$ é uma constante, tal que $c = -1$ para máscaras com centro negativo e $c = 1$, caso contrário.

| $1$ | $1$ | $1$ |
|:---:|:---:|:---:|
| $1$ | $-8$ | $1$ |
| $1$ | $1$ | $1$ |

| $-1$ | $-1$ | $-1$ |
|:---:|:---:|:---:|
| $-1$ | $8$ | $-1$ |
| $-1$ | $-1$ | $-1$ |

## Filtro de Ênfase

Filtro que busca enfatizar as arestas e outras descontinuidades de intensidade, porém, sem eliminar os componentes de baixa frequência da imagem (regiões de intensidade contínua).

Ao contrário do Filtro Laplaciano, que, além da operação de convolução, é necessário fazer uma soma ou subtração da imagem de saída com a imagem original, o filtro de ênfase necessita apenas da aplicação de uma única operação de convolução.

$g(x, y) = Af(x, y) + \nabla^{2}f(x, y)$

Esse filtro pode ser implementado com uma das seguintes máscaras:

| $0$ | $-1$ | $0$ |
|:---:|:---:|:---:|
| $-1$ | $A + 4$ | $-1$ |
| $0$ | $-1$ | $0$ |

| $-1$ | $-1$ | $-1$ |
|:---:|:---:|:---:|
| $-1$ | $A + 8$ | $-1$ |
| $-1$ | $-1$ | $-1$ |

Como a imagem de saída do filtro laplaciano será somada da imagem original multiplicada por um fator $A$, é como se, na verdade, o pixel central da máscara que está sendo adicionado pelo pixel correspondente na imagem original. Dessa forma, basta colocar a intensidade do pixel central em evidência e somar os dois valores que o multiplicam: $A$ e o valor central presente na máscara.

Valores comumente utilizados para $A$ são $1.3$ e $1.7$.