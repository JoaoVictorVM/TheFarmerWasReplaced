# Script de Colheita de Grama

Este script tem como objetivo **automatizar completamente a colheita da grama** na fazenda.  
A lógica é simples, mas muito eficiente: o drone percorre **toda a área da plantação**, verifica se há grama crescida em cada posição e, caso haja, realiza a colheita automaticamente.

---

## 🧠 Lógica por trás do script

A base da automação é garantir que o drone **visite todas as posições possíveis do terreno**, independentemente do tamanho da fazenda.  
Pra isso, usamos a função **`get_world_size()`**, que retorna as dimensões totais do mapa (largura e altura).  
Assim, o código se adapta a qualquer tamanho de plantação — desde pequenos campos até áreas maiores.

Durante o percurso, o drone segue uma rotina de varredura em um **padrão de linhas**, garantindo que **nenhum quadrado da plantação seja deixado para trás**.

Em cada posição visitada, ele faz uma checagem:

```python
if can_harvest():
    harvest()