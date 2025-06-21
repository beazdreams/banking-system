"""
This module contains the core methods for banking operations,
such as withdrawing money, depositing money, and printing the statement.

@author: Beatriz (beabea)
@date: 2025-04-05
"""
from abc import ABC
from datetime import datetime

LIMIT_PER_WITHDRAWAL = 500 # equivalent to 'limite por saque'
LIMIT_OF_WITHDRAWALS = 3 # equivalent to 'limitet de saques diários'

class Transaction(ABC):
    """
    This abstract class defines the base for banking transactions
    """

    def __init__(self, value: float):
        self._value = value
        self._date = datetime.now()

    @property
    def value(self):
        """Returns the transaction's `_value`"""
        return self._value

    @property
    def date(self):
        """Returns the transaction's `_date`"""
        return self._date

    def print_transaction_details(self) -> None:
        """Prints all data regarding to a `Transaction` object"""

        prettify_names = {
            'Withdrawal': 'saque',
            'Deposit': 'depósito'
        }

        print(
            f'Operação: {prettify_names.get((self.__class__.__name__), "N/A")}\n'
            f'Valor da operação:\tR$ {self._value:.2f}\n'
            f'Data da operação:\t{self._date.strftime("%d-%m-%Y %H:%M:%s")}'
        )

class Withdraw(Transaction):
    """
    Withdrawing methods
    """

class Deposit(Transaction):
    """
    Depositing methods
    """
