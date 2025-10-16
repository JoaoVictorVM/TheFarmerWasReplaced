# Script de Colheita de Arbusto

Este script tem como objetivo **automatizar totalmente o ciclo de plantio e colheita de arbustos** na fazenda.  
A lógica ainda é bem simples: o drone percorre toda a área da plantação, planta um arbusto em cada posição e, depois disso, faz uma segunda varredura colhendo todos os arbustos que já cresceram.  

O processo então se repete em loop, garantindo um ciclo contínuo de **plantar → crescer → colher**.

---

## 🧠 Lógica por trás do script

Assim como no script da grama, aqui também utilizamos a função **`get_world_size()`** para que o drone consiga percorrer toda a fazenda, **independente do tamanho do terreno**.

Durante o processo, o drone segue dois passos principais:

1. **Plantio:** em cada posição, o drone executa  

   ```python
   plant(Entities.Bush)

2. **Colheita:** após o plantio, o drone percorre novamente todo o mapa e verifica se o arbusto já pode ser colhido, utilizando uma checagem simples:

   ```python
    if can_harvest():
        harvest()