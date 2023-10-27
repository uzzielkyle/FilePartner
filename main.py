# Disclaimer: The way I wrote this code was to somehow make it 'work'... I had no prior experience nor knowledge in app/software development. Feel free to give constructive feedbacks :)
from PyPDF2 import PdfMerger
import glob
import os
from PyPDF2 import PdfMerger
from customtkinter import *

set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("dark-blue")

EDGY = {'corner_radius': 0}  # To remove round corners


'''
    FUNCTIONS   
'''
def toggle_appearance() -> None:
    current = get_appearance_mode()

    if current == "Light":
        set_appearance_mode("Dark")
        return
    
    set_appearance_mode("Light")


def merge_pdf(files: list[str], filename: str) -> int:
    if len(files) == 1:  # If there's only one PDF file, skip merging
        return 0

    merger = PdfMerger()
    for pdf_file in files:
        merger.append(pdf_file)
        
    merger.write(filename)
    num_pages = len(merger.pages)
    merger.close()
    return num_pages


def display_no_path(master) -> None:
    lbl_no_path = CTkLabel(master=master, text='No path provided.')
    lbl_no_path.grid(row=0, column=0, padx=5, pady=(5, 0), sticky='w')


def display_path_pages(master, folder: str, total_pages: int, count: int) -> None:
    lbl_path = CTkLabel(master=master, text=f"📁 {folder}")
    lbl_pages = CTkLabel(master=master, text=f"=> {total_pages} pages")

    lbl_path.grid(row=count, column=0, padx=(5, 15), pady=(5, 0), sticky='w')
    lbl_pages.grid(row=count, column=1, sticky='w')
    

def display_no_files(master, count: int) -> None:
    lbl_no_files = CTkLabel(master=master, text='No files to merge...')
    lbl_no_files.grid(row=count, column=0, padx=5,  pady=(5, 0), sticky='w')
    

'''
CLASSES
'''    
class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("PDFMergeXpress")
        self.geometry("900x420")
        self.resizable(False, False)


class MainFrame(CTkFrame):
    def __init__(self, container) -> None:
        super().__init__(container, **EDGY, fg_color='transparent')
        self.folder_path = ''
        self.pack()

        frm_search_folder = CTkFrame(self, **EDGY)
        frm_search_folder.pack(padx=10, pady=(30, 10))

        lbl_folder_path = CTkLabel(frm_search_folder, text="Folder Path", font=CTkFont(size=15, family="monospace"))
        lbl_folder_path.grid(row=0, column=0, padx=(10, 20))

        btn_toggle_appearance = CTkButton(frm_search_folder, text="Dark/Light", font=CTkFont(size=15, family="monospace"), width=80, **EDGY, command=lambda: toggle_appearance())
        btn_toggle_appearance.grid(row=1, column=0, padx=(10, 0), sticky='nw')

        ent_folder_path = CTkEntry(frm_search_folder, placeholder_text='Enter folder path or load folder', font=CTkFont(size=13, family="monospace"), width=480, **EDGY)
        ent_folder_path.grid(row=0, column=1, padx=(0, 20))

        btn_merge = CTkButton(frm_search_folder, text="Merge", font=CTkFont(size=15, family="monospace"), width=120, **EDGY, command=lambda: self.start_merge(scl_display))
        btn_merge.grid(row=1, column=1, sticky='n')

        btn_update = CTkButton(frm_search_folder, text="Update", font=CTkFont(size=15, family="monospace"), width=150, **EDGY, command=lambda: self.update_folder(ent_folder_path))
        btn_update.grid(row=0, column=2, padx=(0, 10), pady=(5, 5), sticky='e')

        btn_load_folder = CTkButton(frm_search_folder, text="Load", font=CTkFont(size=15, family="monospace"), width=150, **EDGY, command=lambda: self.load_folder(ent_folder_path))
        btn_load_folder.grid(row=1, column=2, padx=(0, 10), pady=(0, 5), sticky='e')

        frm_display_folders = CTkFrame(self, **EDGY, width=700)
        frm_display_folders.pack(pady=(0, 20))

        scl_display = CTkScrollableFrame(frm_display_folders, width=800, height=250, **EDGY)
        scl_display.pack()

        btn_clear = CTkButton(frm_display_folders, text="Clear All", font=CTkFont(size=15, family="monospace"), **EDGY, command=lambda: self.clear_display(scl_display))
        btn_clear.pack(fill="x")

    def update_folder(self, ent_folder_path) -> None:
        self.folder_path = ent_folder_path.get()
    
    def load_folder(self, ent_folder_path) -> None:
        self.folder_path = filedialog.askdirectory()

        if not self.folder_path:
            return

        if ent_folder_path:
            ent_folder_path.delete(1, END)
        
        ent_folder_path.insert(END, self.folder_path)

    @staticmethod
    def clear_display(scl_display) -> None:
        for element in scl_display.winfo_children():
            element.destroy()

    def start_merge(self, scl_display) -> None:
        self.clear_display(scl_display)

        if not self.folder_path: 
            display_no_path(master=scl_display)
            return

        if not self.folder_path.endswith(os.path.sep):
            self.folder_path += os.path.sep
            
        roots_not_empty = self.scan_folders()

        if roots_not_empty: 
            self.merge_files(root_dir=roots_not_empty, scroll_frame=scl_display)                
                         
    @staticmethod
    def merge_files(root_dir: list, scroll_frame) -> None:
        count = 0  # placing items in grid rows

        for folder in root_dir:
            str_path = os.path.join(folder, '*.pdf')  # Use os.path.join for paths

            files = glob.glob(str_path, recursive=True)

            number_of_pages = merge_pdf(files, os.path.join(folder, 'output.pdf'))

            if number_of_pages > 0:
                display_path_pages(master=scroll_frame, folder=folder, total_pages=number_of_pages, count=count)
                
                count += 1

        if count == 0:
            display_no_files(master=scroll_frame, count=count)    
                    
    def scan_folders(self):
        list_roots = []
        
        for (root, dirs, files) in os.walk(self.folder_path, topdown=True):
            if any(f.endswith('.pdf') for f in files):
                list_roots.append(root)
        
        return list_roots
    
    
def main() -> None:
    app = App()
    main = MainFrame(app)
    app.mainloop()


if __name__ == "__main__":
    main()
    