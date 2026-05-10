import streamlit as st
import pandas as pd

from app.controllers.upload_controller import UploadController


st.set_page_config(
    page_title="Credit Card Analyzer",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Analyzer")

st.write("Sistema inteligente de análise de faturas.")

st.divider()

uploaded_file = st.file_uploader(
    "Selecione a fatura CSV",
    type=["csv"]
)

if uploaded_file:

    try:

        df = UploadController.process_invoice(uploaded_file)

        st.success("Fatura carregada com sucesso!")

        st.subheader("Pré-visualização da Fatura")

        st.dataframe(
            df.style.format({
                "data": lambda x: x.strftime("%Y-%m-%d"),
                "valor": "R$ {:.2f}"
            })
        )

        st.subheader("Informações da Base")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Linhas", df.shape[0])

        with col2:
            st.metric("Colunas", df.shape[1])

        with col3:
            st.metric(
                "Memória",
                f"{round(df.memory_usage(deep=True).sum() / 1024, 2)} KB"
            )

    except Exception as e:

        st.error(str(e))