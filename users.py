"""
This module contains the methods related to user CRUD

@author: Beatriz (beabea)
@date: 2025-04-13
"""

import datetime
from cpf_validator import main as verify_cpf

def validate_uf(user_uf: str) -> bool:
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

def register_birth_date() -> datetime.date:
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

def register_state_uf() -> str:
    """
    Registers the user's state UF, using a `while` loop to ensure that the
    user can't break if the value is invalid.
    """
    while True:
        try:
            user_uf = input('Informe o Estado de residência (UF, apenas dois caracteres): ')
            uf_is_valid = validate_uf(user_uf)
            if len(user_uf) != 2:
                raise ValueError('UF deve conter dois caracteres')
            if not uf_is_valid:
                raise ValueError('os caracteres inseridos não correspondem a nenhum '
                                    'Estado brasileiro')
            return user_uf
        except ValueError as e:
            print(f'ValueError: {e}')


def main(user_arr: list):
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
            print(user_cpf)
            is_valid = verify_cpf(user_cpf)

            if is_valid:
                find_user = [user for user in user_arr if user.get('cpf', None) == user_cpf]

                if len(find_user) > 0:
                    # if a list is returned, then, user exists:
                    raise ValueError('um usuário com este CPF já existe na base de dados.')

                user_name = input("Informe o nome completo: ")

                user_birth_date = register_birth_date()

                user_address = input("informe o logradouro de residência: ")
                user_house_number = input("Informe o número da casa: ")
                user_neighbourhood = input("Informe o bairro de residência: ")
                user_city = input("Informe a cidade de residência: ")

                user_uf = register_state_uf()

                user_arr.append(
                    {
                        'cpf': user_cpf,
                        'name': user_name,
                        'birth_date': user_birth_date,
                        'house_number': user_house_number,
                        'address': user_address,
                        'neighbourhood': user_neighbourhood,
                        'city': user_city,
                        'state_uf': user_uf,
                        'full_address': (f'{user_address} - {user_house_number}'
                                         f' - {user_neighbourhood} - '
                                         f'{user_city}/{user_uf}')
                    }
                )

                print("Usuário cadastrado com sucesso!")
                return user_arr

        except Exception as e:
            print(e)
