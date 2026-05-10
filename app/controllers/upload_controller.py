from app.processors.csv_processor import CSVProcessor


class UploadController:

    @staticmethod
    def process_invoice(file):

        df = CSVProcessor.read_invoice(file)

        return df