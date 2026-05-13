class ProjectionService:

    @staticmethod
    def next_invoice_projection(
        subscriptions_df,
        installments_df
    ):

        subscriptions_total = 0
        installments_total = 0

        if not subscriptions_df.empty:

            subscriptions_total = (
                subscriptions_df["valor"]
                .sum()
            )

        if not installments_df.empty:

            installments_total = (
                installments_df["valor"]
                .sum()
            )

        projected_total = (
            subscriptions_total +
            installments_total
        )

        return {
            "subscriptions_total": subscriptions_total,
            "installments_total": installments_total,
            "projected_total": projected_total
        }