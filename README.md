# make-aggrid

`make-aggrid` é uma biblioteca Python que facilita a configuração avançada do componente AgGrid para uso com Streamlit. Basta passar um DataFrame e ela automaticamente aplica filtros, formatações e estilos adequados com base nos tipos de dados.

## Instalação

```bash
pip install make-aggrid
```

## Uso Básico

```python
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from make_aggrid import make_grid

df = pd.read_csv("dados.csv")

grid_options = make_grid(df)
AgGrid(df, gridOptions=grid_options)
```

## Recursos incluídos

- Filtros automáticos para texto, número e datas
- Formatação brasileira para números e datas (`pt-BR`)
- Alinhamento de colunas conforme tipo
- Edição inline
- Paginação e animações

## Exemplo Avançado com Streamlit

```python
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from make_aggrid import make_grid

data = {
    "Nome": ["Ana", "João", "Carlos"],
    "Idade": [23, 35, 29],
    "Salário": [3000.50, 5000.00, 4200.75],
    "Data de Admissão": pd.to_datetime(["2020-01-15", "2019-03-10", "2021-07-22"])
}

df = pd.DataFrame(data)

st.title("Tabela Interativa com AgGrid")

grid_options = make_grid(df)
AgGrid(df, gridOptions=grid_options, editable=True, fit_columns_on_grid_load=True)
```

## Licença

MIT