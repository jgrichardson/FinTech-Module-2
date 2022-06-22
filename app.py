# This is the Module 2 Challenge submission for Greg Richardson

# import libraries
import sys
from requests import head
import fire
import questionary
from pathlib import Path
import csv

# import fileio mdule
from qualifier.utils.fileio import load_csv

# import calculators module
from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

# import filters module
from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

# Load the bank data from the daily_rate_sheet.csv file inside the repo
def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    # Prompt the user to enter the path to the bank data CSV
    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    # Make sure the entered path finds a CSV file, if not, let them know.
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")
    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    # Output whether any qualifying loans were found
    if len(bank_data_filtered) < 1:
        # If none were found, let the user know.
        print("Sorry, no qualifying loans were found based on your inputs.")
    else:
        # At least one was found, so let the user know how many
        print(f"Great news!  We found {len(bank_data_filtered)} qualifying loans based on your inputs!")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans):

    """Takes in the qualifying_loans (list of lists): The qualifying bank loans.
    
    Prompt dialog to ask if user wants to export results to CSV. 

    Prompt dialog to ask user for path/file to save CSV being saved.

    Saves the qualifying loans to a CSV file if the user answered yes and provides a path/filename.

    """
    # NOTE - a TODO here would be to consider moving this function to the fileio module, since it is saving a CSV.
    # The challenge instructions did not indicate to do this, so I left it here, and imported the csv lib above to supoprt it.

    # Ask user if they want to save results to a CSV
    answer = questionary.confirm('Do you want to save a CSV fle with all qualifying loans?').ask()
    
    # If they answer yes
    if answer:

        # Prompt the user for a path and filename to save their CSV
        csvpath_answer = questionary.text('Enter a path and filename for your CSV file').ask()
        
        # Create a csvpath object from the user-entered path and filename
        # NOTE a TODO for this needs to be to check that the user-entered path/fileman is valid, however this was not instructed in the chalenge
        csvpath = Path(csvpath_answer)

        # Define a list variable to hold the header of the CSV
        header = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']

        # Open and write the CSV
        with open(csvpath, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Write our header row first
            csvwriter.writerow(header)

            # Write the data rows from qualifying_loans
            for row in qualifying_loans:
                csvwriter.writerow(row)

        # Give the user feedback that their loans can be found in the CSV file
        print(f"Your qualified loans have been saved in the file {csvpath_answer}") 


def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    # First, check to make sure at least one qualifying_loan was found before offering to export a CSV
    if len(qualifying_loans) > 0:
        save_qualifying_loans(qualifying_loans)

if __name__ == "__main__":
    fire.Fire(run)
