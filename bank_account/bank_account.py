"""
Description: A class meant to manage Bank Accounts.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the BankAccount class to manage bank account records and 
apply interest.
"""
from .interest_rate import InterestRate

class BankAccount:
    
    def __init__(self, account_number: int, balance:float, years_active: int):

        try:
            account_number = int(account_number)
        except ValueError:
            raise ValueError("Account Number must be numeric.")
        
        if account_number <= 0:
            raise ValueError("Account Number must be positive.")

        try:
            balance = float(balance)
        except ValueError:
            raise ValueError("Balance must be numeric.")
        
        try:
            years_active = int(years_active)
        except ValueError:
            raise ValueError("Years Active must be numeric.")
        
        if years_active < 0:
            raise ValueError("Years Active must be positive.")

        self._account_number = account_number
        self._balance = balance
        self._years_active = years_active
   
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Account Number must be numeric.")
        
        if value <= 0:
            raise ValueError("Account Number must be positive.")

        self._account_number = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Balance must be numeric.")
        self._balance = value


    @property
    def years_active(self):
        return self._years_active

    @years_active.setter
    def years_active(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Years Active must be numeric.")
        
        if value < 0:
            raise ValueError("Years Active must be positive.")

        self._years_active = value


    def apply_interest(self) -> None:
        interest_rate = 0
        if self._balance < 0:
            interest_rate = InterestRate.NEGATIVE.value
        elif self._balance < 10000:
            interest_rate = InterestRate.LOW.value
        elif self._balance < 20000:
            interest_rate = InterestRate.MEDIUM.value
        else:
            interest_rate = InterestRate.HIGH.value
        
        if self._years_active > 10 and self._balance  > 0:
            interest_rate += 0.0250


        self._balance = self._balance + (self._balance * interest_rate)

    
    def __str__(self):

        return (f"Account Number: {self._account_number}\n"
                f"Balance: ${self._balance}\n"
                f"Years Active: {self._years_active}")
    
    def __repr__(self):
        return [self._account_number, self._balance, self._years_active]
