def add_book(shelf, title, read_status, id):
    book = {}
    book['ID'] = id
    book['title'] = title
    book['read_status'] = read_status
    shelf.append(book)

def edit_book(shelf, index, new_title=False, new_read_status=False):
    if new_title:
        shelf[index]["title"] = new_title
    if new_read_status:
        shelf[index]["read_status"] = new_read_status

def search_book(shelf, title=False, read_status=False):
    #ここに文字が全部一致する場合と、部分一致を含めて、下の関数を削除する
    search_result = []
    for book in shelf:
        if title and (title in book["title"]):
            search_result.append(book["title"])
        if read_status == 2 and book["read_status"] == True:
            search_result.append(book["title"])
        if read_status == 1 and book["read_status"] == False:
            search_result.append(book["title"])
    return search_result

def book_existed(shelf, title):
    for index, book in enumerate(shelf):
        if book["title"] == title:
            return index+1
    return False

def delete_book(shelf, index):
    del shelf[index]
    #shelf = [book for book in shelf if book['title'] != title]

def view_shelf_stats(shelf):
    number_of_read = 0
    number_of_unread = 0
    for book in shelf:
        if book['read_status'] == True:
            number_of_read += 1
        else:
            number_of_unread += 1
    
    print("======Shelf stats======")
    print(f"total number of books: {number_of_read+number_of_unread}")
    print(f"number of read books: {number_of_read}")
    print(f"number of unread books: {number_of_unread}")
    print("=======================")
  

def check_input(comment, target_number):
    while True:
        user_input = input(comment)
        if user_input.isdigit() and int(user_input) in target_number:
            return int(user_input)
        else:
            print(f"Please enter the number from {target_number}.")

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
            title = input("please input the title you'd like to add: ")
            if book_existed(shelf, title):
                print("Same title exists in your library")
            else:
                read_status = bool(check_input("please input read status from 0(not done) or 1(done): ", [0, 1]))
                add_book(shelf, title, read_status, id)
                id += 1

        if user_select == 2:
            title = input("Please input the title you'd like to edit: ")
            index = book_existed(shelf, title)
            if index:
                edit_status = check_input("Please input item you'd like to edit from 0(title) or 1(read_status): ", [0, 1])
                if edit_status == 0:
                    while True:
                        new_title = input("Please input new title: ")
                        if book_existed(shelf, new_title):
                            print("Same title exists in your library")
                        else:
                            edit_book(shelf, index-1, new_title=new_title)
                            break
                else:
                    new_read_status = check_input("please input read status from 0(not done) or 1(done): ", [0, 1])
                    edit_book(shelf, index-1, new_read_status=new_read_status)
                    print("Read status updated!!")
            else:
                print("No such title exists in your library")          

        if user_select == 3:
            print("How do you search books?")
            search_method = check_input("Select 1(Search by title) or 2(Search by read status): ", [1, 2])
            if search_method == 1:
                title = input("Please input the title you'd like to search: ")
                seach_result = search_book(shelf, title=title)
            else:
                read_status = check_input("Which status do you search 0(unread) or 1(read)? : ", [0, 1])+1
                seach_result = search_book(shelf, read_status=read_status)
            print(seach_result)

        if user_select == 4:
            title = input("Please input the title you want to delete: ")
            index = book_existed(shelf, title)
            if index:
                delete_book(shelf, index-1)
                print(f"Delete {title} !!")
            else:
                print("No such title exists")

        if user_select == 5:
            view_shelf_stats(shelf)

        if user_select == 6:
            print("Shutdown your library")