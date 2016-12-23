_author_ = "prabhjot kaur"


# Initialize the constants


def main():
    """

"""
    print("Reading List 1.0 - by Prabhjot kaur ")
    list_book = []
    displaymenu()
    load_books(list_book)
    choice = input("enter your choice").upper()
    print(choice)
    while choice != 'Q':
        if choice == 'R':
            print("required")
            list_required(list_book)
        elif choice == 'C':
            list_completebooks(list_book)
        elif choice == 'A':
            """
        """
        elif choice == 'M':
            """
        """
        else:
            print("invalid input")
        choice = input("enter your choice").upper()


# end of main()
def displaymenu():
    print("Menu:")


print("R - List required books")
print("C - List completed books")
print("A - Add new book")
print("M - Mark a book as completed")
print("Q - Quit")


def load_books(list_book):
    temp_file = open("books.csv", "r")
    for line in temp_file:
        list_book.append(line.strip().split(','))
        print(line)
        # temp_file.close()



        # end of load_books()


def complete_a_book():
    """

"""


print("complete a book")


# end of complete_a_book()

# Start the program
def list_completebooks(list_book):
    for list in list_book:
        if list_book[list][3] == 'c':
            print(list_book[list][0], list_book[list][1], list_book[list][2])


def list_required(list_book):
    totalpages = 0
    count = 0
    for list in list_book:
        if list_book[count][3] == 'r':
            print(list_book[count][0], list_book[count][1], list_book[count][2])
            totalpages += int(list_book[count][2])
        count += 1

def add_book():
    """
"""


def mark_completebook():
    """
"""


main()
