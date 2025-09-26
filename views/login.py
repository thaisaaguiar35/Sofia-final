import streamlit as st
import sqlite3
import hashlib

def hash_senha(senha: str) -> str:
    """Retorna o hash da senha com SHA256"""
    return hashlib.sha256(senha.encode()).hexdigest()


def login():
    st.subheader("🔐 Login")

    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")

    if st.button("Entrar", key="btn_login"):
        ...

    if st.button("Entrar", key="btn_login"):
        conn = sqlite3.connect("sofia.db")
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, hash_senha(senha)))
        usuario = c.fetchone()
        conn.close()

        if usuario:
            st.session_state["usuario"] = usuario[1]  # Nome do usuário
            st.success(f"Bem-vindo, {usuario[1]}! ✅")
            st.rerun()  # Recarrega a aplicação
        else:
            st.error("Email ou senha incorretos ❌")


def cadastro():
    st.subheader("📝 Cadastro")

    nome = st.text_input("Nome", key="cadastro_nome")
    email = st.text_input("Email", key="cadastro_email")
    senha = st.text_input("Senha", type="password", key="cadastro_senha")

def cadastrar_usuario():
    conn = sqlite3.connect("sofia.db")
    c = conn.cursor()
    c.execute("INSERT INTO tabela VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

