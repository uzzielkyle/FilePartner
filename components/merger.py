# Looks like this component would not work hehe
from typing import Optional, Tuple, Union
from customtkinter import *
from utils.pdf_logics import *
from CTkMessagebox import CTkMessagebox

class Merger(CTkFrame):
    WIDTH: int = 600
    HEIGHT: int = 50
    
    def __init__(self, *args, 
                get_path_func,
                clear_search_func,
                 bg_color: str | Tuple[str, str] = 'transparent', 
                 fg_color: str | Tuple[str, str] = 'transparent', 
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, bg_color=bg_color, fg_color=fg_color, corner_radius=corner_radius, **kwargs)
        
        self.get_path = get_path_func
        self.clear_search = clear_search_func
        
        self.treeview_connection = None
        
        self.grid_columnconfigure((0, 1), weight=1)
        
        # Will figure out kung paano talaga magamit ito
        self.progress_bar = CTkProgressBar(self, orientation='horizontal', width=self.WIDTH - 120)
        self.progress_bar.grid(row=0, column=0, columnspan=2, padx=(10, 0), pady=(0, 5), sticky='ew')
        self.progress_bar.configure(mode='indeterminate')
        
        self.merge_btn = CTkButton(self, text='Merge', width=90, corner_radius=corner_radius, command=self.merge)
        self.merge_btn.grid(row=0, column=2, padx=(20, 0), pady=(0, 5), sticky='ew')
               
    def merge(self) -> None:
        folder_path = self.get_path()
                
        if not folder_path: 
            self.blank_searchbar_message = CTkMessagebox(fg_color='whitesmoke', bg_color='whitesmoke', title='Blank Entry' ,message='Please input a folder path.', icon='warning', justify='center',font=('Arial', 11), option_focus='option_1')
            return
             
        self.clear_search()
        self.clear_treeview()
        self.working_state()
        
        if not folder_path.endswith(os.path.sep):
            folder_path += os.path.sep
                        
        roots_not_empty = scan_folders(folder_path=folder_path)
               
        if roots_not_empty:  
            folders, outputs = recursive_merging(main_path=folder_path, dirs=roots_not_empty)
            self.display_folders(folders)
            self.display_pdfs(outputs)
            
        else: 
            self.no_files_message = CTkMessagebox(fg_color='whitesmoke', bg_color='whitesmoke', title='No PDFs found' ,message='No PDF file inside the directory.', icon='warning', justify='center',font=('Arial', 11), option_focus='option_1')
            
        self.idle_state()
        
    def idle_state(self):
        self.progress_bar.stop()
        self.merge_btn.configure(state='normal')
        
    def working_state(self):
        self.progress_bar.start()
        self.merge_btn.configure(state='disabled')
        
    def set_treeview_connection(self, clear,  display_folders, display_pdfs):
        self.clear_treeview = clear
        self.display_folders = display_folders
        self.display_pdfs = display_pdfs
            

class Tester(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        
        self.Merger = Merger(master=self, width=750)
        self.Merger.grid(row=0, column=0, padx=10, pady=10)
        
        
def main():
    app = Tester()
    
    app.mainloop()
    

if __name__ == '__main__':
    main()
    