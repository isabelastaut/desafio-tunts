import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep

# Setting up the usage of Google Sheets API
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Engenharia de Software - Desafio Isabela Staut").sheet1

data = sheet.get_all_records()
number_students = len(data) - 2

for m in range(number_students):
    row = m + 4

    attendance = int(sheet.cell(row, 3).value)

    # Reading the test scores and calculating the average
    first_score = int(sheet.cell(row, 4).value)
    second_score = int(sheet.cell(row, 5).value)
    third_score = int(sheet.cell(row, 6).value)

    avg_score = round((first_score + second_score + third_score) / 3)

    # Determining if student passed, failed or has to do the final exam
    if (attendance / 60) > 0.25:
        sheet.update_cell(row, 7, "Reprovado por Falta")

    elif avg_score >= 70:
        sheet.update_cell(row, 7, "Aprovado")

        sheet.update_cell(row, 8, 0)

    elif 70 > avg_score >= 50:
        sheet.update_cell(row, 7, "Exame Final")

        final_exam = 100 - avg_score
        sheet.update_cell(row, 8, final_exam)

    elif 50 > avg_score:
        sheet.update_cell(row, 7, "Reprovado por Nota")

        sheet.update_cell(row, 8, 0)

    sleep(3)    # Waiting time to prevent exceeding Google Sheets API's requests limit per 100 seconds
