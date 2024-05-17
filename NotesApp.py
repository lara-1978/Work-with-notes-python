import json
import os
from datetime import datetime

class NotesApp:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json","r") as file:
                self.notes = json.load(file)

    def save_notes(self):
        with open("notes.json", "w") as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, title, message):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "message": message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(note)
        self.save_notes()
        print("Note added!")

    def list_notes(self, filter_date=None):
        if filter_date:
            filtered_notes = [note for note in self.notes if note["timestamp"].split()[0] == filter_date]
            for note in filtered_notes:
                print(f"ID: {note['id']}, Title: {note['title']}, Message: {note['message']}, Timestamp: {note['timestamp']}")
        else:
            for note in self.notes:
                print(f"ID: {note['id']}, Title: {note['title']}, Message: {note['message']}, Timestamp: {note['timestamp']}")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note["id"] != note_id]
        self.save_notes()
        print("Note deleted!")

    def edit_note(self, note_id, new_title, new_message):
        for note in self.notes:
            if  note["id"] == note_id:
                note["title"] = new_title
                note["message"] = new_message
                note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
        self.save_notes()
        print("Note edited!")

if __name__ == "__main__":
    app = NotesApp()
    while True:
        command = input("Enter command (add/list/delete/edit/exit): ").lower()
        if command == "add":
            title = input("Enter note title: ")
            message = input("Enter note message: ")
            app.add_note(title, message)
        elif command == "list":
            filter_date = input("Enter date to filter notes (YYYY-MM-DD) ")
            app.list_notes(filter_date)
        elif command == "delete":
            note_id = int(input("Enter note ID to delete: "))
            app.delete_note(note_id)
        elif command == "edit":
            note_id = int(input("Enter note ID to edit: "))
            new_title = input("Enter new title: ")
            new_message = input("Enter new message: ")
            app.edit_note(note_id, new_title, new_message)
        elif command == "exit":
            break
        else:
            print("Error !!! Please try again.")




        
    
    