from typing import Optional, Tuple, Union
from customtkinter import *
import json
import shutil
from appdirs import user_data_dir


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

        self.config_path = self.get_config_path()

        with open(self.resource_path("app/config.json")) as config:
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
            self.update_appearance_mode(choice)
            with open(self.resource_path("app/config.json")) as config:
                new_config = json.load(config)
                new_config["appearanceMode"] = choice

            with open(self.resource_path("app/config.json"), mode="w") as config:
                config.write(json.dumps(new_config))

        except ValueError:
            return

    @staticmethod
    # Function to get the correct path to the resource
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def get_config_path(self):
        """ Ensure the config file is in a writable location and return its path. """
        user_data_path = user_data_dir("FilePartner", "UzzielKyleYnciong")
        os.makedirs(user_data_path, exist_ok=True)
        config_path = os.path.join(user_data_path, "config.json")

        if not os.path.exists(config_path):
            shutil.copyfile(self.resource_path("app/config.json"), config_path)

        return config_path

    def save_config(self, config):
        """ Save the given config to the writable config path. """
        with open(self.config_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    def update_appearance_mode(self, mode):
        """ Update appearance mode in the config file and apply it. """
        with open(self.config_path) as config_file:
            config = json.load(config_file)
        config["appearanceMode"] = mode
        self.save_config(config)
        set_appearance_mode(mode)
