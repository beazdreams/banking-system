"""
This module contains the code for a fictional banking company,
made for DIO's Python Developer Bootcamp challenge.

@author: Beatriz (beabea)
@date: 2025-04-05
"""

from banking_methods import deposit_money, withdraw_money, print_statement, convert_str_to_float
from users import main as create_user
from account import register_account

# Pre-made template start

MENU = """

[d] Depositar
[s] Sacar
[c] Cadastrar conta corrente
[u] Cadastrar usuário
[x] Extrato
[e] Sair

=> """

# Pre-made template end

def main():
    """
    Holds the main logic for the module
    """
    acc_balance = 0 # equivalent to 'saldo'
    acc_daily_withdrawals = 0 # equivalent to 'saques diários'
    acc_statement = [] # equivalent to 'extrato'
    user_database = []
    account_database = []

    while True:
        options = input(MENU)

        try:
            match options:
                case 'd':
                    print('Depósito')
                    deposit_value = input('Insira o valor que será depositado:')

                    if isinstance(deposit_value, str):
                        deposit_value = convert_str_to_float(deposit_value)
                    if isinstance(deposit_value, int):
                        deposit_value = float(deposit_value)

                    acc_balance, acc_statement = deposit_money(acc_balance,
                                                               deposit_value,
                                                               acc_statement)

                case 's':
                    print('Saque')
                    withdrawal_value = input('Insira o valor que será sacado:')

                    if isinstance(withdrawal_value, str):
                        withdrawal_value = convert_str_to_float(withdrawal_value)
                    if isinstance(withdrawal_value, int):
                        withdrawal_value = float(withdrawal_value)

                    acc_balance, acc_daily_withdrawals, acc_statement = withdraw_money(
                        acc_balance,
                        acc_daily_withdrawals,
                        withdrawal_value,
                        acc_statement
                    )

                case 'c':
                    print('Cadastrar conta bancária')
                    account_database = register_account(
                        user_arr=user_database,
                        acc_arr=account_database)

                case 'u':
                    print('Cadastrar usuário')
                    user_database = create_user(user_database)

                case 'x':
                    print('Extrato')
                    print_statement(acc_statement)

                case 'e':
                    print('Agradecemos a preferência!')
                    break

                case _:
                    print('Opção inválida, por favor, selecione'
                        'novamente a operação desejada')

        except TypeError as e:
            print(f'TypeError: {e}')
            print('Tente novamente:')

        except ValueError as e:
            print(f'ValueError: {e}')
            print('Tente novamente:')

if __name__ == '__main__':
    main()
