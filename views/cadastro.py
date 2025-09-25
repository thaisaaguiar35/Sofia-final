import streamlit as st
import sqlite3
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastro():
    st.subheader("📝 Cadastro")

    nome = st.text_input("Nome", key="cadastro_nome")
    email = st.text_input("Email", key="cadastro_email")
    senha = st.text_input("Senha", type="password", key="cadastro_senha")

    if st.button("Cadastrar", key="cadastro_btn_cadastrar"):
        if not nome or not email or not senha:
            st.error("Por favor, preencha todos os campos!")
            return

        conn = sqlite3.connect("sofia.db")
        c = conn.cursor()
        # criar tabela se não existir
        c.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            )
        """)
        try:
            c.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome, email, hash_senha(senha))
            )
            conn.commit()
            st.success("Cadastro realizado com sucesso! 🎉 Agora faça login.")
        except sqlite3.IntegrityError:
            st.error("Email já cadastrado ❌")
        finally:
            conn.close()

