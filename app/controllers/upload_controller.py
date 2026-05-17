from app.processors.csv_processor import CSVProcessor
from app.services.invoice_analysis_service import InvoiceAnalysisService
from app.services.recurrence_service import RecurrenceService
from app.services.subscription_service import SubscriptionService
from app.services.installment_service import InstallmentService
from app.services.projection_service import ProjectionService
from app.services.financial_score_service import (
    FinancialScoreService
)


class UploadController:

    @staticmethod
    def process_invoice(file):

        df = CSVProcessor.read_invoice(file)

        analysis_df = InvoiceAnalysisService.get_analysis_dataframe(df)

        subscriptions_df = SubscriptionService.detect_subscriptions(
            analysis_df
        )

        installments_df = InstallmentService.detect_installments(
            analysis_df
        )

        category_summary = (
            InvoiceAnalysisService.category_summary(
                analysis_df
            )
        )

        analysis = {
            "total": InvoiceAnalysisService.calculate_total(analysis_df),

            "transaction_count": InvoiceAnalysisService.calculate_transaction_count(
                analysis_df
            ),

            "average_ticket": InvoiceAnalysisService.calculate_average_ticket(
                analysis_df
            ),

            "expenses_by_category": InvoiceAnalysisService.expenses_by_category(
                analysis_df
            ),

            "top_expenses": InvoiceAnalysisService.top_expenses(
                analysis_df
            ),

            "biggest_expense": InvoiceAnalysisService.biggest_expense(
                analysis_df
            ),

            "category_summary": category_summary,

            "recurring_purchases": RecurrenceService.recurring_purchases(
                analysis_df
            ),

            "subscriptions": subscriptions_df,

            "installments": installments_df,

            "projection": ProjectionService.next_invoice_projection(
                subscriptions_df,
                installments_df
            ),

            "financial_score": FinancialScoreService.calculate_score(
                subscriptions_df,
                installments_df,
                category_summary
            )
        }

        return df, analysis