import re
import pandas as pd


class InstallmentService:

    @staticmethod
    def detect_installments(df):

        installment_rows = []

        pattern = r"(\d{1,2})/(\d{1,2})"

        for _, row in df.iterrows():

            installment_type = str(row["tipo"])

            match = re.search(pattern, installment_type)

            if match:

                current_installment = int(match.group(1))
                total_installments = int(match.group(2))

                remaining_installments = (
                    total_installments - current_installment
                )

                installment_data = row.to_dict()

                installment_data["parcela_atual"] = current_installment

                installment_data["total_parcelas"] = total_installments

                installment_data["parcelas_restantes"] = (
                    remaining_installments
                )

                installment_data["comprometimento_futuro"] = (
                    remaining_installments * row["valor"]
                )

                installment_rows.append(installment_data)

        if not installment_rows:

            return pd.DataFrame()

        installments_df = pd.DataFrame(installment_rows)

        installments_df = installments_df.sort_values(
            by="parcelas_restantes",
            ascending=False
        )

        return installments_df