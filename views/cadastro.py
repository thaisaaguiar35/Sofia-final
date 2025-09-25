def cadastro():
    st.subheader("📝 Cadastro")

    nome = st.text_input("Nome", key="cadastro_nome")
    email = st.text_input("Email", key="cadastro_email")
    senha = st.text_input("Senha", type="password", key="cadastro_senha")

    if st.button("Cadastrar", key="cadastro_btn_cadastrar"):
        conn = sqlite3.connect("sofia.db")
        c = conn.cursor()
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
