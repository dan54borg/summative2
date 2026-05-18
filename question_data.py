import csv


def load_questions(filepath="questions.csv") -> list:
    """
    Loads yes/no questions from a CSV file.
    """
    questions = []
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append(row["Questions"])
    return questions


def save_response(name: str, stopped_at: int | None, filepath="responses.csv"):
    """
    Writes name, timestamp, and result to the responses CSV.
    stopped_at is the question index where they said No,
    or None if they answered Yes to all questions.
    """
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if stopped_at is None:
        result = "Completed all questions"
    else:
        result = f"Said No at question {stopped_at + 1}"

    with open(filepath, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, timestamp, result])