# Fatiamento de Bits

Cada plano pode ser representado individualmente como uma imagem binária (assume apenas 0 ou 1 como níveis de intensidade).

Geralmente, os bits mais significativos guardam as informações mais importantes para a composição da imagem e, portanto, são selecionados na compressão da mesma. Quanto mais bits forem utilizados, mais o resultado obtido se aproxima da imagem original.

Para a reconstrução da imagem original, os bits removidos são substituídos pelo valor zero. Sendo assim, para o cálculo da intensidade de cada pixel, basta realizar o somatório de cada bit selecionado multiplicado por $2^n$, onde $n$ representa o n-ésimo plano da imagem, que se encontra ocupado pelo bit em questão.

## Detalhes da Implementação

