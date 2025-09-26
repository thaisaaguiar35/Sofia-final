import streamlit as st

def show():
    st.subheader("📚 Conteúdo")
    texto = st.text_area("Adicionar nota:", key="conteudo_texto")
    if st.button("Salvar Nota", key="btn_salvar_nota"):
        st.success(f"Nota salva: {texto}")
