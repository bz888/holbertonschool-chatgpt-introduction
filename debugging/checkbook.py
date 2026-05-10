#!/usr/bin/python3
"""
A simple command-line checkbook program.

The program allows a user to:
- deposit money
- withdraw money
- check their balance
- exit the program

It includes input validation so invalid numeric input does not crash
the program.
"""


class Checkbook:
    """
    Represents a simple checkbook with a balance.
    """

    def __init__(self):
        """
        Initialize the checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Args:
            amount (float): The amount to deposit.
        """
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook if funds are available.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current checkbook balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_amount(prompt):
    """
    Safely get a numeric amount from the user.

    Args:
        prompt (str): The input message shown to the user.

    Returns:
        float or None: The entered amount, or None if input is invalid.
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return None


def main():
    """
    Run the main checkbook command loop.
    """
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        ).lower()

        if action == "exit":
            break

        if action == "deposit":
            amount = get_amount("Enter the amount to deposit: $")

            if amount is not None:
                cb.deposit(amount)

        elif action == "withdraw":
            amount = get_amount("Enter the amount to withdraw: $")

            if amount is not None:
                cb.withdraw(amount)

        elif action == "balance":
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()