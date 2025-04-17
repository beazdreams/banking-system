"""
This module verifies the CPF to ensure only a valid document can
be used to register an user and/or bank account.

@author: Beatriz (beabea)
@date: 2025-04-13
"""

def multiply_from_arr(int_arr: list[int]):
    """
    Multiplies each integer in the given list by a decreasing sequence of numbers 
    based on the list length and returns the total sum.

    The sequence starts at `len(int_arr) + 1` and decreases for each element.

    Params:
    int_arr: A list of integers to be multiplied.

    Returns:
    int: The total sum of the multiplied values.

    Example:
    >>> multiply_from_arr([2, 6, 4])
    32  # Calculation: (2 * 4) + (6 * 3) + (4 * 2)
    """
    total = 0

    num_multiply = len(int_arr) + 1

    for arr_number in int_arr:
        if not isinstance(arr_number, int):
            raise TypeError('The function only accepts int-only lists')
        math = arr_number * num_multiply
        total += math
        num_multiply -= 1

    return total

def generate_verification_digit(total_multiply: int):
    """
    Generates the verification digit for a Brazilian CPF number based on the given 
    `total_multiply` value.

    Params:
    total_multiply: The total sum obtained from the `multiply_from_arr` function.

    Returns:
    int: The computed verification digit.

    Example:
    >>> generate_verification_digit(34)
    7  # Calculation: 11 - (34 % 11)
    """

    mod_eleven = total_multiply % 11

    if mod_eleven < 2:
        return 0
    verify_value = 11 - mod_eleven
    return verify_value

def main(cpf: str) -> bool:
    """Verifies if a CPF is valid, and returns `True` if so.
    
    Params:
    @cpf: the evaluated CPF, without punctuation
    """

    if isinstance(cpf, int):
        cpf = str(cpf)

    full_cpf_list = [int(char) for char in cpf]

    multiplication_result_d1 = multiply_from_arr(full_cpf_list[0:9])

    given_d1 = full_cpf_list[9]
    generated_d1 = generate_verification_digit(multiplication_result_d1)

    compare_d1 = given_d1 == generated_d1

    multiplication_result_d2 = multiply_from_arr(full_cpf_list[0:10])

    given_d2 = full_cpf_list[10]
    generated_d2 = generate_verification_digit(multiplication_result_d2)

    compare_d2 = given_d2 == generated_d2

    if compare_d1 and compare_d2:
        return True
    return False
