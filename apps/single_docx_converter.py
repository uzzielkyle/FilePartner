from typing import Tuple
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from utils.docx_to_pdf import DocxConverter
from threading import Thread


class SingleDocxConverter(CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = 'transparent', fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color,
                         border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.docx_converter = DocxConverter()

        self.label = CTkLabel(self, text='Individual Docx File Converter')
        self.label.grid(row=0, column=0)

        self.open_file_btn = CTkButton(
            self, text='Choose a file.', command=lambda: self.select_file())
        self.open_file_btn.grid(row=1, column=0)

    def select_file(self):
        filetypes = (
            ('Docx files', '*.docx'),
        )

        file_path = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        if file_path:
            dialog = CTkMessagebox(
                title='Selected File',
                message=file_path
            )
            directory, file_name = os.path.split(file_path)

            self.file_name_label = CTkLabel(self, text=file_name)
            self.file_name_label.grid(row=2, column=0)

            self.convert_btn = CTkButton(
                self, text='Convert', command=lambda: Thread(target=lambda: self.convert(file_path)).start())
            self.convert_btn.grid(row=3, column=0)

    def convert(self, file_path: str):
        self.docx_converter.single_conversion(file_path)


if __name__ == '__main__':
    app = SingleDocxConverter()
    app.mainloop()
