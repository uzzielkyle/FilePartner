from typing import Optional, Tuple, Union
from customtkinter import *
from components.sidebar import SideBar
from pdf_merger.index import BulkPdfMerger
import json
import os
import sys
import shutil
from appdirs import user_data_dir

basedir = os.path.dirname(__file__)


class App(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # Path to the icon file
        icon_path = self.resource_path("app/assets/icon/logo.ico")
        self.iconbitmap(icon_path)

        self.title('FilePartner')
        self.geometry('780x340')
        self.minsize(750, 330)

        self.config_path = self.get_config_path()
        with open(self.config_path) as config_file:
            config = json.load(config_file)
            appearance_mode = config["appearanceMode"]

        set_appearance_mode(appearance_mode)
        set_default_color_theme(self.resource_path(
            'app/assets/themes/metal.json'))

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.bulk_merger = BulkPdfMerger(master=self)

        self.sidebar = SideBar(master=self, page1=self.bulk_merger)
        self.sidebar.grid(row=0, column=0, sticky='nsw')

    @staticmethod
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


if __name__ == '__main__':
    app = App()
    app.mainloop()
