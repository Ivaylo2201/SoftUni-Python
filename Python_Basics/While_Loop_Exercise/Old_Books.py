bookList = []
wantedBook = input()
while True:
    bookName = input()
    checkedBooks = len(bookList)

    if bookName != wantedBook:
        bookList.append(bookName)

    if bookName == wantedBook:
        print(f"You checked {checkedBooks} books and found it.")
        quit()

    if bookName == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checkedBooks} books.")
        quit()
