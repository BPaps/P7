import csv

class OutputHandler:
    """
     Handles writing transaction data to CSV files.
    
    Attributes:
        account_summaries (dict): A dictionary containing account summaries.
        suspicious_transactions (list): A list of suspicious transactions.
        transaction_statistics (dict): A dictionary containing transaction statistics.
    """

    def __init__(self, account_summaries: dict, 
                       suspicious_transactions: list, 
                       transaction_statistics: dict) -> None:
        """
        Initializes the OutputHandler with transaction data.

        Args:
            account_summaries (dict): A dictionary containing account summaries.
            suspicious_transactions (list): A list of suspicious transactions.
            transaction_statistics (dict): A dictionary containing transaction statistics.
        """
        self.__account_summaries = account_summaries
        self.__suspicious_transactions = suspicious_transactions
        self.__transaction_statistics = transaction_statistics
    
    @property
    def account_summaries(self):
        """
         Getter method for account summaries.

        Returns:
            dict: Account summaries.
        """
        return self.__account_summaries
    
    @property
    def suspicious_transactions(self):
        """
        Getter method for suspicious transactions.

        Returns:
            list: Suspicious transactions.
        """
        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self):
        """
        Getter method for transaction statistics.

        Returns:
            dict: Transaction statistics.
        """
        return self.__transaction_statistics

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """
        Writes account summaries to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

            for account_number, summary in self.__account_summaries.items():
                writer.writerow([
                    account_number,
                    summary['balance'],
                    summary['total_deposits'],
                    summary['total_withdrawals']
                ])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """
         Writes suspicious transactions to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction ID', 'Account number', 'Date', 'Transaction type', 'Amount', 'Currency', 'Description'])

            for transaction in self.__suspicious_transactions:
                writer.writerow([
                    transaction['Transaction ID'],
                    transaction['Account number'],
                    transaction['Date'],
                    transaction['Transaction type'],
                    transaction['Amount'],
                    transaction['Currency'],
                    transaction['Description']
                ])

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """
        Writes transaction statistics to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
        """        
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction type', 'Total amount', 'Transaction count'])

            for transaction_type, statistic in self.__transaction_statistics.items():
                writer.writerow([
                    transaction_type,
                    statistic['total_amount'],
                    statistic['transaction_count']
                ])