def add_book(shelf: list[dict], title: str, read_status:int, id:int):
    """
    This function add the book to your shelf with read status.

    Args:
        shelf (list[dict]): The shelf has books as list
        title (str): Title of the book you would like to add
        read_status (int): read_status (int): Read status of the book. 0(not done) or 1(done)
        id (int): ID of the book.
    """
    book = {}
    book['ID'] = id
    book['title'] = title
    book['read_status'] = read_status
    shelf.append(book)

def edit_book(shelf: list[dict], title: str, new_title: str | bool = False, new_read_status: int | bool = False):
    """
    This function edits the information of the book.
    You can select the book by the title.
    
    Args:
        shelf (list[dict]): The shelf has books as list
        title (str): Title of the book you would like to edit
        new_title (str | bool, optional): New title to edit. Defaults to False.
        new_read_status (int | bool, optional): New read status to edit. Defaults to False.
    """
    for index, book in enumerate(shelf):
        if book['title'] == title:
            if new_title:
                shelf[index]["title"] = new_title
            if new_read_status:
                shelf[index]["read_status"] = new_read_status

def search_book(shelf: list[dict], title: str | bool=False, read_status: int | bool=False)->list:
    """
    This function searches the book by title or read status

    Args:
        shelf (list[dict]): The shelf has books as list.
        title (str | bool, optional): Title of the book you would like to search. Defaults to False.
        read_status (int | bool, optional): Status of the book you would like to search. Defaults to False.

    Returns:
        list: List of books you search
    """
    search_result = []
    for book in shelf:
        if title and (title == book["title"]):
            search_result.append(book["title"])
        if read_status == 2 and book["read_status"] == True:
            search_result.append(book["title"])
        if read_status == 1 and book["read_status"] == False:
            search_result.append(book["title"])
    return search_result

def book_existed(shelf: list[dict], title: str):
    for index, book in enumerate(shelf):
        if book["title"] == title:
            return index+1
    return False

def delete_book(shelf: list[dict], title: str)->list[dict]:
    """
    This function deletes the book from the shelf.

    Args:
        shelf (list[dict]): The shelf has books as list.
        title (str): Title of the book

    Returns:
        list[dict]: The shelf after deleting the book
    """
    return [book for book in shelf if book['title'] != title]

def view_shelf_stats(shelf:list[dict]):
    """
    This function shows the stats of shelf.

    Args:
        shelf (list[dict]): The shelf has books as list.
    """
    number_of_read = 0
    number_of_unread = 0
    for book in shelf:
        if book['read_status'] == True:
            number_of_read += 1
        else:
            number_of_unread += 1
    
    print("=========Shelf stats=========")
    print(f"total number of books: {number_of_read+number_of_unread}")
    print(f"number of read books: {number_of_read}")
    print(f"number of unread books: {number_of_unread}")
    print("=============================\n")

def check_input(comment, target_number=False):
    while True:
        user_input = input(comment).strip()
        if target_number:
            if user_input.isdigit() and int(user_input) in target_number:
                return int(user_input)
            else:
                print(f"Please enter the number from {target_number}.")
        else:
            if user_input:
                return user_input
            else:
                print(f"Do not input the blanks.\n")

if __name__ == '__main__':
    shelf = []
    id = 1
    user_select = 0

    while user_select != 6:
        print("================================================\nWelcome to your personal books desital library!\n================================================")
        print("1: Add a Book")
        print("2: Edit a Book")
        print("3: Search for Books")
        print("4: Delete a Book")
        print("5: View Library Stats")
        print("6: Exit app")
        user_select = check_input("Please select from 1 to 6: ", [1, 2, 3, 4, 5, 6])

        if user_select == 1:
            title = check_input("please input the title you'd like to add: ")
            if search_book(shelf, title):
                print("Same title exists in your library\n")
            else:
                read_status = bool(check_input("Please input read status from 0(not done) or 1(done): ", [0, 1]))
                add_book(shelf, title, read_status, id)
                id += 1

        if user_select == 2:
            title = input("Please input the title you'd like to edit: ")
            search_result = search_book(shelf, title)
            if search_result:
                edit_status = check_input("What parameter do you want to edit? Select from 0(title) or 1(read_status): ", [0, 1])
                if edit_status == 0:
                    while True:
                        new_title = check_input("Please input new title: ")
                        if search_book(shelf, new_title):
                            print("Same title exists in your library!!\n")
                        else:
                            edit_book(shelf, title, new_title=new_title)
                            print(f"{title} chenged to {new_title}")
                            break
                else:
                    new_read_status = check_input("please input read status from 0(not done) or 1(done): ", [0, 1])
                    edit_book(shelf, title, new_read_status=new_read_status)
                    print("Read status updated!!\n")
            else:
                print("No such title exists in your library!!\n")          

        if user_select == 3:
            print("How do you search books?")
            search_method = check_input("Select 1(Search by title) or 2(Search by read status): ", [1, 2])
            if search_method == 1:
                title = check_input("Please input the title you'd like to search: ")
                seach_result = search_book(shelf, title=title)
            else:
                read_status = check_input("Which status do you search 0(unread) or 1(read)? : ", [0, 1])+1
                seach_result = search_book(shelf, read_status=read_status)
            print(f"Seach results: {seach_result}\n")

        if user_select == 4:
            title = check_input("Please input the title you want to delete: ")
            if search_book(shelf, title=title):
                shelf = delete_book(shelf, title)
                print(f"Delete {title} !!\n")
            else:
                print("No such title exists\n")

        if user_select == 5:
            view_shelf_stats(shelf)

        if user_select == 6:
            print("Shutdown your library")