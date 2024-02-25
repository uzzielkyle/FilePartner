from typing import Optional, Tuple, Union
from customtkinter import *
from utils.docx_to_pdf import DocxConverter
from utils.pdf_merger import LogicHandler
from CTkMessagebox import CTkMessagebox
from threading import Thread
import os


class Converter(CTkFrame):
    WIDTH: int = 600
    HEIGHT: int = 50

    def __init__(self, *args,
                 get_path_func,
                 bg_color: str | Tuple[str, str] = 'transparent',
                 fg_color: str | Tuple[str, str] = 'transparent',
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, bg_color=bg_color, fg_color=fg_color,
                         corner_radius=corner_radius, **kwargs)

        self.docx_converter = DocxConverter()
        self.logic_handler = LogicHandler()

        self.get_path = get_path_func

        self.treeview_connection = None

        self.grid_columnconfigure((0, 1), weight=1)

        # Will figure out kung paano talaga magamit ito...
        # 2023-11-07: By multithreading hehe
        self.progress_bar = CTkProgressBar(
            self, orientation='horizontal', width=self.WIDTH - 110)
        self.progress_bar.grid(row=0, column=0, columnspan=2,
                               padx=0, pady=(0, 5), sticky='ew')
        self.progress_bar.configure(mode='indeterminate')

        # self.merge_btn = CTkButton(self, text='Merge', width=90, corner_radius=corner_radius, command=lambda: self.merge())
        self.convert_btn = CTkButton(self, text='Convert', width=90, corner_radius=corner_radius,
                                     command=lambda: Thread(target=self.convert).start())
        self.convert_btn.grid(row=0, column=2, padx=(20, 0),
                              pady=(0, 5), sticky='ew')

    def convert(self) -> None:
        try:
            folder_path = self.get_path()

            if not folder_path:
                self.blank_searchbar_message = CTkMessagebox(fg_color='whitesmoke', bg_color='whitesmoke', title='Blank Entry',
                                                             message='Please input a folder path.', icon='warning', justify='center', font=('Arial', 11), option_focus='option_1', sound=True)
                return

            self.clear_search()
            self.clear_treeview()
            self.working_state()

            if not folder_path.endswith(os.path.sep):
                folder_path += os.path.sep

            folder_path = os.path.normpath(folder_path)

            roots_not_empty = self.logic_handler.scan_folders(
                folder_path=folder_path)

            if not roots_not_empty:
                self.no_files_message = CTkMessagebox(fg_color='whitesmoke', bg_color='whitesmoke', title='No PDFs found',
                                                      message='No PDF file inside the directory.', icon='info', justify='center', font=('Arial', 11), option_focus='option_1')

                self.idle_state()

                return

            outputs = self.docx_converter.bulk_conversion(folder_path)

            if not outputs:
                self.no_merging_message = CTkMessagebox(fg_color='whitesmoke', bg_color='whitesmoke', title='No Merging Happened',
                                                        message='The root directory (and its subdirectories) only contained one PDF file.', icon='info', justify='center', font=('Arial', 11), option_focus='option_1', sound=True)

                self.idle_state()

                return

            self.idle_state()

        except:
            self.blank_searchbar_message = CTkMessagebox(fg_color='whitesmoke', bg_color='whitesmoke', title='Error',
                                                         message='Error in merging PDFs.', icon='warning', justify='center', font=('Arial', 11), option_focus='option_1', sound=True)

            self.idle_state()

    def idle_state(self):
        self.progress_bar.stop()
        self.merge_btn.configure(state='normal')

    def working_state(self):
        self.progress_bar.start()
        self.merge_btn.configure(state='disabled')
