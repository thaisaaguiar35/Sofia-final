import streamlit as st

def show():
    st.subheader("📂 Documentos")

    # Upload de arquivos
    uploaded_file = st.file_uploader(
        "Carregar documento", 
        type=["pdf", "docx", "txt"], 
        key="doc_uploader"
    )

    # Mensagem de sucesso ao carregar o arquivo
    if uploaded_file:
        st.success(f"Arquivo {uploaded_file.name} carregado com sucesso! ✅")
