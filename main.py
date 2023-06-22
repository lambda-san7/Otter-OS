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
        self.contents = [
            "test",
            "hi",
            "hello",
        ]

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
            except:
                cl_history.append(f"{fg.RED}<sys>unable to create {cmd[8:]}")
        if cmd[5:7] == "-o":
            try:
                for i in files:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        active_file = i
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
            except:
                cl_history.append(f"{fg.RED}<sys>unable to display file list")
        cl()
    if cmd[0:3] == "cls":
        cl_history = []
        cl()
    else:
        cl_history.append(f"{fg.RED}<sys>unknown command")
        cl()


#cmd = input(f"${user}")
start_up()