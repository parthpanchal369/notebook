import json
from datetime import datetime
import os

class Note:
    def __init__(self, title, content, category):
        self.title = title
        self.content = content
        self.category = category


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def view_notes(self):
        for note in self.notes:
            print(f'Title: {note.title}\nContent: {note.content}\ncategory: {note.category}\n')

    def update_note(self, title, new_content):
        for note in self.notes:
            if note.title == title:
                note.content = new_content
                print(f"Note '{title}' updated successfully. ")
                return
        print(f"Note '{title} not found.'")

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print(f"Note '{title}' deleted successfully.")

                # Delete the corresponding JSON file
                filename = f'notes_{note.title}.json'
                self.delete_file(filename)

                return
        print(f"Note '{title}' not found.")

    def delete_file(self, filename):
        try:
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error deleting file '{filename}': {e}")

    def save_notes_to_file(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f'notes_{timestamp}.json'
        with open(filename, 'w') as file:
            notes_data = [{'title': note.title, 'content': note.content, 'category': note.category}
                          for note in self.notes]
            json.dump(notes_data, file, indent=2)
        print(f'Notes saved to file: {filename}')

    def load_notes_from_file(self, filename='notes.json'):
        try:
            with open(filename, 'r') as file:
                notes_data = json.load(file)
                self.notes = [Note(note['title'], note['content'], note['category']) for note in notes_data]
        except FileNotFoundError:
            # Handle the case where the file doesn't exist yet
            pass


def main():
    my_notebook = Notebook()
    my_notebook.load_notes_from_file()

    while True:
        print("\nOptions:")
        print('1. Add Note')
        print('2. View Notes')
        print('3. Update Note')
        print('4. Delete Note')
        print('5. Quit')

        choice = input("Enter your choice from above: ")

        if choice == '1':
            title = input("Enter your title: ")
            content = input("Enter your note content: ")
            category = input('Enter your note category: ')
            new_note = Note(title, content, category)
            my_notebook.add_note(new_note)
            print("Note added successfully.")

        elif choice == '2':
            my_notebook.view_notes()

        elif choice == '3':
            title = input("Enter the title of the note to update: ")
            new_content = input("Enter the new content: ")
            my_notebook.update_note(title, new_content)

        elif choice == '4':
            title = input("Enter the title of the note to delete: ")
            my_notebook.delete_note(title)
            my_notebook.save_notes_to_file()



        elif choice == '5':
            my_notebook.save_notes_to_file()
            print("Exiting from the notes, Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue


if __name__ == "__main__":
    main()

