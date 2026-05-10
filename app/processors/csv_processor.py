import pandas as pd


class CSVProcessor:

    @staticmethod
    def read_invoice(file):
        """
        Lê e trata a fatura CSV.
        """

        try:

            df = pd.read_csv(file)

            df = CSVProcessor.standardize_columns(df)

            df = CSVProcessor.clean_dates(df)

            df = CSVProcessor.clean_values(df)

            return df

        except Exception as e:
            raise Exception(f"Erro ao processar fatura: {str(e)}")

    @staticmethod
    def standardize_columns(df):
        """
        Padroniza nomes das colunas.
        """

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df

    @staticmethod
    def clean_dates(df):
        """
        Converte datas para datetime.
        """

        df["data"] = pd.to_datetime(
            df["data"],
            format="%d/%m/%Y"
        )

        return df

    @staticmethod
    def clean_values(df):
        """
        Converte valores monetários para float.
        """

        df["valor"] = (
            df["valor"]
            .astype(str)
            .str.replace("R$", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.replace(r"\s+", "", regex=True)
            .str.strip()
        )

        df["valor"] = pd.to_numeric(df["valor"])

        return df