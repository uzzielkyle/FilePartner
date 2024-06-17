from typing import Optional, Tuple, Union
from customtkinter import *
from .appearance_mode_toggler import AppearanceModeToggler
from PIL import Image


class SideBar(CTkFrame):
    WIDTH = 50

    def __init__(self, *args,
                 page1, page2=None, page3=None,
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, corner_radius=corner_radius, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.page1 = page1

        self.logo_img = CTkImage(
            light_image=Image.open('app/assets/img/logo.png'), dark_image=Image.open('app/assets/img/logo.png'), size=(100, 100))
        self.logo_img_lbl = CTkLabel(self, text='', image=self.logo_img)
        self.logo_img_lbl.grid(row=0, column=0, pady=(20, 5))

        self.sidebar_title_label = CTkLabel(
            self, text='FilePartner', font=CTkFont(size=15, weight='bold'))
        self.sidebar_title_label.grid(row=1, column=0)

        self.sidebar_subtitle_label = CTkLabel(
            self, text='Your Lifetime Partner for Digital Files', font=CTkFont(size=12, weight='normal'))
        self.sidebar_subtitle_label.grid(
            row=2, column=0, pady=(0, 20), padx=10)

        self.nav_frm = CTkFrame(
            self, corner_radius=corner_radius, fg_color="transparent")
        self.nav_frm.grid(row=3, column=0, sticky='ew')
        self.nav_frm.grid_columnconfigure(0, weight=1)

        self.bulk_merge_btn = CTkButton(
            self.nav_frm, text='Bulk PDF Merger', height=40, corner_radius=corner_radius, fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'), anchor='center', command=lambda: self.select_frame_by_name('bulk_pdf'))
        self.bulk_merge_btn.grid(
            row=0, column=0, padx=(0, 1), sticky='ew')

        self.appearance_mode_toggler = AppearanceModeToggler(master=self)
        self.appearance_mode_toggler.grid(
            row=4, column=0, padx=10, pady=20, sticky='s')

        # select default frame
        self.select_frame_by_name('bulk_pdf')

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.bulk_merge_btn.configure(
            fg_color=('gray65', 'gray40') if name == 'bulk_pdf' else 'transparent')

        # show selected frame
        if name == 'bulk_pdf':
            self.page1.grid(row=0, column=1, sticky='nsew')
        else:
            self.page1.grid_forget()
