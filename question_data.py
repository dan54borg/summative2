import csv # for reading the CSV file

def load_questions(filepath="questions.csv"):

    questions = []

    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: