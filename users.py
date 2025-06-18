"""
This module contains the methods related to user CRUD

@author: Beatriz (beabea)
@date: 2025-04-13
"""

import datetime
from account import Account

class User:
    """
    Defines and instantiates a User
    """
    def __init__(self, cpf: str, name: str, birth_date: datetime.date,
                 address: str, house_number: str, neighbourhood: str,
                 city: str, uf: str) -> None:
        self._cpf = cpf
        self._name = name
        self._birth_date = birth_date
        self._address = address # logradouro
        self._house_number = house_number # número da casa
        self._neighbourhood = neighbourhood # bairro de residência
        self._city = city # cidade de residência
        self._uf = uf # UF do Estado
        self._accounts:list[Account] = []

    @property
    def cpf(self):
        """Returns `self._cpf`"""
        return self._cpf

    @property
    def name(self):
        """Returns `self._name`"""
        return self._name

    @property
    def full_address(self):
        """
        Formats the address according to the business rules.
        """
        return (f'{self._address} - {self._house_number}'
                f' - {self._neighbourhood} - '
                f'{self._city}/{self._uf}')

    def print_account_list(self):
        """
        Prints all account's data on the terminal with adequate formatting.

        Uses a `Account` print method to print account data for each account
        in the `_accounts` User list.
        """

        print(f'Imprimindo informações da(s) conta(s) de {self._name}')

        if len(self._accounts) >= 1:
            for account in self._accounts:
                account.print_account_data()
                print('\n')
        else:
            print('Nenhuma conta registrada até o momento')

    def print_user_info(self):
        """
        Prints the user's data on the terminal with adequate formatting
        """

        print(
            f'Nome:\t{self._name}\n'
            f'CPF:\t{self._cpf}\n'
            f'Endereço:\t{self.full_address}'
        )

class UserFactory:
    """Factory class for creating users"""

    @classmethod
    def _validate_uf(cls, user_uf: str) -> bool:
        """
        Checks if the UF input is valid and returns `True` if yes, `False` if no.

        Params:

        """
        brazil_uf = [
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
            "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
            "RS", "RO", "RR", "SC", "SP", "SE", "TO"
        ]

        if user_uf in brazil_uf:
            return True
        return False

    @classmethod
    def _register_birth_date(cls) -> datetime.date:
        """
        Registers the user's birth date, using a `while` loop to ensure that the
        user can't break if the date is invalid.
        """
        while True:
            try:
                user_birth_date = input("Informe a data de nascimento (dd-mm-aaaa): ")
                user_birth_date = datetime.datetime.strptime(user_birth_date, "%d-%m-%Y").date()
                return user_birth_date

            except ValueError as e:
                print(f'ValueError: a data inserida é inválida!\n{e}')

    @classmethod
    def _register_state_uf(cls) -> str:
        """
        Registers the user's state UF, using a `while` loop to ensure that the
        user can't break if the value is invalid.
        """
        while True:
            try:
                user_uf = input('Informe o Estado de residência (UF, apenas dois caracteres): ')
                uf_is_valid = cls._validate_uf(user_uf)
                if len(user_uf) != 2:
                    raise ValueError('UF deve conter dois caracteres')
                if not uf_is_valid:
                    raise ValueError('os caracteres inseridos não correspondem a nenhum '
                                        'Estado brasileiro')
                return user_uf
            except ValueError as e:
                print(f'ValueError: {e}')

    @staticmethod
    def create_user(user_cpf: str) -> User:
        """
        When triggered, starts the process of banking user creation, asking the user
        information such as CPF, full name, birth date and address.

        In this procedural programming form, the data is stored in a list, taken by
        this function as the `user_arr` argument. If the CPF already exists in the
        list, the program will print a message pointing that, and allow the user to
        input another CPF.

        If the CPF is not in the database, the user can follow the registration flow.
        The function validates the date and UF input to ensure no invalid values are
        inserted to the database.

        Params:
        @user_arr: the list used as user database
        """

        while True:
            try:
                user_name = input("Informe o nome completo: ")

                user_birth_date = UserFactory._register_birth_date()

                user_address = input("informe o logradouro de residência: ")
                user_house_number = input("Informe o número da casa: ")
                user_neighbourhood = input("Informe o bairro de residência: ")
                user_city = input("Informe a cidade de residência: ")

                user_uf = UserFactory._register_state_uf()

                return User(cpf=user_cpf, name=user_name, birth_date=user_birth_date,
                           address=user_address, house_number=user_house_number,
                           neighbourhood=user_neighbourhood, city=user_city, uf=user_uf)

            except ValueError as e:
                print(f'ValueError: {e}')

            except TypeError as e:
                print(f'TypeError: {e}')

            except NameError as e:
                print(f'NameError: {e}')
