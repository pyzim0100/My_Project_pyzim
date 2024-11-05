# My_Diary Project V-1

import json
import csv
import os
from time import sleep
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich.prompt import Prompt
from pyfiglet import figlet_format
from rich import box

clear = lambda : os.system("cls" if os.name == "nt" else "clear")
console = Console()
Style_Themes = {
    "Warning":Style(color="red", blink2=True, bold=True),
    "Success": Style(color="green", blink=True, bold=True, italic=True),
    "Regular": Style(color="white", bold=True)
}
##### Designs Func #####

def Print(msg, msg_style= Style_Themes["Regular"]):
    console.print(msg, style= msg_style)

##### Sub Func #####

def Make_Diary():
    Print(Panel("You Don't Have A Diary Yet !!", expand=False, style=Style_Themes['Warning']))

    # Diary Folder
    Diary_name = console.input("[b]What You Want To Call It? ").strip()
    os.mkdir(Diary_name)

    # JSON File
    with open('Diary_Info.json', 'a') as json_file:
        Diary_data = {
    "Name": Diary_name
    }
        json.dump(Diary_data, json_file)
    
    # CSV File
    with open('Pages_Data.csv', 'a', newline='') as csv_file:
        fieldnames = ['Page_Name', 'Page_Title', 'Page_Date', 'Page_First_line']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    Print(Panel("Diary was make it successefully !", expand=False, style=Style_Themes["Success"]))
    Options_After_Func(["Add Your First Page?", "Back To Main?"],
                       lambda: Add_Page(),
                       lambda: main())
    return Diary_name

def Diary_Info():
    with open("Diary_Info.json") as Diary:
        data = json.load(Diary)
    Diary_name = data["Name"]
    Diary_pages = len(os.listdir(Diary_name))
    return Diary_name, Diary_pages

def Back_To_Main():
    u_choice = console.input("[b]Back To Main? ").strip().lower()
    if u_choice == "y" or u_choice == "yes":
        main()
    elif u_choice == "n" or u_choice == "no":
        sleep(2)
        Back_To_Main()
    else:
        Print(Panel("Invalid Key !!", style=Style_Themes["Warning"], expand=False))
        Back_To_Main()

def Text_Write(Page_name):
    clear()
    console.rule(Page_name, style="white bold")
    Title = console.input("[b]Title: ").strip('')
    lines = [f"Title: {Title}",
             f"Date: {datetime.now().strftime(f'%d/%m/%Y')}",
             ""]
    num_line = 0
    while len(lines) < 4:
        line = Prompt.ask(str(num_line))
        if line == "END".lower():
            Print("You Must Write At Least One Line !", msg_style=Style_Themes["Warning"])
            continue
        num_line += 1
        lines.append(line)
    else:
        while True:
            line = Prompt.ask(str(num_line))
            if line == "END".lower():
                break
            num_line += 1
            lines.append(line)
    return Title, lines

def Text_Edit(Page_name, previous_text):
    diary_info = Diary_Info() 
    Title = console.input("[b]Title: ").strip('')
    New_Lines = [f"Title: {Title}",
             f"Date: {datetime.now().strftime(f'%d/%m/%Y')}",
             ""]
    num_line = 0
    for Previous_line in previous_text[3:]:
        New_Line = Prompt.ask(f"{str(num_line)}: {Previous_line}\n")
        if New_Line == "END".lower():
            break
        elif New_Line == "":
            New_Lines.append(Previous_line)
        num_line += 1
        New_Lines.append(New_Line)
    else:
        while True:
            line = Prompt.ask(str(num_line))
            if line == "END".lower().strip():
                break
            num_line += 1
            New_Lines.append(line)

    while True:
        confirmation = console.input("[b]are you shure you want to add this page? ").lower().strip()
        if confirmation == "y":
            break
        elif confirmation == "n":
            Options_After_Func(["Edit The Text", "Back To Main?"],
                               lambda: Text_Edit(Page_name, New_Lines),
                               lambda: main())
        else:
            Print(Panel("Invalid Key !!", expand=False, style=Style_Themes["Warning"]))
            continue

    with open(f"{diary_info[0]}/{Page_name}", "w") as Edited_Text:
        for New_line in New_Lines:
            Edited_Text.write(f"{New_line}\n")
    Page_Save(Page_name, Title, New_Lines[3], New_Lines, file_mode='w')
    Print(Panel("The Page Was Added Successfully !", style=Style_Themes["Success"], expand=False))
    Options_After_Func(["Read The Page?", "Back To Main?"],
                       lambda: Read_Page(diary_info[0], Page_name),
                       lambda: main())

def Page_Edit(Page_name):
    clear()
    console.rule(Page_name, style="white bold")
    with open(f"{Diary_Info()[0]}/{Page_name}") as Page:
        Previous_Lines = Page.readlines()
        Title = console.input("[b]Title: ").strip('')
        New_Lines = [f"Title: {Title}",
             f"Date: {datetime.now().strftime(f'%d/%m/%Y')}",
             ""]
        num_line = 0
        for previous_line in Previous_Lines[3:]:
            Edit_line = Prompt.ask(f"{str(num_line)}: {previous_line}")
            if Edit_line == "END".lower():
                break
            elif Edit_line == "":
                New_Lines.append(previous_line)
            num_line += 1
            New_Lines.append(Edit_line)
        while True:
            New_Line = Prompt.ask(str(num_line))
            if New_Line == "END".lower().strip():
                break
            num_line += 1
            New_Lines.append(New_Line)
    with open(f"{Diary_Info()[0]}/{Page_name}", "w") as Edited_Page:
        for line in New_Lines:
            Edited_Page.write(f"{line}\n")
    Back_To_Main()

def Read_Page(Diary_name, Page_name):
    clear()
    with open(f"{Diary_name}/{Page_name}") as Page:
        Page_Lines = Page.readlines()
    Panel_Content = "".join(Page_Lines)
    Print(Panel(Panel_Content, title=f'[b]{Page_name}', style=Style_Themes["Regular"]))
    Back_To_Main()

def Options_After_Func(options, *responses):
    num = []
    for i, option in enumerate(options):
        Print(Panel(f"{i+1}- {option}", width=30, highlight=True))
        num.append(str(i+1))
    while True:
        u_option = console.input("[b]---> ").strip()
        if u_option in num:
            responses[int(u_option)-1]()
        else:
            Print(Panel("Invalid Key !!", expand=False, style=Style_Themes["Warning"]))
            continue

def Page_Save(Page_Name, Page_Title, Page_First_Line, Page_Text, file_mode='a'):
    with open(f"{Diary_Info()[0]}/{Page_Name}", mode=file_mode) as Page:
                for line in Page_Text:
                    Page.write(f'{line}\n')
    with open('Pages_Data.csv', "a", newline='') as csv_file:
        fieldnames = ['Page_Name', 'Page_Title', 'Page_Date', 'Page_First_Line']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerow({"Page_Name": Page_Name,
                             "Page_Title": Page_Title,
                             "Page_Date": datetime.now().strftime(f'%d/%m/%Y'),
                             "Page_First_Line": Page_First_Line})

##### Decorators #####

def Check_Diary(func):
    def wrapper():
        if os.path.exists("Diary_Info.json"):
            clear()
            func()
        else:
            Make_Diary()
            main()
    return wrapper

def Check_Pages(func):
    @Check_Diary
    def wrapper():
        if Diary_Info()[1] != 0:
            clear()
            func()
        else:
            Print(Panel("There Is NO Pages Yet!!", expand=False, style=Style_Themes["Warning"]))
            Options_After_Func(["Make Your First Page?", "Back To Main?"],
                               lambda: Add_Page(),
                               lambda: main())
    return wrapper

##### Main Func #####

@Check_Pages
def View_Dairy():
    console.print(Panel(figlet_format("View Diary.", font='roman', width=120, justify='center'), expand=False, box=box.ASCII2))
    Print(Panel(f"[u]Diary Name[/u]: {Diary_Info()[0]} {"-"*60} [u]Total Pages[/u]: {Diary_Info()[1]}", width=100, style=Style_Themes["Regular"]))
    for page in os.listdir(Diary_Info()[0]):
        with open('Pages_Data.csv') as Page:
            page_reader = csv.DictReader(Page)
            for row in page_reader:
                Panel_Content = f'[b i u]Title[/b i u]: {row['Page_Title']}\t[b i u]Date[/b i u]: {row['Page_Date']}\n[b i u]Some Content[/b i u]: {row['Page_First_line']}...'.expandtabs(20)
            console.print(Panel(Panel_Content, title=f'[b]{page}', style="italic", border_style="white", width=100))
    Options_After_Func(["Search On Page?","Add Page?","Back To Main?"],
                       lambda: Search_Page(),
                       lambda: Add_Page(),
                       lambda: main())

@Check_Pages
def Search_Page():
    console.print(Panel(figlet_format("Search Page.", font='roman', width=120, justify='center'), expand=False, box=box.ASCII2))
    Page_Name = console.input("[b]Name Of Page: ")
    Diary_name = Diary_Info()[0]
    for name in os.listdir(Diary_name):
        if Page_Name in name and len(Page_Name) == len(name):
            Print(Panel("The Page Is Exist", expand=False, style=Style_Themes["Success"]))
            break
    else:
        Print(Panel("The Page Isn't Exist", expand=False, style=Style_Themes["Warning"]))
        Options_After_Func(["Search Again?", "Add Page?","Back To Main?"],
                           lambda: Search_Page(),
                           lambda: Add_Page(),
                           lambda: main())

    Options_After_Func(["Read The Page", "Edit The Page", "Back To Main"],
                       lambda: Read_Page(Diary_name, Page_Name),
                       lambda: Page_Edit(Page_Name),
                       lambda: main())

@Check_Diary
def Add_Page():
    Print(Panel(figlet_format("Add Page.", font='roman', width=100, justify='center'), expand=False, style=Style_Themes["Regular"], box=box.ASCII2))
    diary_info = Diary_Info()
    # Page Name Condition
    Print("You Can't Change The Name Of The Page Later.. So be Careful", msg_style=Style_Themes['Warning'])
    while True:
        Page_name = console.input("[b]Enter Page Name: ").strip()
        if Page_name == "BACK":
            main()
        if all(char.isalnum() or char.isspace() for char in Page_name):
            break
        else:
            Print(Panel("Invalid Key !!", style=Style_Themes["Warning"], expand=False))
            continue
    for name in os.listdir(diary_info[0]):
        if Page_name in name and len(Page_name) == len(name):
            Print(Panel("The Page Is already Exist", expand=False, style=Style_Themes['Warning']))
            Options_After_Func(["Do You Want To Edit It?", "Add Another Page?", "Back To Main?"],
                               lambda: Page_Edit(Page_name),
                               lambda: Add_Page(),
                               lambda: main())
    text = Text_Write(Page_name)
    while True:
        confirmation = console.input("[b]are you shure you want to add this page? ").strip().lower()
        if confirmation == "y" or confirmation == "yes":
            Page_Save(Page_name, text[0], text[1][3], text[1])
            
            Options_After_Func(["Read The Page?", "Add Another Page?", "Back To Main?"],
                               lambda: Read_Page(diary_info[0], Page_name),
                               lambda: Add_Page(),
                               lambda: main())
        elif confirmation == "n" or confirmation == "no":
            Options_After_Func(["Edit The Text?", "Back To Main?"],
                               lambda: Text_Edit(Page_name, text[1]),
                               lambda: main())
        else:
            Print(Panel("Invalid Key !!", style=Style_Themes['Warning'], expand=False))
            continue
    
@Check_Pages
def Delete_Page():
    console.print(Panel(figlet_format("Delete Page.", font='roman', width=120, justify='center'), expand=False, box=box.ASCII2))
    Page_Name = console.input("[b]Enter Page Name: ").strip()
    Diary_Name = Diary_Info()[0]
    if os.path.exists(f"{Diary_Name}/{Page_Name}"):
        # Delete File
        os.remove(f"{Diary_Name}/{Page_Name}")
        # Delete File Data
        with open('Pages_Data.csv', "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            rows_to_keep = []
            for row in csv_reader:
                if Page_Name != row[0]:
                    rows_to_keep.append(row)
            with open('Pages_Data.csv', 'w', newline='') as result:
                csv_writer = csv.writer(result)
                for line in rows_to_keep:
                    csv_writer.writerow(line)

        Options_After_Func(["Delete Another Page?", "Back To Main?"],
                           lambda: Delete_Page(),
                           lambda: main())
    else:
        Print(Panel("The Page Isn't Exist", expand=False, style=Style_Themes["Warning"]))
        Back_To_Main()

##### Main #####
def main():
    clear()
    Print(Panel(figlet_format("My Diary.", font='roman', width=100, justify='center'), expand=False, style=Style_Themes["Regular"], box=box.ASCII2))
    for line in ("1- View My Diary",
            "2- Search On Day",
            "3- Add New Page",
            "4- Delete Page",
            "5- Quit"):
        Panel(line, expand=False)
        Print(Panel(line, expand=False, box= box.SQUARE, style=Style_Themes["Regular"], highlight=True))
    while True:
        u_option = console.input("[b][b]Enter Your Option: ").strip()
        if u_option in [str(num) for num in range(1, 6)]:
            break
        else:
            Print(Panel("Invalid Option !", expand=False, style=Style_Themes["Warning"]))
    
    if u_option == "5":
        quit()
    if u_option == "1":
        View_Dairy()
    elif u_option == "2":
        Search_Page()
    elif u_option == "3":
        Add_Page()
    else:
        Delete_Page()

if __name__ == "__main__":
    main()
