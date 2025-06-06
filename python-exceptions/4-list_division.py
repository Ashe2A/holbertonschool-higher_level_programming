#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides lists together

    Args:
        my_list_1 (list): List of int or float (divided)
        my_list_2 (list): List of int or float (divider)
        list_length (int): length of the new list

    Returns:
        list: list of division results
    """
    div_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            continue
        except IndexError:
            print("out of range")
            continue
        except (TypeError, ValueError):
            print("wrong type")
            continue
        finally:
            div_list.append(res)
    return div_list
