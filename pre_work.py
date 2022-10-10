# 1. Write a function to pring "Hello user_name"
def hello_name(user_name):

    print("Hello,", user_name + "!")


# hello_name("chris")


def hello_name(user_name):
    """Prints a message to the username in the function input"""
    print('something here \nhello_' + user_name.upper() + '!')


# hello_name('Kelsey')

# Print all odd numbers between 1 and 100


def first_odds():
    for num in range(101):
        if num % 2 == 1:
            print(num)


# first_odds()


def first_odds():
    for number in range(1, 100):
        if number % 2 == 0:
            print(number)


# first_odds()


def first_odds():
    """prints a list of the odd numbers from 1-100 and returns nothing"""
    odds = list(range(1, 100, 2))
    print('\n' + str(odds))


# first_odds()

# Write a function that returns the max number in a given list
def max_num_in_list(a_list):
    return max(a_list)


max_num_in_list([1, 2, 3, 4, 5, 6])


def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num


def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])


# max_num_in_list([1, 3, 5, 6, 7, 9, 8])


def max_num_in_list(a_list):
    """Returns the maximum number in a given list"""
    maximum = max(a_list)
    print('\n' + str(maximum))


a_list = [1, 2, 3, 4]
# max_num_in_list(a_list)

# Write a function to return if the given year is a leap year.


def is_leap_year(a_year):
    if (a_year % 4 == 0) \
        or ((a_year % 400 == 0)
            and not (a_year % 100 == 0)):
        return True
    else:
        return False


def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            return True
        elif a_year % 400 == 0 and a_year % 100 == 0:
            return True
        else:
            return False
    else:
        return False


def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
        return False
    else:
        leap = False
        return leap


# print(is_leap_year(2024))

# Write a function to check if all numbers in a list are consecutive


def is_consecutive(a_list):
    # a_list.sort()
    num_pop_last = a_list.pop()
    while a_list:
        num_pop_first = a_list.pop()
        if num_pop_last - num_pop_first == 1:
            num_pop_last = num_pop_first
            result = True

        else:
            result = False
            break

    if result == True:
        return True
    else:
        return False


def is_consecutive(a_list):
    """print to see if all numbers in a list are consecutive"""
    compare = list(range(min(a_list), max(a_list)+1))
    print(compare)
    print(a_list)
    return a_list == compare


def is_consecutive(a_list):
    min_value = min(a_list)
    max_value = max(a_list)
    a_list.sort()
    for number in a_list:
        if number == min_value:
            min_value += 1
        else:
            return False
        last_number = number
    if last_number == max_value:
        return True
    else:
        return False


print(is_consecutive([1, 2, 3, 5, 6]))
