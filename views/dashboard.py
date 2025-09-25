import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    # Título da página
    st.title("📊 Dashboard Escolar")

    # Texto de introdução
    st.write("Aqui você encontra relatórios e estatísticas dos alunos.")

    # Criando dados de exemplo (poderia vir do banco de dados)
    dados = {
        "Aluno": ["Ana", "Bruno", "Carla", "Diego", "Fernanda"],
        "Notas": [8.5, 7.0, 9.2, 6.8, 8.0],
        "Frequência (%)": [95, 87, 98, 80, 90]
    }

    df = pd.DataFrame(dados)

    # Mostra a tabela
    st.subheader("📋 Notas e Frequência dos Alunos")
    st.dataframe(df)

    # Gráfico de notas
    st.subheader("📈 Distribuição das Notas")
    fig, ax = plt.subplots()
    ax.bar(df["Aluno"], df["Notas"])
    ax.set_xlabel("Alunos")
    ax.set_ylabel("Notas")
    ax.set_title("Notas dos alunos")
    st.pyplot(fig)

    # Gráfico de frequência
    st.subheader("📊 Frequência (%)")
    fig2, ax2 = plt.subplots()
    ax2.plot(df["Aluno"], df["Frequência (%)"], marker="o")
    ax2.set_xlabel("Alunos")
    ax2.set_ylabel("Frequência (%)")
    ax2.set_title("Frequência dos alunos")
    st.pyplot(fig2)