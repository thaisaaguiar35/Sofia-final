import streamlit as st
from utils.db import get_user_by_email, save_user  # Assumindo que você tenha funções para DB

def cadastro():
    st.header("🔐 Cadastro de Usuário")
    
    # Campos do formulário
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    confirmar_senha = st.text_input("Confirmar Senha", type="password")
    
    if st.button("Cadastrar"):
        # Validações básicas
        if not nome or not email or not senha or not confirmar_senha:
            st.error("Todos os campos são obrigatórios!")
            return
        
        if senha != confirmar_senha:
            st.error("As senhas não coincidem!")
            return
        
        # Verifica se o usuário já existe
        if get_user_by_email(email):
            st.error("Este email já está cadastrado!")
            return
        
        # Cria hash da senha
        hashed = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())
        
        # Salva no banco
        save_user(nome, email, hashed)
        
        st.success("Usuário cadastrado com sucesso!")
