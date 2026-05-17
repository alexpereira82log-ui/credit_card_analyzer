import streamlit as st
import pandas as pd

from app.controllers.upload_controller import UploadController
from app.utils.charts import Charts


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

        df, analysis = UploadController.process_invoice(uploaded_file)

        st.success("Fatura carregada com sucesso!")

        st.subheader("Resumo Financeiro")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Valor Total",
                f"R$ {analysis['total']:,.2f}"
            )

        with col2:
            st.metric(
                "Transações",
                analysis["transaction_count"]
            )

        with col3:
            st.metric(
                "Ticket Médio",
                f"R$ {analysis['average_ticket']:,.2f}"
            )

        st.subheader("Pré-visualização da Fatura")

        st.dataframe(
            df.style.format({
                "data": lambda x: x.strftime("%Y-%m-%d"),
                "valor": "R$ {:.2f}"
            })
        )

        st.subheader("Gastos por Categoria")

        st.dataframe(
            analysis["expenses_by_category"].style.format({
                "valor": "R$ {:.2f}"
            })
        )

        col1, col2 = st.columns(2)

        with col1:

            pie_chart = Charts.category_pie_chart(
                analysis["expenses_by_category"]
            )

            st.plotly_chart(
                pie_chart,
                use_container_width=True
            )

        with col2:

            bar_chart = Charts.category_bar_chart(
                analysis["expenses_by_category"]
            )

            st.plotly_chart(
                bar_chart,
                use_container_width=True
            )

        st.subheader("Insight Automático")

        summary = analysis["category_summary"]

        st.info(
            f"""
            A categoria com maior gasto foi
            '{summary["category"]}', representando
            {summary["percentage"]:.1f}% da fatura,
            totalizando R$ {summary["value"]:.2f}.
            """
        )

        st.subheader("Maiores Gastos")

        st.dataframe(
            analysis["top_expenses"].style.format({
                "data": lambda x: x.strftime("%Y-%m-%d"),
                "valor": "R$ {:.2f}"
            })
        )

        st.subheader("Compras Recorrentes")

        recurring_df = analysis["recurring_purchases"]

        if recurring_df.empty:

            st.warning("Nenhuma compra recorrente encontrada.")

        else:

            st.dataframe(
                recurring_df.style.format({
                    "valor_total": "R$ {:.2f}",
                    "ticket_medio": "R$ {:.2f}"
                })
            )

        st.subheader("Assinaturas Detectadas")

        subscriptions_df = analysis["subscriptions"]

        if subscriptions_df.empty:

            st.warning("Nenhuma assinatura detectada.")

        else:

            st.dataframe(
                subscriptions_df.style.format({
                    "data": lambda x: x.strftime("%Y-%m-%d"),
                    "valor": "R$ {:.2f}"
                })
            )

            total_subscriptions = subscriptions_df["valor"].sum()

            st.info(
                f"""
                Total mensal estimado com assinaturas:
                R$ {total_subscriptions:.2f}
                """
            )

        st.subheader("Parcelamentos Detectados")

        installments_df = analysis["installments"]

        if installments_df.empty:

            st.warning("Nenhum parcelamento detectado.")

        else:

            st.dataframe(
                installments_df.style.format({
                    "data": lambda x: x.strftime("%Y-%m-%d"),
                    "valor": "R$ {:.2f}",
                    "comprometimento_futuro": "R$ {:.2f}"
                })
            )

            future_commitment = (
                installments_df["comprometimento_futuro"]
                .sum()
            )

            st.info(
                f"""
                Comprometimento futuro identificado:
                R$ {future_commitment:.2f}
                """
            )

        st.subheader("Projeção da Próxima Fatura")

        projection = analysis["projection"]

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Assinaturas Previstas",
                f"R$ {projection['subscriptions_total']:.2f}"
            )

        with col2:

            st.metric(
                "Parcelamentos Ativos",
                f"R$ {projection['installments_total']:.2f}"
            )

        with col3:

            st.metric(
                "Próxima Fatura Estimada",
                f"R$ {projection['projected_total']:.2f}"
            )

        st.subheader("Score Financeiro")

        financial_score = analysis["financial_score"]

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Score",
                f"{financial_score['score']}/100"
            )

        with col2:

            st.metric(
                "Classificação",
                financial_score["level"]
            )

        if financial_score["alerts"]:

            st.subheader("Alertas Financeiros")

            for alert in financial_score["alerts"]:

                st.warning(alert)

        else:

            st.success(
                "Nenhum alerta financeiro relevante encontrado."
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