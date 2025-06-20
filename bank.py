"""
This module contains banking methods.
"""

from cpf_validator import CPFValidator
from users import User, UserFactory
from account import Account

class Bank:
    """Singleton representing the Bank"""

    MENU = """

    [d]\tDepositar
    [s]\tSacar
    [c]\tCadastrar conta corrente
    [u]\tCadastrar usuário
    [x]\tExtrato
    [lu]\tListar usuários cadastrados
    [lc]\tListar contas corrente
    [e]\tSair

    => """

    def __init__(self) -> None:
        self._user_list: list[User] = []
        self._account_list: list[Account] = []

    @staticmethod
    def _insert_cpf() -> tuple[str, bool]:
        user_cpf = input("Insira o CPF do usuário que deseja cadastrar: ")
        is_valid = CPFValidator.main(user_cpf)

        if is_valid:
            user_cpf = CPFValidator.remove_punctuation_from_cpf(user_cpf)
            return user_cpf, True
        return '', False

    def find_user_in_database(self, user_cpf: str):
        """'
        Finds the user's data in the user list database
        """

        found_user = [user for user in self._user_list if user.cpf == user_cpf]

        return found_user if found_user else []

    def create_user(self):
        """
        When triggered, starts the process of banking user creation, asking the user
        information such as CPF, full name, birth date and address.

        In this Object Oriented Programming object, all instances of `User` are stored
        in the `Bank`'s `_user_list`. The function checks if the CPF already exists in
        the list. If yes, the program will print a message pointing that, and allow the
        user to input another CPF.

        If the CPF is not in the database, the user can follow the registration flow.
        The function validates the date and UF input to ensure no invalid values are
        inserted to the database.
        """

        while True:
            try:
                user_cpf, is_valid = self._insert_cpf()

                if is_valid:
                    find_user = self.find_user_in_database(user_cpf)

                    if len(find_user) > 0:
                        # if a list is returned, then, user exists:
                        raise ValueError('um usuário com este CPF já existe na base de dados.')

                    new_user = UserFactory.create_user(user_cpf=user_cpf)
                    self._user_list.append(new_user)

                    print("Usuário cadastrado com sucesso!")

                    break

            except ValueError as e:
                print(f'ValueError: {e}')

            except TypeError as e:
                print(f'TypeError: {e}')

            except NameError as e:
                print(f'NameError: {e}')

    def main(self) -> None:
        """Allows the user to select their desired option in a menu"""
        while True:
            options = input(self.MENU)

            try:
                match options:
                    case 'u':
                        print('Cadastrar usuário')
                        self.create_user()
                    case _:
                        print('Opção inválida, por favor, selecione'
                            'novamente a operação desejada')

            except TypeError as e:
                print(f'TypeError: {e}')
                print('Tente novamente:')

            except ValueError as e:
                print(f'ValueError: {e}')
                print('Tente novamente:')

if __name__ == "__main__":
    bank = Bank()

    bank.main()
