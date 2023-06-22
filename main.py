import os
import colorama
from colorama import Fore as fg
from colorama import Back as bg
import time

running = False
user = None
otterLogo = [
    "  _______  ",
    "</ . _ . \>",
    " \___^___/ ",
    " -OtterOS- ",
]
cl_history = []
files = []
active_file = None

class file:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.contents = []

def start_up():
    global user
    os.system("cls")
    for i in otterLogo:
        print(bg.BLACK + fg.WHITE + i)
    time.sleep(1)
    os.system("cls")
    user = input(fg.WHITE + "user: ")
    cl()

def cl():
    print(fg.WHITE)
    global user
    global cl_history
    global active_file
    os.system("cls")
    for i in cl_history:
        print(i)
    cmd = input(f"{fg.WHITE}<{user}>")
    cl_history.append(f"{fg.WHITE}<{user}>{cmd}")
    if cmd[0:4] == "file":
        if cmd[5:7] == "-c":
            try:
                files.append(
                    file(
                        name=cmd[8:cmd.index(".")],
                        type=cmd[cmd.index(".") + 1:],
                    )
                )
                cl_history.append(f"{fg.GREEN}<sys>created {cmd[8:]}")
                for i in files:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        active_file = i
                        cl_history.append(f"{fg.GREEN}<sys>{active_file.name}.{active_file.type} is now open")
            except:
                cl_history.append(f"{fg.RED}<sys>unable to create {cmd[8:]}")
        if cmd[5:7] == "-o":
            try:
                for i in files:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        active_file = i
                        cl_history.append(f"{fg.GREEN}<sys>{active_file.name}.{active_file.type} is now open")
            except:
                cl_history.append(f"{fg.RED}<sys>unable to open file")
        if cmd[5:7] == "-r":
            try:
                for i in files:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        cl_history.append(f"{fg.GREEN}<{i.name}.{i.type}>")
                        for j in i.contents:
                            cl_history.append(f"   {i.contents.index(j) + 1}.{j}")
            except:
                try:
                    cl_history.append(f"{fg.GREEN}<{active_file.name}.{active_file.type}>")
                    for j in active_file.contents:
                        cl_history.append(f"   {active_file.contents.index(j) + 1}.{j}") 
                except:
                    cl_history.append(f"{fg.RED}<sys>unable to read file")
        if cmd[5:7] == "-s":
            try:
                cl_history.append(f"{fg.GREEN}<sys>")
                for i in files:
                    cl_history.append(f"   {fg.GREEN}{i.name}.{i.type}")
            except:
                cl_history.append(f"{fg.RED}<sys>unable to display file list")
        if cmd[5:7] == "-e":
            try:
                active_file.contents[int(cmd[cmd.index("@") + 1:cmd.index("*")]) - 1] = cmd[cmd.index("*") + 1:]
                cl_history.append(f"{fg.GREEN}<sys>{active_file.name}.{active_file.type} updated")
            except:
                try:
                    active_file.contents.append(cmd[cmd.index("*") + 1:])
                    cl_history.append(f"{fg.GREEN}<sys>{active_file.name}.{active_file.type} updated")
                except:
                    cl_history.append(f"{fg.RED}<sys>unable to edit file list")
        cl()
    if cmd[0:3] == "del":
        try:
            for i in files:
                if i.name == cmd[4:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                    cl_history.append(f"{fg.GREEN}<sys>are you sure you want to delete {i.name}.{i.type}?")
                    print(f"{fg.GREEN}<sys>are you sure you want to delete {i.name}.{i.type}?")
                    yn = True
                    while yn:
                        answer = input("(y/n)")
                        cl_history.append("(y/n)"+answer)
                        if answer.lower() == "y":
                            files.remove(i)
                            cl_history.append(f"{fg.GREEN}<sys>{i.name}.{i.type} deleted")
                            yn = False
                        if answer.lower() == "n":
                            yn = False
                            cl_history.append(f"{fg.GREEN}<sys>cancelled deletion")
        except:
            cl_history.append(f"{fg.RED}<sys>unable to delete {cmd[8:]}")
        cl()
    if cmd[0:3] == "cls":
        cl_history = []
        cl()
    else:
        cl_history.append(f"{fg.RED}<sys>unknown command")
        cl()


#cmd = input(f"${user}")
start_up()