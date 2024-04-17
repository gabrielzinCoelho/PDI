# Filtros Lineares de Suavização

A saída é a média dos pixels contidos na vizinhança da máscara.

Utilizados para reduzir transições abruptas de intensidade, diminuindo ruídos e borrando as bordas presentes na imagem. Dessa forma, suaviza falsos contornos, provocados pelo uso de poucos níveis de cinza, e também reduz detalhes irrelevantes contidos na imagem, regiões menores que o tamanho da máscara utilizada.

Podem ser destacados dois tipos de filtros lineares de suavização:

* Filtro da Média

Todos os pixels da vizinhança tem o mesmo peso no cálculo da intensidade do pixel de saída.

Exemplo de uma máscara $3 \ x \ 3$:

| $\frac{1}{9}$ | $\frac{1}{9}$ | $\frac{1}{9}$ |
|:-------------:|:-------------:|:-------------:|
| $\frac{1}{9}$ | $\frac{1}{9}$ | $\frac{1}{9}$ <tr></tr>|
| $\frac{1}{9}$ | $\frac{1}{9}$ | $\frac{1}{9}$ <tr></tr>|

* Filtro da Média Ponderada

Diferentes pesos são atribuídos a cada posição da máscara, resultando no fato de que os pixels da vizinhança vão impactar de forma diferente na intensidade final. De qualquer forma, a soma dos pesos deve resultar em 1.

Exemplo de uma máscara $3 \ x \ 3$, em que os pixels da vizinhança-4 e o pixel central tem peso maior:

| $\frac{1}{16}$ | $\frac{2}{16}$ | $\frac{1}{16}$ |
|:--------------:|:--------------:|:--------------:|
| $\frac{2}{16}$ | $\frac{4}{16}$ | $\frac{2}{16}$ <tr></tr>|
| $\frac{1}{16}$ | $\frac{2}{16}$ | $\frac{1}{16}$ <tr></tr>|