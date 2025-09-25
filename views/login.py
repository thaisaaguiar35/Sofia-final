import streamlit as st
import sqlite3
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def login():
    st.subheader("🔐 Login")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        conn = sqlite3.connect("sofia.db")
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, hash_senha(senha)))
        usuario = c.fetchone()
        conn.close()

        if usuario:
            st.session_state["usuario"] = usuario[1]  # Nome do usuário
            st.success(f"Bem-vindo, {usuario[1]}! ✅")
        else:
            st.error("Email ou senha incorretos ❌")

def cadastro():
    st.subheader("📝 Cadastro")
    nome = st.text_input("Nome", key="cadastro_nome")  # rótulo corrigido
    email = st.text_input("Email", key="cadastro_email")
    senha = st.text_input("Senha", type="password", key="cadastro_senha")

    if st.button("Cadastrar", key="btn_cadastrar"):
        conn = sqlite3.connect("sofia.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                      (nome, email, hash_senha(senha)))
            conn.commit()
            st.success("Cadastro realizado com sucesso! 🎉 Agora faça login.")
        except sqlite3.IntegrityError:
            st.error("Email já cadastrado ❌")
        finally:
            conn.close()
