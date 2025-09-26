import streamlit as st
import sqlite3
from utils.db import DB_PATH

def get_conn():
    return sqlite3.connect(DB_PATH)

def login():
    st.subheader("🔑 Login")
    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")

    if st.button("Entrar", key="login_btn"):
        if not email or not senha:
            st.warning("Preencha email e senha.")
            return

        conn = get_conn()
        c = conn.cursor()
        c.execute("SELECT nome, senha FROM usuarios WHERE email = ?", (email.strip(),))
        user = c.fetchone()
        conn.close()

        if user:
            stored_hash = user[1]
            try:
                if bcrypt.checkpw(senha.encode("utf-8"), stored_hash.encode("utf-8")):
                    st.success(f"Bem-vindo, {user[0]}!")
                    st.session_state["usuario"] = user[0]
                    st.experimental_rerun()
                else:
                    st.error("Senha incorreta.")
            except ValueError:
                st.error("Senha em formato inválido, recadastre-se.")
        else:
            st.error("Email não cadastrado.")

def cadastro():
    st.subheader("📝 Cadastro")
    nome = st.text_input("Nome", key="cadastro_nome")
    email = st.text_input("Email", key="cadastro_email")
    senha = st.text_input("Senha", type="password", key="cadastro_senha")

    if st.button("Cadastrar", key="cadastro_btn"):
        if not nome or not email or not senha:
            st.warning("Preencha todos os campos.")
            return

        conn = get_conn()
        c = conn.cursor()
        try:
            hashed = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())
            c.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome.strip(), email.strip(), hashed.decode("utf-8"))
            )
            conn.commit()
            st.success("Usuário cadastrado com sucesso!")
            st.session_state["usuario"] = nome.strip()
            st.experimental_rerun()
        except sqlite3.IntegrityError:
            st.error("Este email já está cadastrado.")
        finally:
            conn.close()
