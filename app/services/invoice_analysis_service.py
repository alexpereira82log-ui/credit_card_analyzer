class InvoiceAnalysisService:

    @staticmethod
    def get_analysis_dataframe(df):
        """
        Retorna apenas transações válidas para análise financeira.
        """

        excluded_transactions = [
            "PAGAMENTO DE FATURA"
        ]

        analysis_df = df[
            ~df["lancamento"].isin(excluded_transactions)
        ].copy()

        return analysis_df

    @staticmethod
    def calculate_total(df):

        return df["valor"].sum()

    @staticmethod
    def calculate_transaction_count(df):

        return df.shape[0]

    @staticmethod
    def calculate_average_ticket(df):

        return df["valor"].mean()

    @staticmethod
    def expenses_by_category(df):

        category_df = (
            df.groupby("categoria")["valor"]
            .sum()
            .reset_index()
            .sort_values(by="valor", ascending=False)
        )

        return category_df

    @staticmethod
    def top_expenses(df, limit=10):

        top_df = (
            df.sort_values(by="valor", ascending=False)
            .head(limit)
        )

        return top_df
    
    @staticmethod
    def biggest_expense(df):

        return df.loc[df["valor"].idxmax()]

    @staticmethod
    def category_summary(df):

        category_df = (
            df.groupby("categoria")["valor"]
            .sum()
            .reset_index()
        )

        top_category = category_df.sort_values(
            by="valor",
            ascending=False
        ).iloc[0]

        total = category_df["valor"].sum()

        percentage = (top_category["valor"] / total) * 100

        return {
            "category": top_category["categoria"],
            "value": top_category["valor"],
            "percentage": percentage
        }