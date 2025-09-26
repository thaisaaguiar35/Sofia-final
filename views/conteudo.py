def show():
    import streamlit as st

    st.write("📚 Página de Conteúdo")
    st.write("Aqui você pode adicionar artigos, vídeos e materiais.")

    # Área de texto para adicionar nota
    texto = st.text_area("Adicionar nota:", key="conteudo_texto")
    
    # Botão para salvar a nota
    if st.button("Salvar Nota", key="btn_salvar_nota"):
        if texto.strip():  # garante que não salve nota vazia
            st.success(f"Nota salva: {texto}")
        else:
            st.warning("Digite algum texto antes de salvar.")
