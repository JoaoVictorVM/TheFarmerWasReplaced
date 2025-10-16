# Script de Colheita de Cenoura

Este script tem como objetivo **automatizar totalmente o ciclo de plantio e colheita de cenouras** na fazenda.  
Aqui somos apresentados a uma nova mecânica do jogo: **arar o chão**.  
Diferente das plantações anteriores, **as cenouras só podem ser plantadas em solo arado**, então nosso drone precisa primeiro preparar o terreno antes de iniciar o plantio.  
O fluxo geral será o mesmo visto na automação do arbusto — percorrer todo o terreno, plantar, colher e repetir o processo continuamente.

---

## 🧠 Lógica por trás do script

Assim como nos outros scripts, continuamos utilizando a função **`get_world_size()`**, que permite ao drone percorrer toda a fazenda **independente do tamanho do mapa**.

Durante o processo, o drone verifica o tipo de chão da posição atual com **`get_ground_type()`**.  
Essa função retorna o tipo de solo em que o drone está, e aqui usamos ela para identificar se o terreno é **`Grounds.Grassland`** (solo comum).  
Caso seja, o drone executa **`till()`** para arar aquele local, preparando-o para o plantio.

Depois que o terreno estiver pronto, o drone faz uma nova varredura plantando e colhendo as cenouras, seguindo a lógica abaixo:

1. **Arar:** em cada posição, o drone faz a validação do tipo de solo.  
   Se o chão for normal, ele ara o terreno:  
   
   ```python
   if get_ground_type() == Grounds.Grassland:
       till()

2. **Plantar e Colher:** após o solo estar preparado, o drone percorre novamente todo o mapa.
Em cada posição, ele verifica se pode colher e planta uma nova cenoura:
   
   ```python
   if can_harvest():
        harvest()
    plant(Entities.Carrot)