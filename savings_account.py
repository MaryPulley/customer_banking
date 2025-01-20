"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(savings_balance, savings_interest, savings_maturity):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        savings_balance (float): The initial savings account balance.
        savings_interest (float): The APR interest rate for the savings account.
        savings_maturity (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    savings_account = Account(savings_balance, savings_interest)
    

    # Calculate interest earned
    # ADD YOUR CODE HERE
    def cal_interest(savings_maturity, savings_interest):
        interest_earned = savings_balance * (savings_interest/100 * savings_maturity/12)
        
            #interest_made = interest_rate * months
        #    int_made = interest_made
        return interest_earned 

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    def update_interest(savings_balance, interest_earned):
        updated_savings_balance = interest_earned + savings_balance
        return updated_savings_balance


    interest_earned = cal_interest(savings_maturity, savings_interest)
    updated_savings_balance = update_interest(savings_balance, interest_earned)

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(updated_savings_balance)


    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(interest_earned)
    

    # Return the updated balance and interest earned.
    return updated_savings_balance, interest_earned # ADD YOUR CODE HERE
