# Desafio Tunts

A simple grading program developed to interact with [this gradebook](https://docs.google.com/spreadsheets/d/1QI7u61hhoaLEjTpddQ_aN9nFnhP9q4XaJK7Vd1KSz4s/edit#gid=0), made with Google Sheets. This project is part of TuntsCorp's selection process, and was created as proposed on Gupy platform.


Features:
- Calculate the final score, based on three exam scores;
- Round decimal places of the final score, if applicable;
- Determine if the student passed, failed or has to do the final exam, based on the final score;
- Calculate the score the student needs on the final exam, if applicable;
- Determine if the student failed the class due to excessive absences.

**Disclaimer:** For privacy reasons, the account exposed in the credentials.json file was created solely for this project and contains no information about me other than my name.

Basic usage
-----------

In order to run this script on Microsoft Windows, it is required to have Python 3+ installed ([click here](https://www.python.org/downloads/) to download it) and follow the instructions:

1. Download this repository to Desktop;
2. Unzip the file;
3. Open the Command Prompt;
4. Enter the following commands:
    ```
    > pip install gspread oauth2client
    > cd Desktop
    > cd desafio-Tunts
    > python main.py
    ```
