"""
This module contains the methods related to bank account CRUD

Business rules:
An account contains:
- agency, identified by the number (default = 0001)
- account_number

@author: Beatriz (beabea)
@date: 2025-06-03
"""

from statement import Statement

class Account:
    """User's banking account"""
    LIMIT_OF_WITHDRAWALS = 3
    LIMIT_PER_WITHDRAWAL = 500

    def __init__(self, number_id: int, user_id: str) -> None:
        self._number_id = number_id
        self._agency = "0001"
        self._balance = 0
        self._statement = Statement()
        self._user_id = user_id

    @property
    def number_id(self):
        """Returns `self._number_id`"""
        return self._number_id

    @property
    def statement(self):
        """Returns `self._statement`"""
        return self._statement

    def print_account_data(self):
        """
        Prints all account's data on the terminal with adequate formatting.

        Data includes:

        - Unique ID;
        - Agency number;
        - Balance.
        """

        try:
            print(
                f'Identificador único:\t{self._number_id}\n'
                f'Agência:\t{self._agency}\n'
                f'Saldo:\t{self._balance}'
            )

        except ValueError as e:
            print(f'ValueError: {e}')

    def withdraw_money(self, value: float):
        """
        Withdraws money from the user's account.

        The function checks if the given `value` to deposit is bigger than the minimal
        withdrawing value, if the user already exhausted their daily withdrawal limit,
        and if the balance is bigger or equal to the `value` being withdrawed.

        If all conditions are `True`, the function then subtracts the `value` from
        the `balance`, adds 1 to the `current_withdrawal_number` and calls `add_to_statement`
        to ensure that the operation will be registered on the account's `statement`.

        Params:
        @value: the amount of money to be deposited
        """

        current_withdrawal_number = len(
            [transaction for transaction in self._statement.history
             if transaction.__class__.__name__ == "Withdraw"]
        )

        below_max_daily_withdrawals = current_withdrawal_number < self.LIMIT_OF_WITHDRAWALS
        value_is_500_or_more = value >= self.LIMIT_PER_WITHDRAWAL
        saldo_bigger_than_value = self._balance >= value

        if below_max_daily_withdrawals and value_is_500_or_more and saldo_bigger_than_value:
            self._balance -= value
            current_withdrawal_number += 1
            print(f'O saque de R$ {value:.2f} foi realizado com sucesso!')
            #self._statement.add_to_statement('withdrawal', value, balance, statement)
            #return balance, current_withdrawal_number, statement

        if not below_max_daily_withdrawals:
            raise ValueError('você já excedeu o número máximo de saques diários')

        if not value_is_500_or_more:
            raise ValueError(f'o valor mínimo para realizar o saque é'
                             f'R$ {self.LIMIT_PER_WITHDRAWAL}, por favor, repita a'
                             'operação inserindo um valor de saque maior ou igual ao limite')

        if not saldo_bigger_than_value:
            raise ValueError('o saldo disponível na conta é insuficiente para realizar o saque.')

    def deposit_money(self, value: float):
        """
        Deposits money to the user's own account.

        The function checks if the given value to deposit is bigger than zero.
        If yes, adds the number to the account's balance and calls add_to_statement
        to ensure that the operation will be registered on the account's statement.

        Params:
        @balance: the account's total balance
        @value: the amount of money to be deposited
        @statement: the user's account statement
        """

        above_eq_zero = value > 0

        if above_eq_zero:
            self._balance += value
            print(f'O depósito de R$ {value:.2f} foi realizado com sucesso!')

        else:
            raise ValueError('o valor para depósito deve ser maior que zero.')

class AccountFactory:
    """Factory for `Account` objects, creating new instances of it"""

    @staticmethod
    def register_account(acc_id: int, acc_owner: str) -> Account:
        """
        Using a `while` loop, it allows the user to insert a CPF, and, if it's valid,
        verifies if it's on the user database. If not, refuses the account creation.

        Params:
        @user_arr: list of users registered in the bank app;
        @acc_arr: list of accounts existing in the bank;
        @agency_number: default agency number.
        """

        return Account(acc_id, acc_owner)
