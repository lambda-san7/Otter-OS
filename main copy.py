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
dirs = []
active_file = None
active_dir = None

class clr:
    def __init__(self):
        self.bg = bg.BLUE
        self.fg = fg.WHITE

class file:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.contents = []

class dir:
    def __init__(self,name):
        self.name = name
        self.type = "dir"
        self.contents = []

main = dir("main")

active_dir = main

sys_clr = clr()

def start_up():
    global user
    os.system("cls")
    print(sys_clr.bg)
    for i in otterLogo:
        print(sys_clr.fg + i)
    time.sleep(1)
    os.system("cls")
    user = input(sys_clr.fg + "$user: ")
    user = input(sys_clr.fg + "$pass: ")
    cl()

def cl():
    print(sys_clr.fg)
    global user
    global cl_history
    global active_file
    global active_dir
    os.system("cls")
    for i in cl_history:
        print(i)
    cmd = input(f"{sys_clr.fg}${user}>")
    cl_history.append(f"{sys_clr.fg}<{user}>{cmd}")
    if cmd[0:4] == "file":
        if cmd[5:7] == "-c":
            try:
                active_dir.contents.append(
                    file(
                        name=cmd[8:cmd.index(".")],
                        type=cmd[cmd.index(".") + 1:],
                    )
                )
                cl_history.append(f"{fg.GREEN}$sys>_created {cmd[8:]}")
                for i in active_dir.contents:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        active_file = i
                        files.append(active_file)
                        cl_history.append(f"{fg.GREEN}$sys>_{active_file.name}.{active_file.type} is now open")
            except:
                cl_history.append(f"{fg.RED}$sys>_unable to create {cmd[8:]}")
        if cmd[5:7] == "-o":
            try:
                for i in active_dir.contents:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        active_file = i
                        cl_history.append(f"{fg.GREEN}$sys>_{active_file.name}.{active_file.type} is now open")
            except:
                cl_history.append(f"{fg.RED}$sys>_unable to open file")
        if cmd[5:7] == "-r":
            try:
                for i in active_dir.contents:
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
                    cl_history.append(f"{fg.RED}$sys>_unable to read file")
        if cmd[5:7] == "-e":
            try:
                active_file.contents[int(cmd[cmd.index("@") - 1:])] = cmd[8:cmd.index("@")]
                cl_history.append(f"{fg.GREEN}$sys>_{active_file.name}.{active_file.type} updated")
            except:
                try:
                    active_file.contents.append(cmd[8:cmd.index("@")])
                    cl_history.append(f"{fg.GREEN}$sys>_{active_file.name}.{active_file.type} updated")
                except:
                    try:
                        active_file.contents.append(cmd[8:])
                    except:
                        cl_history.append(f"{fg.RED}$sys>_unable to edit file list")
        if cmd[5:7] == "-n":
            try:
                namePlaceHolder = active_file.name
                active_file.name = cmd[8:]
                cl_history.append(f"{fg.GREEN}$sys>_{namePlaceHolder}.{active_file.type} is now {active_file.name}.{active_file.type}")
            except:
                cl_history.append(f"{fg.RED}$sys>_unable to edit file list")
        cl()
    if cmd[0:3] == "del":
        try:
            for i in active_dir.contents:
                if i.name == cmd[4:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                    cl_history.append(f"{fg.GREEN}$sys>_are you sure you want to delete {i.name}.{i.type}?")
                    print(f"{fg.GREEN}$sys>_are you sure you want to delete {i.name}.{i.type}?")
                    yn = True
                    while yn:
                        answer = input("(y/n)")
                        cl_history.append("(y/n)"+answer)
                        if answer.lower() == "y":
                            active_dir.contents.remove(i)
                            cl_history.append(f"{fg.GREEN}$sys>_{i.name}.{i.type} deleted")
                            yn = False
                        if answer.lower() == "n":
                            yn = False
                            cl_history.append(f"{fg.GREEN}$sys>_cancelled deletion")
        except:
            cl_history.append(f"{fg.RED}$sys>_unable to delete {cmd[8:]}")
        cl()
    if cmd[0:3] == "cls":
        cl_history = []
        cl()
    if cmd[0:3] == "dir":
        if cmd[4:6] == "-c":
            try:
                active_dir.contents.append(
                    dir(
                        name=cmd[7:]
                    )
                )

                cl_history.append(f"{fg.GREEN}$sys>_created {cmd[7:]}")
                for i in active_dir.contents:
                    if i.name == cmd[7:] and i.type == "dir":
                        active_dir = i
                        dirs.append(i)
                        cl_history.append(f"{fg.GREEN}$sys>_dir:{active_dir.name} is now open")
            except:
                cl_history.append(f"{fg.RED}$sys>_unable to create {cmd[7:]}")
            cl()
        if cmd[4:6] == "-s":
            try:
                cl_history.append(f"{fg.GREEN}$sys>_{active_dir.name}")
                for i in active_dir.contents:
                    cl_history.append(f"   {fg.GREEN}{i.name}.{i.type}")
            except:
                cl_history.append(f"{fg.RED}$sys>_unable to display dir contents")
            cl()
        if cmd[5:7] == "-o":
            try:
                for i in active_dir.contents:
                    if i.name == cmd[7:] and i.type == "dir":
                        active_dir = i
                        cl_history.append(f"{fg.GREEN}$sys>_dir:{active_dir.name} is now open")
            except:
                cl_history.append(f"{fg.RED}$sys>_unable to open directory")
            cl()
        if cmd[5:7] == "-n":
            try:
                namePlaceHolder = active_dir.name
                active_dir.name = cmd[8:]
                cl_history.append(f"{fg.GREEN}$sys>_{namePlaceHolder} is now {active_dir.name}")
            except:
                cl_history.append(f"{fg.RED}$sys>_unable to edit file list")
        if cmd == "dir":
            cl_history.append(f"{fg.GREEN}$sys>_{active_dir.name}")
        cl()
    if cmd[0:3] == "nav":
        if cmd[4:6] == "-f":
            try:
                active_dir.contents.append(
                    dir(
                        name=cmd[7:]
                    )
                )
                cl_history.append(f"{fg.GREEN}$sys>_created {cmd[7:]}")
                for i in active_dir.contents:
                    if i.name == cmd[7:] and i.type == "dir":
                        active_dir = i
                        cl_history.append(f"{fg.GREEN}$sys>_dir:{active_dir.name} is now open")
            except:
                cl_history.append(f"{fg.RED}$sys>_unable to create {cmd[7:]}")
            cl()
    else:
        cl_history.append(f"{fg.RED}$sys>_unknown command")
        cl()


#cmd = input(f"${user}")
start_up()