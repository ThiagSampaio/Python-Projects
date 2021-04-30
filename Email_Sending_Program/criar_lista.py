from tkinter import *
def criar_lista(lista_estados):
    list_var = StringVar(value=lista_estados)
    l = Listbox(listvariable=list_var)
    l.grid(column=0, row=1)