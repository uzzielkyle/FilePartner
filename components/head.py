# A combination of a progress bar, button, and my very own searchbar component.
from typing import Optional, Tuple, Union
from customtkinter import *
from components.searchbar import Searchbar
from utils.pdf_logics import *
import glob


class HeadComponent(CTkFrame):
    WIDTH: int = 100
    HEIGHT: int = 50
    
    def __init__(self, *args, 
                 bg_color: str | Tuple[str, str] = 'transparent', 
                 fg_color: str | Tuple[str, str] = 'whitesmoke', 
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, bg_color=bg_color, fg_color=fg_color, corner_radius=corner_radius, **kwargs)
        
        self.configure(border_width=5)
        
        self.grid_columnconfigure(0, weight=1)
        
        self.searchbar = Searchbar(master=self)
        self.searchbar.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 0))
        
        self.progress_bar = CTkProgressBar(self, orientation='horizontal', width=self.WIDTH - 100)
        self.progress_bar.grid(row=1, column=0, columnspan=2, padx=(10, 0), pady=10, sticky='ew')
        self.progress_bar.configure(mode='indeterminate')
        
        self.merge_btn = CTkButton(self, text='Merge', width=90, corner_radius=corner_radius, command=self.start_merge)
        self.merge_btn.grid(row=1, column=2, padx=10, pady=10, sticky='e')
        
    def merge(self) -> None:
        folder_path = self.searchbar.get()
        
        if not folder_path:
            return
        
        try: 
            print(f'Merging PDFs in {folder_path}')
            
        except:
            return
        
    def start_merge(self) -> None:
        folder_path = self.searchbar.get()
        self.searchbar.clear()
        
        self.progress_bar.start()
        self.merge_btn.configure(state='disabled')
        
        if not folder_path: 
            print('no path')
            return
        
        if not folder_path.endswith(os.path.sep):
            folder_path += os.path.sep
            
        folder_path.replace("\\","/")  # https://stackoverflow.com/a/18776536, tnx
            
        roots_not_empty = self.scan_folders(folder_path=folder_path)
        
        print(roots_not_empty)

        if roots_not_empty: 
            self.merge_files(main_path=folder_path, root_dir=roots_not_empty)
        
    def merge_files(self, main_path: str, root_dir: list) -> None:
        files = []

        for row_num, folder in enumerate(root_dir):
            str_path = os.path.join(folder, '*.pdf').replace("\\","/")  # Use os.path.join for paths
            pdfs = [path for path in glob.glob(str_path, recursive=True) if os.path.isfile(path)] # also check if the glob is a pdf file, it may sometimes be a folder that ends with .pdf
            files = files + pdfs
            number_of_pages = get_num_pages(pdfs)
            print(number_of_pages)

        files = flatten_array(files)
        total_pages = get_num_pages(files)
        print(files, total_pages)
        # by default, save the output to the first folder
        output_path = os.path.join(root_dir[0], 'output.pdf')
        merge_pdf(files, output_path)
        
        self.progress_bar.stop()
        self.merge_btn.configure(state='normal')

    def scan_folders(self, folder_path: str) -> list:
        list_roots = []

        for (root, dirs, files) in os.walk(folder_path, topdown=True):
            if any(f.endswith('.pdf') for f in files):
                list_roots.append(root.replace("\\","/"))

        return list_roots
        
        
class Tester(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
    
        self.head = HeadComponent(self)
        self.head.grid(row=0, column=0)
        
        
def main():
    app = Tester()
    app.mainloop()
    

if __name__ == '__main__':
    main()
    