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
        self.success = fg.GREEN
        self.err = fg.RED

class file:
    def __init__(self,name,type,parent):
        self.name = name
        self.type = type
        self.contents = []
        self.parent = parent
        self.path = name
        i = self
        while i.parent != "None":
            self.path = i.parent.name + "\\" + self.path
            i = i.parent

class dir:
    def __init__(self,name,parent):
        self.name = name
        self.type = "dir"
        self.contents = []
        self.parent = parent
        self.path = name
        i = self
        while i.parent != "None":
            self.path = i.parent.name + "\\" + self.path
            i = i.parent

main = dir(
    "main",
    parent="None"
)

active_dir = main

sys_clr = clr()

print(sys_clr.bg)
print(sys_clr.fg)

def start_up():
    global user
    os.system("cls")
    for i in otterLogo:
        print(i)
    time.sleep(1)
    os.system("cls")
    user = input(sys_clr.fg + "$user: ")

    #user = input(sys_clr.fg + "$pass: ")
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
    cl_history.append(f"{sys_clr.fg}${user}>{cmd}")
    if cmd == "debug":
        for i in main.contents:
            print(i.name)
        input()
    if cmd[0:4] == "file":
        if cmd[5:7] == "-c":
            try:
                active_dir.contents.append(
                    file(
                        name=cmd[8:cmd.index(".")],
                        type=cmd[cmd.index(".") + 1:],
                        parent=active_dir,
                    )
                )
                cl_history.append(f"{sys_clr.success}$sys>_created {cmd[8:]}")
                for i in active_dir.contents:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        active_file = i
                        files.append(active_file)
                        cl_history.append(f"{sys_clr.success}$sys>_{active_file.name}.{active_file.type} is now open")
            except:
                cl_history.append(f"{sys_clr.err}$sys>_unable to create {cmd[8:]}")
        if cmd[5:7] == "-o":
            try:
                for i in active_dir.contents:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        active_file = i
                        cl_history.append(f"{sys_clr.success}$sys>_{active_file.name}.{active_file.type} is now open")
            except:
                cl_history.append(f"{sys_clr.err}$sys>_unable to open file")
        if cmd[5:7] == "-r":
            try:
                for i in active_dir.contents:
                    if i.name == cmd[8:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                        cl_history.append(f"{sys_clr.success}${i.name}.{i.type}>")
                        for j in i.contents:
                            cl_history.append(f"   {i.contents.index(j) + 1}.{j}")
            except:
                try:
                    cl_history.append(f"{sys_clr.success}${active_file.name}.{active_file.type}>")
                    for j in active_file.contents:
                        cl_history.append(f"   {active_file.contents.index(j) + 1}.{j}") 
                except:
                    cl_history.append(f"{sys_clr.err}$sys>_unable to read file")
        if cmd[5:7] == "-e":
            try:
                active_file.contents[int(cmd[cmd.index("@") - 1:])] = cmd[8:cmd.index("@")]
                cl_history.append(f"{sys_clr.success}$sys>_{active_file.name}.{active_file.type} updated")
            except:
                try:
                    active_file.contents.append(cmd[8:cmd.index("@")])
                    cl_history.append(f"{sys_clr.success}$sys>_{active_file.name}.{active_file.type} updated")
                except:
                    try:
                        active_file.contents.append(cmd[8:])
                    except:
                        cl_history.append(f"{sys_clr.err}$sys>_unable to edit file list")
        if cmd[5:7] == "-n":
            try:
                namePlaceHolder = active_file.name
                active_file.name = cmd[8:]
                cl_history.append(f"{sys_clr.success}$sys>_{namePlaceHolder}.{active_file.type} is now {active_file.name}.{active_file.type}")
            except:
                cl_history.append(f"{sys_clr.err}$sys>_unable to edit file list")
        if cmd == "file":
            cl_history.append(f"{sys_clr.success}$sys>_{active_file.path}.{active_file.type}")
        cl()
    if cmd[0:3] == "del":
        try:
            for i in active_dir.contents:
                if i.name == cmd[4:cmd.index(".")] and i.type == cmd[cmd.index(".") + 1:]:
                    cl_history.append(f"{sys_clr.success}$sys>_are you sure you want to delete {i.name}.{i.type}?")
                    print(f"{sys_clr.success}$sys>_are you sure you want to delete {i.name}.{i.type}?")
                    yn = True
                    while yn:
                        answer = input("(y/n)")
                        cl_history.append("(y/n)"+answer)
                        if answer.lower() == "y":
                            active_dir.contents.remove(i)
                            cl_history.append(f"{sys_clr.success}$sys>_{i.name}.{i.type} deleted")
                            yn = False
                        if answer.lower() == "n":
                            yn = False
                            cl_history.append(f"{sys_clr.success}$sys>_cancelled deletion")
        except:
            cl_history.append(f"{sys_clr.err}$sys>_unable to delete {cmd[8:]}")
        cl()
    if cmd[0:3] == "cls":
        cl_history = []
        cl()
    if cmd[0:3] == "dir":
        if cmd[4:6] == "-c":
            try:
                active_dir.contents.append(
                    dir(
                        name=cmd[7:],
                        parent=active_dir,
                    )
                )

                cl_history.append(f"{sys_clr.success}$sys>_created {cmd[7:]}")
                for i in active_dir.contents:
                    if i.name == cmd[7:] and i.type == "dir":
                        active_dir = i
                        dirs.append(i)
                        cl_history.append(f"{sys_clr.success}$sys>_dir:{active_dir.name} is now open")
            except:
                cl_history.append(f"{sys_clr.err}$sys>_unable to create {cmd[7:]}")
            cl()
        if cmd[4:6] == "-s":
            try:
                cl_history.append(f"{sys_clr.success}$sys>_{active_dir.name}")
                for i in active_dir.contents:
                    cl_history.append(f"   {sys_clr.success}{i.name}.{i.type}")
            except:
                cl_history.append(f"{sys_clr.err}$sys>_unable to display dir contents")
            cl()
        if cmd[5:7] == "-o":
            try:
                for i in active_dir.contents:
                    if i.name == cmd[7:] and i.type == "dir":
                        active_dir = i
                        cl_history.append(f"{sys_clr.success}$sys>_dir:{active_dir.name} is now open")
            except:
                cl_history.append(f"{sys_clr.err}$sys>_unable to open directory")
            cl()
        if cmd[5:7] == "-n":
            try:
                namePlaceHolder = active_dir.name
                active_dir.name = cmd[8:]
                cl_history.append(f"{sys_clr.success}$sys>_{namePlaceHolder} is now {active_dir.name}")
            except:
                cl_history.append(f"{sys_clr.err}$sys>_unable to edit file list")
        if cmd == "dir":
            cl_history.append(f"{sys_clr.success}$sys>_{active_dir.path}")
        cl()
    if cmd[0:3] == "nav":
        if cmd[4:6] == "-b":
            try:
                active_dir = active_dir.parent
                cl_history.append(f"{sys_clr.err}$sys>_navigated to {active_dir.path}")
            except:
                cl_history.append(f"{sys_clr.err}$sys>_unable to navigate to {active_dir.path}")
            cl()
    else:
        cl_history.append(f"{sys_clr.err}$sys>_unknown command")
        cl()


#cmd = input(f"${user}")
start_up()