from os import listdir, path, makedirs
from pathlib import Path

def init():
    if not path.exists("data"):
        makedirs("data")

def get_subjects():
    entries = Path("data")
    subjects = []
    for entry in entries.iterdir():
        subjects.append(entry.name.split('.')[0].capitalize())
    
    return subjects

def create_subject(subject):
    subjects = get_subjects()
    formatted_subject = subject.replace(" ", "").replace(".", "").lower()
    if formatted_subject in subjects:
        raise FileExistsError("Subject already exists")
    open(f"data/{formatted_subject}.txt", 'w')

   
