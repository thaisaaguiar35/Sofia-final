import os
import streamlit as st
from utils.db import init_db
from views import conteudo, dashboard, documentos, login

# Inicializa banco e garante que todas as tabelas existam
init_db()

# Mostra o caminho completo do arquivo do banco (apenas para debug)
st.write("Caminho do banco de dados:", os.path.abspath("sofia.db"))

# Título estilizado em roxo
st.markdown(
    "<h1 style='color: purple;'>🥷 SofIA</h1>",
    unsafe_allow_html=True
)

# Controle de sessão
usuario = st.session_state.get("usuario")

if not usuario:
    aba = st.radio("Acesso", ["Login", "Cadastro"])
    if aba == "Login":
        login.login()
    else:
        login.cadastro()
else:
    # Menu lateral só aparece depois do login
    st.sidebar.title(f"👤 Olá, {usuario}")
    opcao = st.sidebar.radio("Navegação", ["Dashboard", "Conteúdo", "Documentos"])

    if opcao == "Conteúdo":
        conteudo.show()
    elif opcao == "Dashboard":
        dashboard.show()
    elif opcao == "Documentos":
        documentos.show()

    if st.sidebar.button("Sair"):
        del st.session_state["usuario"]
        st.experimental_rerun()  # força recarregar a página após logout
