import streamlit as st
import pandas as pd
import altair as alt

def show():
    st.subheader("📊 Dashboard de Alunos")

    # Dados de exemplo (substitua pelo banco de dados se quiser)
    dados = {
        "Nome": ["Ana", "Bruno", "Carla", "Diego", "Eduarda", "Felipe", "Gabriela"],
        "Nota": [8.5, 6.0, 9.2, 5.5, 7.8, 4.9, 10.0],
        "Frequência": [92, 80, 95, 60, 85, 55, 98]
    }
    df = pd.DataFrame(dados)

    # ---------------------------
    # Filtros na barra lateral
    # ---------------------------
    st.sidebar.header("Filtros")
    filtro_nome = st.sidebar.text_input("Filtrar por nome", key="filtro_nome")
    nota_minima = st.sidebar.slider("Nota mínima", 0.0, 10.0, 0.0, 0.1, key="filtro_nota")
    freq_minima = st.sidebar.slider("Frequência mínima (%)", 0, 100, 0, 1, key="filtro_freq")

    # ---------------------------
    # Aplicar filtros
    # ---------------------------
    df_filtrado = df.copy()

    if filtro_nome:
        df_filtrado = df_filtrado[
            df_filtrado["Nome"].str.contains(filtro_nome, case=False, na=False)
        ]

    df_filtrado = df_filtrado[
        (df_filtrado["Nota"] >= nota_minima) &
        (df_filtrado["Frequência"] >= freq_minima)
    ]

    # ---------------------------
    # Exibir tabela
    # ---------------------------
    st.write("### 📋 Alunos Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)

    # ---------------------------
    # Gráficos (Altair)
    # ---------------------------
    if not df_filtrado.empty:
        st.write("### 📈 Notas por Aluno")
        chart_notas = (
            alt.Chart(df_filtrado)
            .mark_bar(color="#4C78A8")
            .encode(
                x=alt.X("Nome:N", sort=None, title="Aluno"),
                y=alt.Y("Nota:Q", title="Nota"),
                tooltip=["Nome", "Nota", "Frequência"]
            )
            .properties(height=300)
        )
        st.altair_chart(chart_notas, use_container_width=True)

        st.write("### 📊 Frequência por Aluno")
        chart_freq = (
            alt.Chart(df_filtrado)
            .mark_bar(color="#F58518")
            .encode(
                x=alt.X("Nome:N", sort=None, title="Aluno"),
                y=alt.Y("Frequência:Q", title="Frequência (%)"),
                tooltip=["Nome", "Nota", "Frequência"]
            )
            .properties(height=300)
        )
        st.altair_chart(chart_freq, use_container_width=True)
    else:
        st.info("⚠️ Sem resultados com esses filtros.")
