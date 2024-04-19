import sys
import os
sys.path.append(r"C:\Users\Inti\OneDrive\Desktop\courses\software_development_fundamentals\projects\assignment_7\P7\financial_data_processor")
import unittest
from unittest import TestCase 
from unittest.mock import mock_open, patch, Mock
from input_handler.input_handler import InputHandler

class TestInputHandler(TestCase):
    
    def setUp(self):
        self.handler_with_extension = InputHandler('example.csv')
        self.handler_without_extension = InputHandler('example')
        self.handler_valid_csv = InputHandler('valid.csv')
        self.handler_empty_csv = InputHandler('empty.csv')
        self.handler_missing_csv = InputHandler('missing.csv')
        self.handler_invalid_extension = InputHandler('invalid.txt')

    def test_get_file_format_with_extension(self):
        """Verify that the correct file extension is returned."""
        self.assertEqual(self.handler_with_extension.get_file_format(), 'csv')      

    def test_get_file_format_without_extension(self):
        """Verify that an empty string is returned when there is no file extension."""
        self.assertEqual(self.handler_without_extension.get_file_format(), '')

    def test_read_csv_data_with_data(self):
        """Verify that a populated list is returned from a valid CSV file."""
        mock_data = "name,age\nJohn,30\nJane,25"
        with patch('builtins.open', mock_open(read_data=mock_data), create=True):
            data = self.handler_valid_csv.read_csv_data()
            self.assertEqual(len(data), 2)

    def test_read_csv_data_empty_file(self):
        """Verify that an empty list is returned from an empty CSV file."""
        with patch('builtins.open', mock_open(read_data=''), create=True):
            data = self.handler_empty_csv.read_csv_data()
            self.assertEqual(data, [])

    def test_read_csv_data_file_not_found(self):
        """Verify that FileNotFoundError is raised for a non-existent CSV file."""
        with patch('builtins.open', Mock(side_effect=FileNotFoundError), create=True):
            with self.assertRaises(FileNotFoundError):
                self.handler_missing_csv.read_csv_data()

    def test_read_input_data_valid_csv(self):
        """Verify that a populated list is returned when a valid CSV file is used."""
        mock_data = "name,age\nJohn,30\nJane,25"
        with patch('builtins.open', mock_open(read_data=mock_data), create=True):
            data = self.handler_valid_csv.read_input_data()
            self.assertEqual(len(data), 2)

    def test_read_input_data_invalid_extension(self):
        """Verify that ValueError is raised when a file with an invalid extension is used."""
        with self.assertRaises(ValueError):
            self.handler_invalid_extension.read_input_data()

if __name__ == "__main__":
    unittest.main()
