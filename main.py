import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Algo to PY 0.1')
root.resizable(False, False)
root.geometry('300x150')

keywords = {
    "<-": "=",
    "Ecrire": "print",
    "Fin": ""
}
Vars = {}
def val_by_type(t):
    if t == "Reel":
        return float(0)
    elif t == "Entier":
        return 0
    else:
        return '""'

def type_to_fn(t):
    if t == "Reel":
        return "float"
    elif t == "Entier":
        return "int"
    else:
        return "str" 

def to_py(l):
    nl = l
    
    for key in keywords.keys():
        nl = nl.replace(key, keywords[key])
        
    return nl



def main(f):

    python_code = ""
    begin = False
    
    with open(f, mode="r") as algo:
        for x, line in enumerate(algo.readlines()):
            if "Var" in line:
                split = line.split("Var")
                split = [i for i in split if i]
                if len(split) == 1:
                    var = split[0].split(':')
                    if len(var) == 2:
                        name = var[0].strip()
                        type_ = var[1].strip()
                        Vars[name] = type_
                        if "=" in type_:
                            val = type_.split("=")
                            if len(val) == 2:
                                python_code += f"\n{name} = {val[1].strip()}"
                        else:
                            python_code += f"\n{name} = {val_by_type(type_)}"
            if begin:
                if "Lire" in line:
                    var = line.split('(')
                    if len(var) == 2:
                        name = var[1][:-2]
                        python_code += f"\n{name} = {type_to_fn(Vars[name])}(input())\n"
                else:
                    python_code += to_py(line.strip()+"\n")
                    
            if line == "Debut:\n":
                python_code += "\n"
                begin = True

    with open(f[:-3] + "_to_python_.py", 'w') as f:
        f.write(python_code)


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Selcet algo file',
        initialdir='/',
        filetypes=filetypes
    )

    main(filename)

def git():
    import webbrowser
    webbrowser.open_new(r"https://github.com/ItzCyzmiX")

# open button
open_button = ttk.Button(
    root,
    text='Open a algo file',
    command=select_file
)

open_button.pack(expand=True)

link = ttk.Button(root, text='Git Repo', command=git)
link.pack(expand=True)

root.mainloop()

