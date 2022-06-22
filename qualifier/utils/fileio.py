# -*- coding: utf-8 -*-
# Helper functions to load and save CSV data.

# import required libraries
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def export_qualifying_loans(qualifying_loans, csvpath_answer):

    """Exports a CSV file containing all qualified loans.

    Args:
        qualifying_loans (Dictionary): The qualified loans based on the user's input and filters
        csvpath_answer (String): The csv file path string entered by the user.

    Returns:
        Nothing

    """
    
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
