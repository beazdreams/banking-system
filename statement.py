"""
This module contains the Statement class
@author: Beatriz
@date: 08-06-2025
"""

from banking_methods import Transaction

class Statement:
    """
    Contains the banking account's historical data about transactions.
    """
    def __init__(self) -> None:
        self._history: list = []

    @property
    def history(self) -> list:
        """
        Returns the private value `_history`
        """
        return self._history

    def add(self, transaction: Transaction):
        """
        Inserts the operation into the statement variable, registering
        it for later consulting.
        
        Params:
        @transaction: the transaction to be added to the statement
        """
        if isinstance(transaction.value, float):
            pass
        else:
            raise TypeError("o valor deve ser float, e não", {type(transaction.value)})

        if isinstance(transaction, Transaction):
            pass
        else:
            raise TypeError(f'o tipo inserido {type(transaction)} não é suportado.')

        self._history.append(transaction)

    def print_statement(self):
        """
        Prints the account's statement on the terminal with adequate formatting
        """

        if len(self._history) > 0:
            for transaction in self._history:
                transaction.print_transaction_details()
                print('\n')
        else:
            print('Nenhuma operação feita até o momento')
