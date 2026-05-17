class FinancialScoreService:

    @staticmethod
    def calculate_score(
        subscriptions_df,
        installments_df,
        category_summary
    ):

        score = 100

        alerts = []

        # =========================
        # ASSINATURAS
        # =========================

        subscription_count = len(subscriptions_df)

        if subscription_count >= 10:

            score -= 15

            alerts.append(
                "Alto número de assinaturas ativas."
            )

        elif subscription_count >= 5:

            score -= 8

            alerts.append(
                "Quantidade moderada de assinaturas."
            )

        # =========================
        # PARCELAMENTOS
        # =========================

        installment_count = len(installments_df)

        if installment_count >= 10:

            score -= 25

            alerts.append(
                "Muitos parcelamentos ativos."
            )

        elif installment_count >= 5:

            score -= 12

            alerts.append(
                "Quantidade moderada de parcelamentos."
            )

        # =========================
        # CONCENTRAÇÃO DE GASTOS
        # =========================

        category_percentage = (
            category_summary["percentage"]
        )

        if category_percentage >= 50:

            score -= 20

            alerts.append(
                "Grande concentração de gastos em uma única categoria."
            )

        elif category_percentage >= 35:

            score -= 10

            alerts.append(
                "Concentração moderada de gastos."
            )

        # =========================
        # LIMITES
        # =========================

        score = max(score, 0)

        # =========================
        # CLASSIFICAÇÃO
        # =========================

        if score >= 85:

            level = "Excelente"

        elif score >= 70:

            level = "Boa"

        elif score >= 50:

            level = "Atenção"

        else:

            level = "Crítica"

        return {
            "score": score,
            "level": level,
            "alerts": alerts
        }