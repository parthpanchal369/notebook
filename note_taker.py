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
                return
        print(f"Note '{title}' not found.")


def main():
    my_notebook = Notebook()

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

        elif choice == '5':
            print("Exiting from the notes, Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()