"""
This module contains the methods related to user CRUD

@author: Beatriz (beabea)
@date: 2025-04-13
"""

import datetime
from cpf_validator import CPFValidator
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

    @classmethod
    def find_user_in_database(cls, user_arr: list, user_cpf: str):
        """'
        Finds the user's data in the user list database
        """

        found_user = [user for user in user_arr if user.cpf == user_cpf]

        return found_user if found_user else []

    @classmethod
    def main(cls, user_arr: list):
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
                user_cpf = input("Insira o CPF do usuário que deseja cadastrar: ")
                is_valid = CPFValidator.main(user_cpf)

                if is_valid:
                    user_cpf = CPFValidator.remove_punctuation_from_cpf(user_cpf)
                    find_user = User.find_user_in_database(user_arr, user_cpf)

                    if len(find_user) > 0:
                        # if a list is returned, then, user exists:
                        raise ValueError('um usuário com este CPF já existe na base de dados.')

                    user_name = input("Informe o nome completo: ")

                    user_birth_date = User._register_birth_date()

                    user_address = input("informe o logradouro de residência: ")
                    user_house_number = input("Informe o número da casa: ")
                    user_neighbourhood = input("Informe o bairro de residência: ")
                    user_city = input("Informe a cidade de residência: ")

                    user_uf = User._register_state_uf()

                    user = User(cpf=user_cpf, name=user_name, birth_date=user_birth_date,
                                address=user_address, house_number=user_house_number,
                                neighbourhood=user_neighbourhood, city=user_city, uf=user_uf)
                    user_arr.append(user)

                    print("Usuário cadastrado com sucesso!")
                    return user_arr

            except Exception as e:
                print(e)

    @classmethod
    def print_user_list(cls, user_database: list):
        """
        Prints the user's data on the terminal with adequate formatting
        """

        if len(user_database) > 0:
            formatted_user_database = [
                f'Nome:\t{ext.name}\n'
                f'CPF:\t{ext.cpf}\n'
                f'Endereço:\t{ext.full_address}'
                for ext in user_database
            ]
            print('\n'.join(formatted_user_database))
        else:
            print('Nenhum usuário cadastrado até o momento')
