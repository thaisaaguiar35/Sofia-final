import streamlit as st
from utils.db import get_user_by_email, update_password

def recuperar():
    from app import get_user_by_email, update_password
    # resto do código
    
    email = st.text_input("Digite seu e-mail cadastrado")
    nova_senha = st.text_input("Digite a nova senha", type="password")
    confirmar = st.text_input("Confirme a nova senha", type="password")

    if st.button("Redefinir senha"):
        if not email or not nova_senha or not confirmar:
            st.warning("⚠️ Preencha todos os campos!")
        elif nova_senha != confirmar:
            st.error("❌ As senhas não coincidem!")
        else:
            usuario = get_user_by_email(email)
            if usuario:
                update_password(email, nova_senha)
                st.success("✅ Senha redefinida com sucesso!")
            else:
                st.error("❌ E-mail não encontrado no sistema.")
