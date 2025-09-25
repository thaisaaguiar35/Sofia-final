import streamlit as st
import pandas as pd

def show():
    st.subheader("📊 Dashboard")

    # Exemplo de dados
    dados = {
        "Categoria": ["A", "B", "C", "D"],
        "Valores": [10, 23, 17, 5]
    }
    df = pd.DataFrame(dados)

    st.dataframe(df, use_container_width=True)

    # Removi o key porque st.bar_chart não aceita esse argumento
    st.bar_chart(df.set_index("Categoria"))
