"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_cd_account(cd_balance, cd_interest, cd_maturity):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_account = Account(cd_balance, cd_interest)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    def cal_cd_interest(cd_maturity, cd_interest):
        cd_interest_earned = cd_balance * (cd_interest/100 * cd_maturity/12)
        return cd_interest_earned

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    def update_cd_interest(cd_balance, cd_interest_earned):
        updated_cd_balance = cd_interest_earned + cd_balance
        return updated_cd_balance


    cd_interest_earned = cal_cd_interest(cd_maturity, cd_interest)
    updated_cd_balance = update_cd_interest(cd_balance, cd_interest_earned)

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_balance(updated_cd_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_interest(cd_interest_earned)

    # Return the updated balance and interest earned.
    return updated_cd_balance, cd_interest_earned # ADD YOUR CODE HERE
