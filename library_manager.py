import json
import os

# Load library from file
if os.path.exists('library.txt'):
    library = json.load(open('library.txt'))
else:
    library = []

print("Welcome to your Personal Library Manager!\n")

while True:
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    choice = input("Enter your choice: ")
    print()

    if choice == '1':
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read_input = input("Have you read this book? (yes/no): ")
        if read_input.lower() == 'yes':
            read_status = True
        else:
            read_status = False
        book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read_status
        }
        library.append(book)
        print("Book added successfully!\n")

    elif choice == '2':
        title = input("Enter the title of the book to remove: ")
        found = False
        for book in library:
            if book['title'] == title:
                library.remove(book)
                found = True
                print("Book removed successfully!\n")
                break
        if not found:
            print("Book not found.\n")

    elif choice == '3':
        print("Search by:")
        print("1. Title")
        print("2. Author")
        search_choice = input("Enter your choice: ")
        term = input("Enter the search term: ")
        print("Matching Books:")
        for book in library:
            if (search_choice == '1' and term.lower() in book['title'].lower()) or \
               (search_choice == '2' and term.lower() in book['author'].lower()):
                status = 'Read' if book['read'] else 'Unread'
                print(book['title'] + " by " + book['author'] + " (" + str(book['year']) + ") - " + book['genre'] + " - " + status)
        print()

    elif choice == '4':
        if library:
            print("Your Library:")
            for book in library:
                status = 'Read' if book['read'] else 'Unread'
                print(book['title'] + " by " + book['author'] + " (" + str(book['year']) + ") - " + book['genre'] + " - " + status)
        else:
            print("Library is empty.")
        print()

    elif choice == '5':
        total = len(library)
        if total > 0:
            read_count = 0
            for book in library:
                if book['read']:
                    read_count += 1
            percent = (read_count / total) * 100
            print("Total books:", total)
            print("Percentage read: " + str(round(percent, 1)) + "%\n")
        else:
            print("No books to show statistics.\n")

    elif choice == '6':
        json.dump(library, open('library.txt','w'), indent=4)
        print("Library saved to file. Goodbye!\n")
        break

    else:
        print("Invalid choice. Please try again.\n")
