import streamlit as st

def show():
    st.subheader("📂 Documentos")
    uploaded_file = st.file_uploader("Carregar documento", type=["pdf", "docx", "txt"], key="doc_uploader")
    if uploaded_file:
        st.success(f"Arquivo {uploaded_file.name} carregado com sucesso! ✅")

