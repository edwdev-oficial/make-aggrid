# make-aggrid

[![PyPI version](https://img.shields.io/pypi/v/make-aggrid.svg)](https://pypi.org/project/make-aggrid/)
[![Python versions](https://img.shields.io/pypi/pyversions/make-aggrid.svg)](https://pypi.org/project/make-aggrid/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repo stars](https://img.shields.io/github/stars/edwdev-oficial/make-aggrid?style=social)](https://github.com/edwdev-oficial/make-aggrid)


`make-aggrid` é uma biblioteca Python que facilita a configuração avançada do componente AgGrid para uso com Streamlit. Basta passar um DataFrame e ela automaticamente aplica filtros, formatações e estilos adequados com base nos tipos de dados.

## 📦 Instalação

### Com pip

```bash
pip install make-aggrid streamlit-aggrid==1.1.2
```

### com poetry
```bash
poetry add make-aggrid streamlit-aggrid@1.1.2
```

⚠️ O `make-aggrid` requer Python 3.10 ou superior (mas abaixo de 4.0) devido à dependência do `streamlit-aggrid` versão 1.1.2.

### Uso Básico
```python
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from make_aggrid import make_grid

df = pd.read_csv("dados.csv")

grid_options = make_grid(df)

grid_response = AgGrid(
    st.session_state.df,
    gridOptions=grid_options,
    enable_enterprise_modules=False,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,
    height=400
)
```

## 🎯 Recursos incluídos

- Filtros automáticos para texto, número e datas
- Formatação brasileira para números e datas (`pt-BR`)
- Alinhamento de colunas conforme tipo
- Edição inline
- Paginação e animações

### 🧪 Exemplo Avançado com Streamlit

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

### 🤝 Contribuir

Contribuições são muito bem-vindas! Para contribuir:
1. Faça um fork do repositório

2.  Crie uma branch (git checkout -b nova-funcionalidade)

3.  Faça suas alterações e commit (git commit -am 'Adiciona nova funcionalidade')

4.  Push para a branch (git push origin nova-funcionalidade)

5.  Abra um Pull Request

Sinta-se à vontade para abrir issues com ideias, sugestões ou bugs que encontrar.

## 📝 Changelog

Todas as mudanças relevantes são listadas no CHANGELOG.md

## Licença
MIT