import plotly.express as px


class Charts:

    @staticmethod
    def category_pie_chart(df):

        fig = px.pie(
            df,
            names="categoria",
            values="valor",
            title="Distribuição por Categoria",
            hole=0.4
        )

        return fig

    @staticmethod
    def category_bar_chart(df):

        fig = px.bar(
            df,
            x="categoria",
            y="valor",
            title="Gastos por Categoria"
        )

        return fig