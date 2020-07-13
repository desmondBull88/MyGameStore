import tkinter as tk
from tkinter import ttk
import backend

root = tk.Tk()

title = ttk.Label(root, text='Title')
title.grid(row=0, column=0, pady=3, padx=3)

title_entry = ttk.Entry(root)
title_entry.grid(row=0, column=1, pady=3, padx=3)

year = ttk.Label(root, text='Year')
year.grid(row=1, column=0, pady=3, padx=3)

year_entry = ttk.Entry(root)
year_entry.grid(row=1, column=1, pady=3, padx=3)

gameCreator = ttk.Label(root, text='Game Company')
gameCreator.grid(row=0, column=2, pady=3, padx=3)

gameCreator_entry = ttk.Entry(root)
gameCreator_entry.grid(row=0, column=3, pady=3, padx=3)

upc = ttk.Label(root, text='UPC')
upc.grid(row=1, column=2, pady=3, padx=3)

upc_entry = ttk.Entry(root)
upc_entry.grid(row=1, column=3, pady=3, padx=3)

view_all = ttk.Button(root, text='View All')
view_all.grid(row=2, column=3, pady=3)

search_entry = ttk.Button(root, text='Search Entry')
search_entry.grid(row=3, column=3, pady=3)

add_entry = ttk.Button(root, text='Add Entry')
add_entry.grid(row=4, column=3, pady=3)

update = ttk.Button(root, text='Update')
update.grid(row=5, column=3, pady=3)

delete = ttk.Button(root, text='Delete')
delete.grid(row=6, column=3, pady=3)

close = ttk.Button(root, text='Close')
close.grid(row=7, column=3, pady=3)

view_area = tk.Listbox(root, width=30)
view_area.grid(row=2, column=1, rowspan=6, columnspan=2)

scroll = ttk.Scrollbar(root)
scroll.place(relx=0.65, rely=0.5)

view_area.configure(yscrollcommand=scroll.set)
scroll.configure(command=view_area.yview)
root.mainloop()
