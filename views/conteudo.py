import streamlit as st

def show():
    st.subheader("📚 Conteúdo")

    st.write("Aqui você pode adicionar artigos, vídeos e materiais.")
    texto = st.text_area("Adicionar nota:", key="conteudo_texto")
    
    if st.button("Salvar Nota", key="btn_salvar_nota"):
        st.success(f"Nota salva: {texto}")
