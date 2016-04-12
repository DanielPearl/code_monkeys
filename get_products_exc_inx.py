# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
#
# For example, given:
#  [1, 7, 3, 4]
# your function would return:
#  [84, 12, 28, 21]
# by calculating:
#  [7*3*4, 1*3*4, 1*7*4, 1*7*3]
# Do not use division in your solution.

int_list = [1,7,3,4]

def mult_index(int_list):
    """
    Multiplies ints in a list
    :param int_list: list
    :return: int
    """
    product = 1
    for i in int_list:
        product *= i
    return product

def get_products_exc_idx(int_list):
    """
    Given a list of ints, returns list of products except current index
    :param int_list: list
    :return: list
    """
    products_list = []
    copied_list = int_list.copy()

    for i in int_list:
        copied_list.remove(i)
        products_list.append(mult_index(copied_list))
        copied_list = int_list.copy()

    return products_list

print(get_products_exc_idx(int_list))
