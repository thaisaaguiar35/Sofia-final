import streamlit as st
import pandas as pd
import altair as alt

def show():
    st.subheader("📊 Dashboard de Alunos")

    # Dados de exemplo (substitua por leitura do DB se quiser)
    dados = {
        "Nome": ["Ana", "Bruno", "Carla", "Diego", "Eduarda", "Felipe", "Gabriela"],
        "Nota": [8.5, 6.0, 9.2, 5.5, 7.8, 4.9, 10.0],
        "Frequência": [92, 80, 95, 60, 85, 55, 98]
    }
    df = pd.DataFrame(dados)

    # Filtros na sidebar
    st.sidebar.header("Filtros")
    filtro_nome = st.sidebar.text_input("Filtrar por nome", key="filtro_nome")
    nota_minima = st.sidebar.slider("Nota mínima", 0.0, 10.0, 0.0, 0.1, key="filtro_nota")
    freq_minima = st.sidebar.slider("Frequência mínima (%)", 0, 100, 0, 1, key="filtro_freq")

    df_filtrado = df.copy()
    if filtro_nome:
        df_filtrado = df_filtrado[df_filtrado["Nome"].str.contains(filtro_nome, case=False, na=False)]

    df_filtrado = df_filtrado[
        (df_filtrado["Nota"] >= nota_minima) &
        (df_filtrado["Frequência"] >= freq_minima)
    ]

    st.write("### 📋 Alunos Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)

    # Gráfico de notas (Altair)
    st.write("### 📈 Notas por Aluno")
    if not df_filtrado.empty:
        chart_notas = alt.Chart(df_filtrado).mark_bar().encode(
            x=alt.X("Nome:N", sort=None),
            y=alt.Y("Nota:Q"),
            tooltip=["Nome", "Nota", "Frequência"]
        ).properties(height=300)
        st.altair_chart(chart_notas, use_container_width=True)

        st.write("### 📊 Frequência por Aluno")
        chart_freq = alt.Chart(df_filtrado).mark_bar().encode(
            x=alt.X("Nome:N", sort=None),
            y=alt.Y("Frequência:Q"),
            tooltip=["Nome", "Nota", "Frequência"]
        ).properties(height=300)
        st.altair_chart(chart_freq, use_container_width=True)
    else:
        st.info("Sem resultados com esses filtros.")
