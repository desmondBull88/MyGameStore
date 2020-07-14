import tkinter as tk
from tkinter import ttk
import backend2


def get_selected_row(event):
    try:
        global selected_tuple
        index = view_area.curselection()[0]
        selected_tuple = view_area.get(index)

        title_entry.delete(0, tk.END)
        title_entry.insert(tk.END, selected_tuple[1])

        year_entry.delete(0, tk.END)
        year_entry.insert(tk.END, selected_tuple[2])

        gameCreator_entry.delete(0, tk.END)
        gameCreator_entry.insert(tk.END, selected_tuple[3])

        upc_entry.delete(0, tk.END)
        upc_entry.insert(tk.END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    view_area.delete(0, tk.END)
    for row in backend2.view():
        view_area.insert(tk.END, row)


def search_command():
    view_area.delete(0, tk.END)
    for row in backend2.search(title_text.get(), gameCreator_text.get(), year_text.get(), upc_text.get()):
        view_area.insert(tk.END, row)


def add_command():
    backend2.insert(title_text.get(), gameCreator_text.get(),
                    year_text.get(), upc_text.get())
    view_area.delete(0, tk.END)
    view_area.insert(tk.END, (title_text.get(), gameCreator_text.get(),
                              year_text.get(), upc_text.get()))


def delete_command():
    backend2.delete(selected_tuple[0])


def update_command():
    backend2.update(selected_tuple[0], title_text.get(), gameCreator_text.get(),
                    year_text.get(), upc_text.get())


root = tk.Tk()

title = ttk.Label(root, text='Title')
title.grid(row=0, column=0, pady=3, padx=3)

title_text = tk.StringVar()
title_entry = ttk.Entry(root, textvariable=title_text)
title_entry.grid(row=0, column=1, pady=3, padx=3)

year = ttk.Label(root, text='Year')
year.grid(row=1, column=0, pady=3, padx=3)

year_text = tk.StringVar()
year_entry = ttk.Entry(root, textvariable=year_text)
year_entry.grid(row=1, column=1, pady=3, padx=3)

gameCreator = ttk.Label(root, text='Game Company')
gameCreator.grid(row=0, column=2, pady=3, padx=3)

gameCreator_text = tk.StringVar()
gameCreator_entry = ttk.Entry(root, textvariable=gameCreator_text)
gameCreator_entry.grid(row=0, column=3, pady=3, padx=3)

upc = ttk.Label(root, text='UPC')
upc.grid(row=1, column=2, pady=3, padx=3)

upc_text = tk.StringVar()
upc_entry = ttk.Entry(root, textvariable=upc_text)
upc_entry.grid(row=1, column=3, pady=3, padx=3)

view_all = ttk.Button(root, text='View All', command=view_command)
view_all.grid(row=2, column=3, pady=3)

search_entry = ttk.Button(root, text='Search Entry', command=search_command)
search_entry.grid(row=3, column=3, pady=3)

add_entry = ttk.Button(root, text='Add Entry', command=add_command)
add_entry.grid(row=4, column=3, pady=3)

update = ttk.Button(root, text='Update', command=update_command)
update.grid(row=5, column=3, pady=3)

delete = ttk.Button(root, text='Delete', command=delete_command)
delete.grid(row=6, column=3, pady=3)

close = ttk.Button(root, text='Close', command=root.destroy)
close.grid(row=7, column=3, pady=3)

view_area = tk.Listbox(root, width=30)
view_area.grid(row=2, column=1, rowspan=6, columnspan=2)

view_area.bind('<<ListboxSelect>>', get_selected_row)

scroll = ttk.Scrollbar(root)
scroll.place(relx=0.65, rely=0.5)

view_area.configure(yscrollcommand=scroll.set)
scroll.configure(command=view_area.yview)
root.mainloop()
