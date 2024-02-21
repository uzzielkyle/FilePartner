from typing import Optional, Tuple, Union
from customtkinter import *
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
import os
import subprocess


class TreeView(CTkFrame):
    WIDTH: int = 300
    HEIGHT: int = 50
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

    def __init__(self, *args,
                 bg_color: str | Tuple[str, str] = 'transparent',
                 fg_color: str | Tuple[str, str] = 'whitesmoke',
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, bg_color=bg_color, fg_color=fg_color,
                         corner_radius=corner_radius, **kwargs)

        self.curr_rows = 0

        self.configure(width=self.WIDTH)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.style = ttk.Style()
        self.style.configure('mystyle.Treeview.Heading',
                             font=('Arial', 13, 'bold'))
        self.style.configure('mystyle.Treeview',
                             font=('Arial', 11), rowheight=30)

        self.tree = ttk.Treeview(
            self, style='mystyle.Treeview', selectmode='browse')
        self.tree['columns'] = ('Link', 'Folder', 'Pages')

        self.tree.column('#0', width=0, stretch=False)
        self.tree.column('Link', width=0, stretch=False)
        self.tree.column('Folder', anchor='w', minwidth=int(
            self.WIDTH*1.65), stretch=True)
        self.tree.column('Pages', anchor='center',
                         minwidth=int(self.WIDTH*.5), stretch=False)

        self.tree.heading('#0', text='', anchor='center')
        self.tree.heading('Link', text='Link', anchor='center')
        self.tree.heading('Folder', text='Folder', anchor='center')
        self.tree.heading('Pages', text='Pages', anchor='center')

        self.tree.grid(row=0, column=0, padx=(
            10, 0), pady=(15, 5), sticky='nsew')

        self.scrollbar = ttk.Scrollbar(
            self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, padx=(0, 10),
                            pady=(15, 5), sticky='ns')

        self.tree.bind('<Double-1>', self.on_double_click)
        self.tree.tag_configure('output', background='whitesmoke')

        self.clear_btn = CTkButton(
            self, text='Clear', command=self.clear, corner_radius=0)
        self.clear_btn.grid(row=1, column=0, columnspan=2,
                            padx=7.25, pady=(0, 5), sticky='ew')

    def clear(self):
        for data in self.tree.get_children():
            self.tree.delete(data)

    def display_outputs(self, values: Tuple):
        for row, data in enumerate(values):
            self.tree.insert(parent='', index=row, iid=row, values=data)

    def on_double_click(self, event):
        try:
            path = self.tree.item(self.tree.focus())['values'][0]

            subprocess.run(
                [self.FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

        except:
            self.blank_searchbar_message = CTkMessagebox(fg_color='whitesmoke', bg_color='whitesmoke', title='Link Error',
                                                         message='Cannot locate file.', icon='warning', justify='center', font=('Arial', 11), option_focus='option_1', sound=True)


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)

            self.grid_columnconfigure(0, weight=1)

            self.treeview = TreeView(self)
            self.treeview.grid(row=0, column=0)

            my_list = ['String 1', 'String 2', 'String 3', 'String 4', 'String 5',
                       'String 6', 'String 7', 'String 8', 'String 9', 'String 10']
            my_list_copy = my_list.copy()
            my_list.extend(my_list_copy)

            self.treeview.display_folders(my_list)
            self.treeview.display_pdfs([('ouput.pdf', 8)])

    app = Tester()
    app.mainloop()
