import bcrypt
import streamlit as st
from utils.db import init_db
from views import conteudo, dashboard, documentos, login

# Inicializa banco de dados
init_db()

# Título
st.markdown("<h1 style='color: purple;'>🥷 SofIA</h1>", unsafe_allow_html=True)

def main():
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
        opcao = st.sidebar.radio("Navegação", ["Dashboard", "Conteúdo", "Documentos"], key="menu_lateral")

        if opcao == "Conteúdo":
            conteudo.show()
        elif opcao == "Dashboard":
            dashboard.show()
        elif opcao == "Documentos":
            documentos.show()

        # Logout seguro
        if st.sidebar.button("Sair", key="botao_sair"):
            st.session_state.clear()
            st.experimental_rerun()

# Roda a função main
if __name__ == "__main__":
    main()
