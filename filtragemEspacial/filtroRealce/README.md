# Filtros Espaciais de Realce para Arestas

* [**Filtro Laplaciano**](laplaciano)
* [**Filtro Gradiente**](gradiente)

Ao contrário dos filtros de suavização, os filtros de realce para arestas buscam evidenciar transições de intensidade em imagens.

Essas transições podem ser determinadas e medidas pelo uso de derivadas. Nesse caso, vale lembrar que imagens são funções bidimensionais que associam a cada posição (x, y), no domínio, um valor f(x, y), no contradomínio. Assim, a intensidade da derivada calculada em um ponto é proporcional ao grau de descontinuidade de intensidade na imagem naquele ponto.

Dessa forma, o comportamento das derivadas pode ser abordado em duas situações distintas:

* áreas de intensidade constante

* início e fim de descontinuidades (degraus e rampas)

```
Rampas são descontinuidades graduais de intensidade, enquanto degraus são descontinuidades abruptas (variações 
grandes em intervalo pequeno de pixels). 
```

## Definição Matemática

Apesar de, como dito anteriormente, imagens serem funções de natureza bidimensional, vamos tomar como base a definição das derivadas de primeira e segunda ordem para uma função unidimensional. Isso significa interpretar as variações de intensidade em uma única linha ou coluna, por exemplo.

$f'(x) = \displaystyle \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$

$f''(x) = \displaystyle \lim_{h \to 0} \frac{f(x + h) + f(x - h) - 2f(x)}{h^{2}}$

Porém, como imagens possuem valores discretos de posição, o menor valor que $h$ pode assumir ao tender a 0 é 1.

Assim, podemos reescrever as funções acima da seguinte forma:

$f'(x) =  f(x + 1) - f(x)$

$f''(x) =  f(x + 1) + f(x - 1) - 2f(x)$


### Comportamento esperado das derivadas

A primeira derivada deve possuir valor 0 em áreas de intensidade constante e diferente de 0 tanto no fim e início, quanto no decorrer de uma rampa ao degrau.

Já a segunda derivada, deve ser nula nos intervalos que a primeira derivada permance constante (sendo 0 ou não). Isso envolve tanto as áreas da imagem com intensidade constante (primeira derivada nula), quanto ao longo de uma rampa com inclinação constante (primeira derivada com valor constante e diferente de 0). Porém, a mesma possui valores diferente de 0 tanto no início quanto no fim de um degrau ou rampa.

Sendo assim, esse comportamento traz algumas implicações:

* Derivadas de primeira ordem produzem bordas mais grossas

* Derivadas de segunda ordem possuem resposta mais forte a detalhes finos, como ruídos e linhas finas

* Derivadas de segunda ordem produzem bordas duplas em transições de intensidade devido à sua ativação apenas no início e fim de rampas e degraus

* Os sinais das derivadas (especialmente de segunda ordem) podem ser utilizados para determinar se a transição foi de uma área mais clara para uma mais escura e vice-versa.

É comum que arestas em imagens digitais se comportem como rampas com inclinação constante. Sendo assim, a primeira derivada resulta em arestas grossas, pois assume um valor constante e diferente de zero, enquanto a segunda derivada produz arestas duplas com um pixel de largura, separada por zeros.

