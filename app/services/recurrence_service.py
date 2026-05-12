class RecurrenceService:

    @staticmethod
    def recurring_purchases(df):

        recurring_df = (
            df.groupby("lancamento")
            .agg({
                "valor": ["count", "sum", "mean"]
            })
        )

        recurring_df.columns = [
            "quantidade",
            "valor_total",
            "ticket_medio"
        ]

        recurring_df = recurring_df.reset_index()

        recurring_df = recurring_df[
            recurring_df["quantidade"] > 1
        ]

        recurring_df = recurring_df.sort_values(
            by="quantidade",
            ascending=False
        )

        return recurring_df