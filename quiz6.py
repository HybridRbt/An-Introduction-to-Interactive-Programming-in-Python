__author__ = 'jeredyang'

# Q6
# A common feature in many object-oriented languages is method overloading.
# In this quiz question, you will learn by example what overloading is and whether or not Python supports it.
# Turn the following English description into code.
#
# ~ Start a class definition.We'll call the class Overload.
# ~ Define an __init__ method.Along with the standard self, it has one parameter.

# ~ Define a second __init__ method. Along with self, it has two parameters.This method also does nothing useful.
# Outside of the class, we want to create two Overload objects.If Python supports overloading, you will be able to
# create an Overload object with one argument, and create another Overload object with two arguments.
# Does Python support overloading?


# class Overload:
# def __init__(self, a_parameter):
# pass
#
# def __init__(self, a_parameter, b_parameter):
#         pass
#
# a = Overload(0)
#
# b = Overload(1, 2)
#
# print a, b

# Q7
class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fee = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance -= amount

        if self.balance < 0:
            self.fee += 5
            self.balance -= 5

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee


#
# my_account = BankAccount(10)
# my_account.withdraw(15)
# my_account.deposit(20)
# print my_account.get_balance(), my_account.get_fees()

# my_account = BankAccount(10)
# my_account.withdraw(5)
# my_account.deposit(10)
# my_account.withdraw(5)
# my_account.withdraw(15)
# my_account.deposit(20)
# my_account.withdraw(5)
# my_account.deposit(10)
# my_account.deposit(20)
# my_account.withdraw(15)
# my_account.deposit(30)
# my_account.withdraw(10)
# my_account.withdraw(15)
# my_account.deposit(10)
# my_account.withdraw(50)
# my_account.deposit(30)
# my_account.withdraw(15)
# my_account.deposit(10)
# my_account.withdraw(5)
# my_account.deposit(20)
# my_account.withdraw(15)
# my_account.deposit(10)
# my_account.deposit(30)
# my_account.withdraw(25)
# my_account.withdraw(5)
# my_account.deposit(10)
# my_account.withdraw(15)
# my_account.deposit(10)
# my_account.withdraw(10)
# my_account.withdraw(15)
# my_account.deposit(10)
# my_account.deposit(30)
# my_account.withdraw(25)
# my_account.withdraw(10)
# my_account.deposit(20)
# my_account.deposit(10)
# my_account.withdraw(5)
# my_account.withdraw(15)
# my_account.deposit(10)
# my_account.withdraw(5)
# my_account.withdraw(15)
# my_account.deposit(10)
# my_account.withdraw(5)
# print my_account.get_balance(), my_account.get_fees()

# Q8
# account1 = BankAccount(10)
# account1.withdraw(15)
# account2 = BankAccount(15)
# account2.deposit(10)
# account1.deposit(20)
# account2.withdraw(20)
# print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()
# account1 = BankAccount(20)
# account1.deposit(10)
# account2 = BankAccount(10)
# account2.deposit(10)
# account2.withdraw(50)
# account1.withdraw(15)
# account1.withdraw(10)
# account2.deposit(30)
# account2.withdraw(15)
# account1.deposit(5)
# account1.withdraw(10)
# account2.withdraw(10)
# account2.deposit(25)
# account2.withdraw(15)
# account1.deposit(10)
# account1.withdraw(50)
# account2.deposit(25)
# account2.deposit(25)
# account1.deposit(30)
# account2.deposit(10)
# account1.withdraw(15)
# account2.withdraw(10)
# account1.withdraw(10)
# account2.deposit(15)
# account2.deposit(10)
# account2.withdraw(15)
# account1.deposit(15)
# account1.withdraw(20)
# account2.withdraw(10)
# account2.deposit(5)
# account2.withdraw(10)
# account1.deposit(10)
# account1.deposit(20)
# account2.withdraw(10)
# account2.deposit(5)
# account1.withdraw(15)
# account1.withdraw(20)
# account1.deposit(5)
# account2.deposit(10)
# account2.deposit(15)
# account2.deposit(20)
# account1.withdraw(15)
# account2.deposit(10)
# account1.deposit(25)
# account1.deposit(15)
# account1.deposit(10)
# account1.withdraw(10)
# account1.deposit(10)
# account2.deposit(20)
# account2.withdraw(15)
# account1.withdraw(20)
# account1.deposit(5)
# account1.deposit(10)
# account2.withdraw(20)
# print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

# quiz 6b
# Q5
# def list_extend_many(lists):
#     result = []
#     i = 0
#     while i < len(lists):
#         result.extend(lists[i])
#         i += 1
#     return result
# def list_extend_many(lists):
#     result = []
#     i = 0
#     while i < len(lists):
#         result += lists[i]
#         i += 1
#     return result
#
# def list_extend_many(lists):
#     result = []
#     i = 0
#     while i < len(lists):
#         result += lists[i]
#         i += 1
#     return result
def list_extend_many(lists):
    result = []
    i = 0
    while i < len(lists):
        result.extend(lists[i])
        i += 1
    return result
print list_extend_many([[1, 2], [3], [4, 5, 6], [7]])

# Q7
# n = 1000
# numbers = range(2, n)
#
# result = []
#
#
# def remove_number(a_list):
#     divider = a_list[0]
#     remove = []
#     i = 0
#     while i < len(a_list):
#         if a_list[i] % divider == 0:
#             remove.append(a_list[i])
#         i += 1
#
#     for each_number in remove:
#         a_list.remove(each_number)
#
#
# while len(numbers) > 0:
#     result.append(numbers[0])
#     remove_number(numbers)
#
# print len(result)

#Q8
# slow_wumpuses = 1000
# Fast_Wumpuses = 1
#
#
# def num_of_slow(year):
#     global slow_wumpuses
#
#     if year == 1:
#         num = slow_wumpuses
#     else:
#         num = 2 * num_of_slow(year - 1) * 0.6
#
#     return num
#
#
# def num_of_fast(year):
#     global Fast_Wumpuses
#
#     if year == 1:
#         num = Fast_Wumpuses
#     else:
#         num = 2 * num_of_fast(year - 1) * 0.7
#
#     return num
#
#
# def out_number():
#     y = 1
#     while num_of_slow(y) > num_of_fast(y):
#         y += 1
#         if y > 43:
#             print y, num_of_slow(y), num_of_fast(y)
#
#     return y
#
# print out_number()