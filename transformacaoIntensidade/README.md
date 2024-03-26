# Funções de Transformação de Intensidade Básicas

Funções de transformação de intensidade se enquadram na categoria de métodos de processamento que ocorrem no **domínio do espaço**, ou seja, operam diretamente sobre os pixels da imagem.

Diferentemente dos métodos de filtragem espacial, que também são métodos que atuam no domínio espacial, as operações de transformação de intensidade **determinam o novo nível de intensidade de um determinado pixel baseado exclusivamente no seu atual valor**, dessa forma, sem considerar o valor dos seus pixels vizinhos.

## Definição matemática

Tais funções podem ser expressas como: 

&nbsp;&nbsp;&nbsp;&nbsp; $g(x, y) = T[f(x, y)]$

onde $g(x, y)$ é a função que determina a imagem de saída, $f(x, y)$ a função que determina a imagem de entrada e $T$ um operador que atua sobre $f$ defininido na vizinhança de $(x, y)$.

No caso específico das funções de intensidade, $T$ é definido como uma função de transformação de intensidade expressa da seguinte forma:

&nbsp;&nbsp;&nbsp;&nbsp; $s = T(r)$

onde $r$ e $s$ denotam os níveis de intensidade dos pixels em $f(x, y)$ e $g(x, y)$ respectivamente.

## Exemplos de implementações

* [Limiarização]()
* [Negativo de Imagens]()
* [Transformação Logarítimica]()
* [Transformação de Potência]()
* [Transformação Linear Definida por Partes](linearPorPartes)