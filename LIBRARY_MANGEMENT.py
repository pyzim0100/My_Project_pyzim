# library_mangement V-1

import os
import time
from rich.console import Console
from pyfiglet import figlet_format
from random import randint

file_path = "books.txt"
agreement_options = ["y", "yes", "n", "no"]

################################################

# the Aesthetics

console = Console()

def back_to_main():
    while True:
        ask = input_slow_writing("\nback to main menu?(y/n)\n--->")
        if ask in agreement_options:
            break
        else:
            slow_writing("invalid key !!", style="underline bold", speed=0)
            continue
    if ask == "y" or ask =="yes":
        os.system("cls")
        main()
    else:
        time.sleep(2)
        back_to_main()

def make_library():
    slow_writing("!! The Library isn't exist !!\n", text_style="underline bold white", speed=0)
    while True:
        make_library = input_slow_writing("do you want to make one?\n---> ")
        if make_library in agreement_options:
            break
        else:
            slow_writing("invalid key !!", text_style="underline white bold", speed=0)
            continue

    if make_library == "y" or make_library == "yes":
        with open(file_path, "a"):
            console.print("The library was added successfully !", style="bold italic white")
            back_to_main()
    else:
        back_to_main()

def slow_writing(text: str,text_style = "white", speed = 0.025):
    for char in text:
        console.print(char, end="", style= text_style)
        time.sleep(speed)
    print()

def input_slow_writing(text: str,text_style = "white", speed = 0.025):
    for char in text:
        console.print(char, end="", style=text_style)
        time.sleep(speed)
    return input()

def loading(text: str):
    x = randint(2, 6)
    for x in range(1, x):
        for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
            time.sleep(0.1)
            if x == 21:
                break
            else:
                print(text +i, end = '\r')

################################################

# decorators
def check_file(func):
    def wrapper():
        if os.path.exists(file_path):
            func()
        else:
            make_library()
    return wrapper

def clear_before_func(func):
    def wrapper():
        os.system("cls")
        func()
    return wrapper
################################################

# view function
@clear_before_func
@check_file
def view_library():
    print(figlet_format("View Library\n"))
    with open(file_path, "r") as file:
        lines = file.readlines()
        if lines == []:
            slow_writing("The Library is Empty >_<", style="bold white")
            time.sleep(1)
            while True:
                add = input_slow_writing("\nDo you want to add some books")
                if add in agreement_options:
                    break
                else:
                    slow_writing("invalid key !!", text_style="underline bold white", speed=0)
                    continue
            if add == "y" or add == "yes":
                add_book()
            else:
                back_to_main()

        else:
            for book in lines:
                console.print(book, end="")
            back_to_main()

# check function
@clear_before_func
@check_file
def search_book():
    print(figlet_format("Search Book\n"))
    with open(file_path) as file:
        books = file.readlines()
        if books == []:
            slow_writing("The Library is Empty >_<\n", text_style="bold white", speed= 0)
            time.sleep(1)
    # optionnel choices
            while True:
                add = input_slow_writing("\nDo you want to add some books\n--->")
                if add in agreement_options:
                    break
                else:
                    slow_writing("invalid key !!", text_style="underline bold white", speed=0)
                    continue
            if add in ["y", "yes"]:
                add_book()
            else:
                back_to_main()
       
        else:
            search_id = input_slow_writing("what is the id of the book?\n---> ")
            loading("\nSearch ")
            for line in books:
                if search_id in line:
                    line_index = books.index(line)
                    print("\n",
                        line, books[line_index + 1],
                        books[line_index + 2],
                        books[line_index + 3],
                        books[line_index + 4])
                    break
                else:
                    slow_writing("this book isn't exist !", style="bold white", speed=0)
                    break
    # optionnel options
        while True:
            choice = input_slow_writing("""    1- search on another book?
    2- Back to main?\n---> """, text_style="bold white",speed=0)
            if choice in ["1", "2"]:
                 break
            else:
                slow_writing("invalid key !!", text_style="bold white underline", speed=0)
                continue
        if choice == "1":
            search_book()
        else:
            back_to_main()

# add functions
def add_conditions():

    while True:
        book_id = input_slow_writing("id: ", text_style="bold white")
        if book_id.isdigit():
            break
        else:
            slow_writing("invalid value! numbers only!\n", text_style="bold underline white", speed=0)
            continue
    with open(file_path) as file:
        for line in file.readlines():
            if book_id in line:
                slow_writing("this id is already existing !\n", text_style="bold white", speed=0)
                back_to_main()
            else:
                break

    while True:
        name = input_slow_writing("name: ", text_style="bold white")
        if name.isalpha():
            break
        else:
            slow_writing("invalid value! letters only!\n", text_style="bold underline white", speed=0)
            continue
    
    while True:
        author = input_slow_writing("author: ", text_style="bold white")
        if author.isalpha():
            break
        else:
            slow_writing("invalid value! letters only!\n", text_style="bold underline white", speed=0)
            continue

    while True:
        pages = input_slow_writing("pages: ", text_style="bold white")
        if pages.isdigit():
            break
        else:
            slow_writing("invalid value! numbers only!\n", text_style="bold underline white", speed=0)
            continue

    return book_id, name, author, pages

@clear_before_func
@check_file
def add_book():
    print(figlet_format("Add Book\n"))
    # take informations
    conditions = add_conditions()
    # confiramtion
    while True:
        confirmation = input_slow_writing("are you shure to add this book?\n---> ", text_style="bold white", speed=0)
        if confirmation in ["y", "yes", "confirm", "n", "no"]:
            break
        else:
            slow_writing("invalid key !!", text_style="bold underline white", speed=0)
            continue

    if confirmation in ["y", "yes", "confirm"]:
        with open("books.txt", "a") as file:
                file.write(f"BOOk {conditions[0]}\nname: {conditions[1]}\nauthor: {conditions[2]}\npages: {conditions[3]}\n---------------------\n")
        slow_writing("the book was added succesfully !!", text_style="bold white italic")
        while True:
            choice = input_slow_writing("""     1- Add another book?
    2- Back to main?\n--> """, text_style="bold white")
            if choice in ["1", "2"]:
                break
            else:
                slow_writing("invalid key !!", text_style="bold underline white", speed=0)
                continue
        if choice == "1":
            add_book()
        else:
            main()
    
    # optionnel options
    else:
        while True:
            choice = input_slow_writing("""   1- Add a book?
    2- Back to main?\n---> """, text_style="bold white")
            if choice in ["1", "2"]:
                break
            else:
                slow_writing("invalid key !!", text_style="bold white underline", speed=0)
                continue
        if choice == "1":
                add_book()
        else:
            main()

# delete function
@clear_before_func
@check_file
def delete_book():
    print(figlet_format("Delete Book\n"))
    search_id = input_slow_writing("what is the id of the book?\n---> ", text_style="white")
    with open("books.txt") as file:
        lines = file.readlines()
        for line in lines:
            if search_id in line:
                line_index = lines.index(line)
                lines.remove(lines[line_index])
                lines.remove(lines[line_index])
                lines.remove(lines[line_index])
                lines.remove(lines[line_index])
                lines.remove(lines[line_index])
                break
            else:
                slow_writing("this book isn't exist !", text_style="bold white", speed=0)
                break
    with open("books.txt", "w") as file:
        for line in lines:
            file.write(line)
    # optionnel options
    while True:
        choice = input_slow_writing("""    1- delete another book?
    2- Back to main?\n---> """, text_style="bold white")
        if choice in ["1", "2"]:
                break
        else:
            slow_writing("invalid key !!", text_style="bold underline white", speed=0)
            continue

    if choice == "1":
        delete_book()
    else:
        main()

######### main ##########
@clear_before_func
def main():
    print(figlet_format("The Library\n"))
    console.print("""
    1- view my library
    2- search books
    3- add books
    4- delete books
    5- quit""", style="bold")
    while True:
        user_option = input_slow_writing("\nwhat is your option?(by numbers)\n---> ")
        if user_option in ["1", "2", "3", "4", "5"]:
            break
        else:
            console.print("invalid option !", style="underline bold")
            continue

    if user_option == "5":
            quit()
    if user_option == "1":
        view_library()
    elif user_option == "2":
        search_book()
    elif user_option == "3":
        add_book()
    elif user_option == "4":
        delete_book()

#########################
       
if __name__ == "__main__":
    main()