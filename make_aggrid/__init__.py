from st_aggrid import AgGrid, GridOptionsBuilder

def make_grid(df):

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(selection_mode="multiple")
    gb.configure_grid_options(animateRow=True)
    gb.configure_grid_options(pagination=True)

    columns_object = df.select_dtypes(include='object').columns.tolist()
    columns_date = df.select_dtypes(include='datetime64[ns]').columns.tolist()
    columns_int = df.select_dtypes(include='int64').columns.tolist()
    columns_float = df.select_dtypes(include='float64').columns.tolist()

    for col in columns_object:
        gb.configure_column(
            col,
            header_name=col,
            editable=True,
            cellStyle={"textAlign": 'left'},
            filter="agTextColumnFilter",
            floatingFilter=True,
            filterParams={
                "buttons": ["reset", "apply"],
                "caseSensitive": False,
                "suppressAndOrCondition": True,
            },
        )        
    for col in columns_date:
        df[col] = df[col].dt.strftime('%Y-%m-%d')
        gb.configure_column(
            col,
            header_name=col,
            editable=True,
            cellStyle={"textAlign": "center"},
            type=["dateColumn"],
            filter="agDateColumnFilter",
            filterParams={
                "browserDatePicker": True,
                "minValidYear": 1900,
                "maxValidYear": 2100,
                "buttons": ["reset", "apply"],
            },
            floatingFilter=True,
            value_formatter="x.toLocaleDateString('pt-BR')",  # 👈 Formata a data
        )
    for col in columns_int:
        gb.configure_column(
            col,
            header_name=col,
            editable=True,
            cellStyle={"textAlign": 'center'},
            valueFormatter="x.toLocaleString('pt-BR', { minimumFractionDigits: 0, maximumFractionDigits: 0 })",  # 👈 Formata o valor como inteiro
            filter="agNumberColumnFilter",
            floatingFilter=True,
            filterParams={
                "buttons": ["reset", "apply"],
                "caseSensitive": False,
                "suppressAndOrCondition": True,
            },
        )
    for col in columns_float:
        gb.configure_column(
            col,
            header_name=col,
            editable=True,
            cellStyle={"textAlign": 'right'},
            valueFormatter="x.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })",  # 👈 Formata o valor como moeda
            filter="agNumberColumnFilter",
            floatingFilter=True,
            filterParams={
                "buttons": ["reset", "apply"],
                "caseSensitive": False,
                "suppressAndOrCondition": True,
            },
        )

    return gb.build()