#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if(my_list_1 is None and my_list_2 is None):
        return 0
    else:
        new_arr = []
        for i in range(list_length):
            result = 0
            try:
                result = my_list_1[i] / my_list_2[i]
            except (ValueError, TypeError):
                result = 0
                print("wrong type")
            except ZeroDivisionError:
                result = 0
                print("division by zero")
            except IndexError:
                result = 0
                print("out of range")
            finally:
                new_arr.append(result)
        return new_arr
