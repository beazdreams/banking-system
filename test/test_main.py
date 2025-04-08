"""
This module contains the code for a fictional banking company,
made for DIO's Python Developer Bootcamp challenge.

@author: Beatriz (beabea)
@date: 2025-04-05
"""

import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(
    0, os.path.abspath(
        os.path.join(os.path.dirname(__file__),'..')
    )
)

from main import convert_str_to_float, add_to_statement, deposit_money, withdraw_money, print_statement

class TestBaseMethods(unittest.TestCase):
    """Tests the helper methods in the `main` module"""
    def test_convert_str_to_float(self):
        """
        Tests the `convert_str_to_float` method
        """
        test1 = convert_str_to_float('500,50')
        test2 = convert_str_to_float(500)
        test3 = convert_str_to_float('5.5')

        list_tests = [
            (test1, 500.50),
            (test2, 500.0),
            (test3, 5.5)
        ]

        for test in list_tests:
            self.assertEqual(
                test[0], test[1],
                f'Error: function value {test[0]} is not equal to expected {test[1]}'
            )

    def test_add_to_statement(self):
        """
        Tests the `add_to_statement` method
        """
        statement1_initial = []

        statement1_final = [
            {
                'operation_type': 'withdrawal',
                'value': 500,
                'saldo_after_operation': 1500
            }
        ]

        self.assertEqual(
            statement1_final,
            add_to_statement('withdrawal', 500.0, 1500.0, statement1_initial)
        )

        statement2_initial = [
            {
                'operation_type': 'deposit',
                'value': 500,
                'saldo_after_operation': 1500
            }
        ]

        statement2_final = [
            {
                'operation_type': 'deposit',
                'value': 500,
                'saldo_after_operation': 1500
            },
            {
                'operation_type': 'deposit',
                'value': 1500,
                'saldo_after_operation': 3000
            }
        ]

        self.assertEqual(
            statement2_final,
            add_to_statement('deposit', 1500.0, 3000.0, statement2_initial)
        )


class TestBankMethods(unittest.TestCase):
    """Tests the main functions, belonging to the business rules"""

    LIMIT_PER_WITHDRAWAL = 500 # equivalent to 'limite por saque'
    LIMIT_OF_WITHDRAWALS = 3 # equivalent to 'limitet de saques diários'

    def test_deposit_money(self):
        """Test the money deposit method"""

        print('Test deposit method:')
        mock_balance = 5000.0
        mock_statement = []

        test1 = deposit_money(mock_balance, 500.0, mock_statement)

        test1_expected_balance = 5500.0
        test1_expected_statement = [
            {
                'operation_type': 'deposit',
                'value': 500.0,
                'saldo_after_operation': test1_expected_balance
            }
        ]

        self.assertEqual(
            test1,
            (test1_expected_balance, test1_expected_statement),
            (f"Expected result for test1 was {(test1_expected_balance, test1_expected_statement)}, "
            f"instead, the function returned: {test1}"))

        test2 = deposit_money(
            test1_expected_balance,
            1500.90000000000000000000000000000000000009,
            test1_expected_statement
        )

        test2_expected_balance = 7000.90000000000000000000000000000000000009
        test2_expected_statement = [
            {
                'operation_type': 'deposit',
                'value': 500.0,
                'saldo_after_operation': test1_expected_balance
            },
            {
                'operation_type': 'deposit',
                'value': 1500.90000000000000000000000000000000000009,
                'saldo_after_operation': test2_expected_balance
            }
        ]

        self.assertEqual(
            test2,
            (test2_expected_balance, test2_expected_statement),
            (f"Expected result for test2 was {(test2_expected_balance, test2_expected_statement)}, "
            f"instead, the function returned: {test2}"))

    def test_withdraw_money(self):
        """Test the money withdrawal method"""

        print('\nTest withdraw method:')
        mock_balance = 5000.0
        mock_statement = []
        mock_daily_withdrawals = 1

        test1 = withdraw_money(
            mock_balance, mock_daily_withdrawals, 500.0, mock_statement
        )

        test1_expected_balance = 4500.0
        test1_expected_withdrawals = 2
        test1_expected_statement = [
            {
                'operation_type': 'withdrawal',
                'value': 500.0,
                'saldo_after_operation': test1_expected_balance
            }
        ]

        self.assertEqual(
            test1,
            (test1_expected_balance, test1_expected_withdrawals, test1_expected_statement),
            ("Expected result for test1 was "
             f"{(test1_expected_balance, test1_expected_withdrawals, test1_expected_statement)}, "
             f"instead, the function returned: {test1}"))

    @patch('builtins.print')  # Substitui a função print
    def test_print_statement(self, mock_print):
        """Test the `print_statement` method"""

        mock_statement = [
            {
                'operation_type': 'deposit',
                'value': 500.0,
                'saldo_after_operation': 1000.0
            },
            {
                'operation_type': 'deposit',
                'value': 1500.90000000000000000000000000000000000009,
                'saldo_after_operation': 2500.90000000000000000000000000000000000009
            }
        ]

        print_statement(mock_statement)

        expected_result = ("Operação: depósito, Valor da operação: R$ 500.00, "
                           "Saldo após a operação: R$ 1000.00\n"
                           "Operação: depósito, Valor da operação: R$ 1500.90, "
                           "Saldo após a operação: R$ 2500.90")

        mock_print.assert_called_once_with(expected_result)

if __name__ == '__main__':
    unittest.main()
