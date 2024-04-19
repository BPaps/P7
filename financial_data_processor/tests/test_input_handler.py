import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open
from input_handler.input_handler import InputHandler

class InputHandlerTests(TestCase):
    """Test cases for the InputHandler class."""

    # Sample file contents for testing
    FILE_CONTENTS = ("Transaction ID,Account number,Date,Transaction type,"
                     + "Amount,Currency,Description\n"
                     + "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
                     + "2,1002,2023-03-01,deposit,1500,CAD,Salary\n"
                     + "3,1001,2023-03-02,withdrawal,200,CAD,Groceries") 

    # Test case to verify that the extension is returned when the file has a proper extension
    def test_get_file_format_with_proper_extension(self):
        input_handler = InputHandler("test.csv")
        self.assertEqual(input_handler.get_file_format(), "csv")

    # Test case to verify that an empty string is returned when the file does not have an extension
    def test_get_file_format_without_extension(self):
        input_handler = InputHandler("test")
        self.assertEqual(input_handler.get_file_format(), "")

    # Test case to verify that a populated list is returned when the .csv file exists and contains data
    def test_read_csv_data_with_existing_file_and_data(self):
        with patch("builtins.open", mock_open(read_data=self.FILE_CONTENTS)):
            input_handler = InputHandler("test.csv")
            data = input_handler.read_csv_data()
            self.assertEqual(len(data), 3)  # Assuming there are 3 records in the test data

    # Test case to verify that an empty list is returned when the .csv file exists, but is empty
    def test_read_csv_data_with_existing_empty_file(self):
        with patch("builtins.open", mock_open(read_data="")):
            input_handler = InputHandler("test.csv")
            data = input_handler.read_csv_data()
            self.assertEqual(len(data), 0)

    # Test case to verify that a FileNotFoundError exception is raised when the .csv file does not exist
    def test_read_csv_data_with_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            input_handler = InputHandler("non_existing.csv")
            input_handler.read_csv_data()

    # Test case to verify that a populated list is returned when a valid .csv file is used
    def test_read_input_data_with_valid_csv_file(self):
        with patch("builtins.open", mock_open(read_data=self.FILE_CONTENTS)):
            input_handler = InputHandler("test.csv")
            data = input_handler.read_input_data()
            self.assertEqual(len(data), 3)  # Assuming there are 3 records in the test data

    # Test case to verify that an empty list is returned when a file with an invalid extension is used
    def test_read_input_data_with_invalid_extension(self):
        input_handler = InputHandler("test.txt")  # Assuming .txt is an invalid extension
        data = input_handler.read_input_data()
        self.assertEqual(len(data), 0)

if __name__ == "__main__":
    unittest.main()
