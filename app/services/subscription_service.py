from app.config.subscriptions import SUBSCRIPTION_KEYWORDS


class SubscriptionService:

    @staticmethod
    def detect_subscriptions(df):

        subscription_rows = []

        for _, row in df.iterrows():

            launch = str(row["lancamento"]).lower()

            for keyword in SUBSCRIPTION_KEYWORDS:

                if keyword in launch:

                    subscription_rows.append(row)

                    break

        if not subscription_rows:

            return df.iloc[0:0]

        subscriptions_df = df.__class__(subscription_rows)

        return subscriptions_df