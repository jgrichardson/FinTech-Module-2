# *FinTech Repository -- Module 2 Challenge Submission*

This project is the Module 2 Challenge submission for the FinTech bootcamp program. Specifically, it adds new features and enhancements to the loan qualifier application. 

The application takes the following inputs from the user and matches them against a pre-defined daily_rate_sheet of lenders and products/characteristics.

* The user's credit score
* The user's monthly debt
* The user's monthly income
* The desired loan amount
* The home value

The application then prompts the user for whether they want any matched lenders/loans to be saved as a CSV file, and if so, prompts the user for the path/filename to be output.

This application also adheres to best practices in the following areas:

* Version Control
* Software Requirements
* System Design
* Code Organization
* Usability
* Documentation

---

## Technologies

The technologies used for this project include:

* Python interpreter v3.9.12
* Python sys library: Support for system-specific parameters and functions
* Python fire library: Support for automatically generating command line interfaces (CLIs)
* Python questionary library: Support for building pretty command line interfaces
* Python pathlib library: Support for Object-oriented filesystem paths
* Python csv library: Support for CSV file reading and writing

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```

---

## Usage

To use this loan qualifier application simply clone the repository and run the **app.py** script using the following command.

```python
python app.py
```

Upon launching the application, you will be asked to input your credit score (range: 300-850), monthly debt, monthly income, desired loan amount, and home value.

![Run Program](images/run_program.png)

You will then be asked whether you want the qualified loans to be saved as a CSV file. If so, enter "Y" -- or press enter -- the default is **Yes**.

![Export Results Prompt](images/first_prompt.png)

If you answered Yes to output your results, you will then be asked to enter a path and/or filename for your results file. e.g. my_output.csv

![Export File Path/Filename Prompt](images/second_prompt.png)

---

---

## Contributors

[Greg Richardson](https://github.com/jgrichardson)

---

## License

The source code for the application is licensed under the MIT license, which you can find in the LICENSE file in this repo.
