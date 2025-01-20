# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
#from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('Enter your starting savings balance: '))
    savings_interest = float(input('Enter the interest rate: '))
    savings_maturity = int(input('Enter months: '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    #interest_earned = savings_balance * (savings_interest/100 * savings_maturity/12)
    #updated_savings_balance = interest_earned + savings_balance


    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Your interest is ", interest_earned, "Your updated savings balance is", updated_savings_balance)


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('Enter your starting cd balance: '))
    cd_interest = float(input('Enter the interest rate: '))
    cd_maturity = int(input('Enter months: '))

    # Call the create_cd_account function and pass the variables from the user.
    #updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    interest_earned_2 = cd_balance * (cd_interest/100 * cd_maturity/12)
    updated_cd_balance = interest_earned_2 + cd_balance


    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Your interest is ", interest_earned_2, "Your updated cd balance is", updated_cd_balance)

if __name__ == "__main__":
    # Call the main function.
    main()