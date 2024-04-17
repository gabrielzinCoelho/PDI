# Filtros Não-lineares de Suavização

Os pixels contidos na vizinhança são ordenados e, então, o pixel resultante na imagem de saída é determinado por algum critério baseado na ordenação feita.

Alguns exemplos de filtros espaciais não-lineares:

* Mediana

Pixel central, na imagem de saída, é substituído pela mediana dos pixels vizinhos.

Pontos com intensidade distinta são forçados a assumirem valores mais próximos de sua vizinhança. 

Fornece uma boa redução de ruídos aleatórios sem causar a impressão de borramento na imagem, que filtros lineares podem produzir. Pode-se citar o ruído "sal e pimenta" como exemplo de bom caso de uso de um filtro mediano.

Agrupamentos isolados de pixels que possuem intensidade discrepante com sua vizinhança, sejam mais claros ou mais escuros, e cuja área é menor que a metade da área da máscara utilizada, são eliminados pelo filtro da mediana. Isso porque tal restrição de tamanho, ser inferior à metada de máscara, garante que o valor obtido ao calcular a mediana seja de um dos pixels de sua vizinhança e não um pixel pertence ao próprio agrupamento.

* Mínimo

Pixel central, na imagem de saída, é substituído pelo menor valor dos pixels vizinhos.

* Máximo

Pixel central, na imagem de saída, é substituído pelo maior valor dos pixels vizinhos.