import json
import os

NOTES = "notes.json"
def notes_json_available():
    if os.path.exists(NOTES):
        with open(NOTES,"r") as f:
            return json.load(f)
    else:
        return []
def add_new_note():  
    data = notes_json_available() 
    new = input("Enter a new note: ")
    data.append(new)
    with open(NOTES, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Saved Current notes: {data}")
def saving_data():
    data = notes_json_available()
    with open(NOTES,"w")as f:
        json.dump(data, f, indent=4)
if __name__=="__main__":
    add_new_note()
    


