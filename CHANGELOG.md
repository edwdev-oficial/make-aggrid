# Changelog

Todas as alterações notáveis neste projeto serão documentadas aqui.

O formato segue [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), e o projeto segue [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [0.1.3] - 2025-04-19
### Corrigido
- Atualizado `README.md` para indicar a instalação com `streamlit-aggrid==1.1.2`.
- Compatibilidade com `Python >=3.10` documentada.
- Melhoria na documentação avançada com exemplo interativo usando `editable=True`.

---

## [0.1.2] - 2025-04-17
### Adicionado
- Parâmetro opcional `locale` para personalizar formatação numérica e de datas.

---

## [0.1.1] - 2025-04-15
### Adicionado
- Suporte para tipos de dados `datetime64` com filtro de datas e formatação `pt-BR`.

### Corrigido
- Erro ao aplicar estilos em colunas com valores nulos.
- Melhor compatibilidade com pandas 2.x.

---

## [0.1.0] - 2025-04-14
### Adicionado
- Primeira versão publicada no PyPI.
- Função `make_grid(df)` para gerar automaticamente `gridOptions` com base nos tipos de dados.
- Estilização automática para colunas numéricas, texto e datas.
- Filtros automáticos e ordenação ativada por padrão.

---

## [Unreleased]
- Suporte a temas escuros do Streamlit.
- Exportação para Excel diretamente da grade.

---

### Links

- [Todas as versões](https://pypi.org/project/make-aggrid/#history)
- [Repositório no GitHub](https://github.com/edwdev-oficial/make-aggrid)
