"""
Description: A client program written to verify accuracy of and 
BankAccount class.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

### REQUIREMENT
### ADD IMPORT STATEMENT FOR THE BANKACCOUNT CLASS
from bank_account.bank_account import BankAccount

### REQUIREMENT
### ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK WHICH 
### WILL CATCH A 'FILENOTFOUNDERROR' EXCEPTION
try:
    with open ("data\\pixell_river_bank_accounts.txt","r") as input:
        print("**************************************************")

        for data in input:
            items = data.split(",")
            
            try:
                bank_account = items[0]
                balance = items[1]
                years_active = items[2]
                       
                ### REQUIREMENT:
                ### INSTANTIATE A BANKACCOUNT OBJECT USING THE VALUES
                ### FOR ACCOUNTNUMBER, BALANCE, AND YEARSACTIVE ABOVE.
                bank_account = BankAccount(bank_account, balance, years_active)
                
                ### REQUIREMENT:
                ### APPLY INTEREST TO THE BANK ACCOUNT
                bank_account.apply_interest()

                ### REQUIREMENT:
                ### PRINT THE BANK ACCOUNT OBJECT
                print(bank_account)
            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: [{data.strip()}] caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: [{data.strip()}] caused Exception: {e}")        
            finally:
                print("**************************************************")
except FileNotFoundError as ex:
    print(ex)
