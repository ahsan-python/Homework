import json
import os

NOTES = "notes.json"
def notes_json_available():
  if os.path.exist(NOTES)
    with open(NOTES, "r") as f:
      return json.load(f)
  else:
      return[]
    
