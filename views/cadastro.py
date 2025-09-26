# views/cadastro.py
import streamlit as st
from utils.db import init_db, hash_password
import sqlite3

def show():
    import streamlit as st
    st.title("Cadastro de Usuário")

    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Cadastrar"):
        if not nome or not email or not senha:
            st.error("Preencha todos os campos!")
        else:
            init_db()
            conn = sqlite3.connect("sofia.db")
            c = conn.cursor()
            try:
                c.execute(
                    "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                    (nome, email, hash_password(senha))
                )
                conn.commit()
                st.success("Usuário cadastrado com sucesso!")
            except Exception as e:
                st.error("Erro ao cadastrar usuário: " + str(e))
            finally:
                conn.close()

