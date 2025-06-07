"""
This module contains the methods related to bank account CRUD

Business rules:
An account contains:
- agency, identified by the number (default = 0001)
- account_number

@author: Beatriz (beabea)
@date: 2025-06-03
"""

from typing import Any
from cpf_validator import main as verify_cpf, remove_punctuation_from_cpf as format_cpf

def register_account(user_arr: list[dict[str, Any]],
                     acc_arr: list[dict[str, Any]],
                     agency_number: str="0001") -> list[dict[str, Any]]:
    """
    Using a `while` loop, it allows the user to insert a CPF, and, if it's valid,
    verifies if it's on the user database. If not, refuses the account creation.

    Params:
    @user_arr: list of users registered in the bank app;
    @acc_arr: list of accounts existing in the bank;
    @agency_number: default agency number.
    """

    while True:
        account_owner_cpf = input("Insira o CPF do dono da conta a ser criada: ")

        is_valid = verify_cpf(account_owner_cpf)

        if is_valid:
            account_owner_cpf = format_cpf(account_owner_cpf)

        find_user_in_user_db = [user for user in user_arr
                                if user.get('cpf', None) == account_owner_cpf]

        if len(find_user_in_user_db) == 0:
            # if a list is returned, then, user exists:
            raise ValueError('um usuário com este CPF não existe na base de dados.')

        account:dict[str, str|int] = {
            "id": 1 if acc_arr == [] else len(acc_arr) + 1,
            "agency": agency_number,
            "user": account_owner_cpf
        }

        acc_arr.append(account)

        print(f"Conta de ID {account.get('id', None)} foi criada para "
            f"o usuário de CPF {account_owner_cpf}")

        return acc_arr
