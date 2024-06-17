from typing import Optional, Tuple, Union
from customtkinter import *
import json


class AppearanceModeToggler(CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 100,
                 bg_color: str | Tuple[str, str] = 'transparent',
                 fg_color: str | Tuple[str, str] = 'transparent',
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, width=width, height=height, bg_color=bg_color,
                         fg_color=fg_color, corner_radius=corner_radius, **kwargs)

        self.grid_rowconfigure(1, weight=1)

        self.modes_list = ['System', 'Dark', 'Light']

        with open("app/config.json") as config:
            config = json.load(config)
            appearance_mode = config["appearanceMode"]

        self.current_mode_var = StringVar(value=appearance_mode)

        self.widget_label = CTkLabel(
            self, text='Appearance Mode', anchor='center')
        self.widget_label.grid(row=0, column=0, padx=15, pady=0)

        self.dropdown_menu = CTkOptionMenu(
            self, values=self.modes_list, variable=self.current_mode_var, command=self.set)
        self.dropdown_menu.grid(row=1, column=0, padx=10,
                                pady=(0, 5), sticky='ew')

    def set(self, choice) -> None:
        try:
            set_appearance_mode(choice)
            with open("app/config.json") as config:
                new_config = json.load(config)
                new_config["appearanceMode"] = choice

            with open("app/config.json", mode="w") as config:
                config.write(json.dumps(new_config))

        except ValueError:
            return
