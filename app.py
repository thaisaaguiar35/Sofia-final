import os
import streamlit as st
from utils.db import init_db
from views import conteudo, dashboard, documentos, login

# Inicializa banco
init_db()

# Debug: mostra caminho do DB (opcional)
st.write("Caminho do banco de dados:", os.path.abspath("sofia.db"))

# Título
st.markdown("<h1 style='color: purple;'>🥷 SofIA</h1>", unsafe_allow_html=True)

# Verifica usuário na sessão
usuario = st.session_state.get("usuario")

if not usuario:
    # Acesso: Login ou Cadastro
    aba = st.radio("Acesso", ["Login", "Cadastro"], key="aba_acesso")
    
    if aba == "Login":
        login.login()
    else:
        login.cadastro()
else:
    # Menu após login
    st.sidebar.title(f"👤 Olá, {usuario}")

    opcao = st.sidebar.radio(
        "Navegação",
        ["Dashboard", "Conteúdo", "Documentos"],
        key="menu_lateral"
    )

    # Renderiza a página selecionada
    if opcao == "Dashboard":
        dashboard.show()
    elif opcao == "Conteúdo":
        conteudo.show()
    elif opcao == "Documentos":
        documentos.show()

    # Logout seguro sempre visível
    if st.sidebar.button("Sair", key="botao_sair"):
        st.session_state.clear()
        st.experimental_rerun()
