import json
import os

NOTES = "notes.json"
def notes_json_available():
  if os.path.exist(NOTES)
    with open(NOTES, "r") as f:
      return json.load(f)
  else:
      return[]
def add_new_note():
  data = notes_json_available()
  new = input("Add new notes:")
  data.append(new)
  with open(NOTES, "w")as f:
    json.dump(data, f, indent=4)
    print(f"Saved Current notes : {data}")
def saving_data():
   data = notes_json_available()
  with open(NOTES, "w")as f:
    json.dump(data, f, indent=4)
    
    
    
  
    
