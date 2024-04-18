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

    # Adapted from Real Python: Python Filter Function (https://realpython.com/python-filter-function/)

    def filter_account_summaries(self, filter_field: str, filter_value: int, filter_mode: bool) -> list:
        """
        Filters the account summaries based on the provided filter criteria.

        Args:
            filter_field (str): The field to filter on. It can be one of 'balance', 'total_deposits', or 'total_withdrawals'.
            filter_value (int): The value to compare against.
            filter_mode (bool): True for greater than or equal, False for less than or equal.

        Returns:
            list: Filtered list of account summaries.
        """
        filtered_summaries = []

        for account_number, summary in self.__account_summaries.items():
            if filter_field in summary:
                if filter_mode:
                    if summary[filter_field] >= filter_value:
                        filtered_summaries.append(summary)
                else:
                    if summary[filter_field] <= filter_value:
                        filtered_summaries.append(summary)

        return filtered_summaries

    def write_filtered_summaries_to_csv(self, filtered_data: list, file_path: str) -> None:
        """
        Writes the filtered data to a CSV file.

        Args:
            filtered_data (list): The list of filtered data.
            file_path (str): The path to the CSV file.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            # Write the header row
            writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])
            # Write each row of filtered data
            for summary in filtered_data:
                writer.writerow([
                    summary['account_number'],
                    summary['balance'],
                    summary['total_deposits'],
                    summary['total_withdrawals']
                ])