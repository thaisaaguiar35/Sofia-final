import streamlit as st
import sqlite3
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def login():
    st.subheader("🔐 Login")

    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")

    if st.button("Entrar", key="login_btn_entrar"):
        conn = sqlite3.connect("sofia.db")
        c = conn.cursor()
        c.execute(
            "SELECT * FROM usuarios WHERE email=? AND senha=?",
            (email, hash_senha(senha))
        )
        usuario = c.fetchone()
        conn.close()

        if usuario:
            st.session_state["usuario"] = usuario[1]  # salva nome na sessão
            st.success(f"Bem-vindo, {usuario[1]}! ✅")
        else:
            st.error("Email ou senha incorretos ❌")
