"""
This module contains banking methods.
"""

from cpf_validator import CPFValidator
from users import User
from account import Account

class Bank:
    """Singleton representing the Bank"""
    def __init__(self) -> None:
        self._user_list: list[User] = []
        self._account_list: list[Account] = []
