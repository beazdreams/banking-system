"""
This module contains the code for a fictional banking company,
made for DIO's Python Developer Bootcamp challenge.

@author: Beatriz (beabea)
@date: 2025-04-05
"""

# Pre-made template start

MENU = """

[d] Depositar
[s] Sacar
[x] Extrato
[e] Sair

=> """

LIMIT_PER_WITHDRAWAL = 500 # equivalent to 'limite por saque'
LIMIT_OF_WITHDRAWALS = 3 # equivalent to 'limitet de saques diários'

# Pre-made template end

def convert_str_to_float(value: str) -> float:
    """
    Attempts to convert a `str` user entry to a `float` number.

    If the conversion fails, in case it has a comma, it tries to replace
    the comma with a dot to comply with Python's `float` structure.

    """
    err_msg = (f'o valor "{value}" não é aceito '
               'pelo sistema. Insira apenas números, separando '
               'as casas decimais por vírgula ou ponto.')
    try:
        value = float(value)
        return value

    except ValueError:
        #check if value has a comma:
        if ',' in value:
            value = value.replace(',', '.')
        try:
            value = float(value)
            return value

        except ValueError as ve:
            raise ValueError(err_msg) from ve

    except TypeError as te:
        raise ValueError(err_msg) from te

def withdraw_from_account(balance: str, current_withdrawal_number: int,
                   value: float, statement: list) -> tuple:
    """
    Withdraws money from the user's account.

    The function checks if the given `value` to deposit is bigger than the minimal
    withdrawing value, if the user already exhausted their daily withdrawal limit,
    and if the balance is bigger or equal to the `value` being withdrawed.

    If all conditions are `True`, the function then subtracts the `value` from
    the `balance`, adds 1 to the `current_withdrawal_number` and calls `add_to_statement`
    to ensure that the operation will be registered on the account's `statement`.

    Params:
    @balance: the account's total balance
    @current_withdrawal_number: the number of withdrawals the user made in the current day
    @value: the amount of money to be deposited
    @statement: the user's account statement
    """

    below_max_daily_withdrawals = current_withdrawal_number < LIMIT_OF_WITHDRAWALS
    value_is_500_or_more = value >= LIMIT_PER_WITHDRAWAL
    saldo_bigger_than_value = balance >= value

    if below_max_daily_withdrawals and value_is_500_or_more and saldo_bigger_than_value:
        balance -= value
        current_withdrawal_number += 1
        print('O saque foi realizado com sucesso!')
        statement = add_to_statement('withdrawal', value, balance, statement)
        return balance, current_withdrawal_number, statement

    if not below_max_daily_withdrawals:
        raise ValueError('você já excedeu o número máximo de saques diários')

    if not value_is_500_or_more:
        raise ValueError(f'o valor mínimo para realizar o saque é R$ {LIMIT_PER_WITHDRAWAL}, '
            'por favor, repita a operação inserindo um valor de saque maior ou igual ao limite')

    if not saldo_bigger_than_value:
        raise ValueError('o saldo disponível na conta é insuficiente para realizar o saque.')

    return balance, current_withdrawal_number, statement

def deposit_to_account(balance: str, value: float, statement: list) -> tuple:
    """
    Deposits money to the user's own account.

    The function checks if the given `value` to deposit is bigger than zero.
    If yes, adds the number to the account's `balance` and calls `add_to_statement`
    to ensure that the operation will be registered on the account's `statement`.

    Params:
    @balance: the account's total balance
    @value: the amount of money to be deposited
    @statement: the user's account statement
    """
    above_eq_zero = value > 0

    if above_eq_zero:
        balance += value
        print('O depósito foi realizado com sucesso!')
        changed_statement = add_to_statement('deposit', value, balance, statement)

    else:
        raise ValueError('o valor para depósito deve ser maior que zero.')

    return balance, changed_statement

def add_to_statement(operation_type: str, value: float,
                     balance: float, statement: list) -> list:
    """
    Inserts the operation into the statement variable, registering
    it for later consulting.
    
    Params:
    @operation_type: must be either 'withdrawal' or 'deposit'
    @value: the amount of money used in the operation
    @balance: the account's total balance
    @statement: the user's account statement
    """
    if isinstance(value, float):
        pass
    else:
        raise TypeError("o valor deve ser float, e não", {type(value)})

    if isinstance(balance, (float, int)):
        pass
    else:
        raise TypeError(f"o saldo deve ser numérico, e não {type(value)}")

    if isinstance(statement, list):
        pass
    else:
        raise TypeError("o extrato deve ser uma lista (tipo `list`)")

    if isinstance(operation_type, str):
        pass
    else:
        raise TypeError(f'o tipo inserido {type(operation_type)} não é suportado.')

    if operation_type in ['withdrawal', 'deposit']:
        statement.append(
            {
                'operation_type': operation_type,
                'value': value,
                'saldo_after_operation': balance
            }
        )
    else:
        raise ValueError('o tipo de operação é inválido.')

    return statement

def print_statement(statement: list):
    """
    Prints the account's statement on the terminal with adequate formatting
    """

    prettify_names = {
        'withdrawal': 'saque',
        'deposit': 'depósito'
    }

    if len(statement) > 0:
        formatted_statement = [
            f'Operação: {prettify_names.get(ext.get("operation_type", {}), "N/A")}, '
            f'Valor da operação: {ext.get("value", 0)}, '
            f'Saldo após a operação: {ext.get("saldo_after_operation", 0)}'
            for ext in statement
        ]
        print('\n'.join(formatted_statement))
    else:
        print('Nenhuma operação feita até o momento')

def main():
    """
    Holds the main logic for the module
    """
    acc_balance = 0 # equivalent to 'saldo'
    acc_daily_withdrawals = 0 # equivalent to 'saques diários'
    acc_statement = [] # equivalent to 'extrato'

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

                    acc_balance, acc_statement = deposit_to_account(acc_balance,
                                                               deposit_value,
                                                               acc_statement)

                case 's':
                    print('Saque')
                    withdrawal_value = input('Insira o valor que será sacado:')

                    if isinstance(withdrawal_value, str):
                        withdrawal_value = convert_str_to_float(withdrawal_value)
                    if isinstance(withdrawal_value, int):
                        withdrawal_value = float(withdrawal_value)

                    acc_balance, acc_daily_withdrawals, acc_statement = withdraw_from_account(
                        acc_balance,
                        acc_daily_withdrawals,
                        withdrawal_value,
                        acc_statement
                    )

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
