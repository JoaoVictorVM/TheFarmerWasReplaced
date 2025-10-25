# Script de Colheita de Arvore

Este script tem como objetivo **automatizar completamente o processo de plantio e colheita de árvores** na fazenda.  
A mecânica aqui é parecida com a dos outros cultivos, mas com um detalhe importante: **árvores plantadas muito próximas demoram muito mais para crescer**.  
Cada árvore plantada diretamente ao lado de outra faz com que o tempo de crescimento dobre, e isso se acumula! Ou seja, se você plantar várias árvores coladas, o tempo pode aumentar em até **16 vezes**.  
Por isso, precisamos criar uma lógica que garanta **espaçamento entre as árvores**.

---

## 🧠 Lógica por trás do script

A base da automação continua a mesma: nosso drone precisa percorrer **toda a fazenda**, então continuamos usando **`get_world_size()`** para definir o tamanho do mundo.  
A diferença está na forma de **decidir onde plantar**.

Para evitar o crescimento lento das árvores, criamos um **contador** e uma **função auxiliar** para verificar se a posição atual é par ou ímpar.  
A ideia é que o drone plante apenas em posições alternadas, criando o espaçamento necessário automaticamente.

```python
count = 0

def count_is_par():
    return count % 2 == 0

```

Essa função retorna `True` quando a linha (eixo X) atual é par.
Usando essa lógica, podemos fazer com que o drone alterne o padrão de plantio entre as linhas pares e ímpares.

Dentro da varredura da fazenda, o comportamento será:

```python

if (count_is_par() == True):
    def is_even():
        y = get_pos_y()
        return y % 2 == 0
    if (is_even() == True):
        plant(Entities.Tree)
    else:
        if (is_even() == False):
            plant(Entities.Tree)

```

Assim, o drone só planta árvores em posições alternadas, garantindo o espaçamento ideal entre elas.
A cada vez que o drone se mover uma coluna para o leste `move(East)`, incrementamos o contador:

```python

count = count + 1

```

Dessa forma, ele percorre toda a fazenda e mantém o padrão de espaçamento entre árvores, garantindo que o crescimento delas aconteça no tempo normal, sem penalidades de proximidade.

Depois de toda essa lógica realizada, utilizamos nossa função de colheita para verificar se há árvores prontas e colher automaticamente sempre que possível, completando o ciclo da automação.

```python

if can_harvest():
    harvest()

```