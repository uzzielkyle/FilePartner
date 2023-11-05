# Needs to clean this up
from PyPDF2 import PdfMerger, PdfFileReader
import os
import glob


def get_pdf_page(file_path: str) -> int:
    """Returns the number of pages of a given PDF file

    Args:
        file_path (str): path to file

    Returns:
        int: total number of pages
    """
    file = open(file_path, 'rb')
    
    # store data in pdfReader 
    pdf_reader = PdfFileReader(file) 
    
    # count number of pages 
    total_pages = len(pdf_reader.pages) 
    
    return  total_pages


def get_pdfs(root_dir: list) -> list:
    files = []
    for row_num, folder in enumerate(root_dir):
        str_path = os.path.join(folder, '*.pdf') # Use os.path.join for paths
        pdfs = [path.replace("\\","/") for path in glob.glob(str_path, recursive=True) if os.path.isfile(path)] # also check if the glob is a pdf file, it may sometimes be a folder that ends with .pdf
        # .replace("\\","/") for 'slash' consistency... https://stackoverflow.com/a/18776536, tnx
        files.append(pdfs)
        

#  Credits to Ma'am Tine (https://github.com/kjvmartinez) for this function
def merge_pdf(pdfs: list[str], filename: str):
        if len(pdfs) == 1:  # If there's only one PDF file, skip merging
            return 0

        merger = PdfMerger()
        for pdf_file in pdfs:
            merger.append(pdf_file)
            
            # merger.append(i)
        merger.write(filename)
        num_pages = len(merger.pages)
        merger.close()
        return num_pages
    

# Credits to jbarry302 (https://github.com/jbarry302) for all the functions below
def get_num_pages(pdfs: list) -> int:
    """
    Returns the total number of pages in a list of PDF files combined.
    Args:
        pdfs (list): A list of PDF file paths located in a subdirectory folder.
    Returns:
        int: The total number of pages in all the PDF files combined.
    """
    merger = PdfMerger()
    
    for pdf_file in pdfs:
        merger.append(pdf_file)

    num_pages = len(merger.pages)
    
    merger.close()
    
    return num_pages


def flatten_array(arr: list) -> list:
    """
    Recursively flattens a nested list into a single list.
    
    Args:
        arr (list): A nested list to be flattened.
    
    Returns:
        list: A flattened list.
    
    Example:
    >>> flatten_array([1, [2, [3, 4], 5], 6])
    [1, 2, 3, 4, 5, 6]
    """
    flattened_list = []
    
    for element in arr:
        if isinstance(element, list):
            flattened_list.extend(flatten_array(element))
        else:
            flattened_list.append(element)
            
    return flattened_list


def has_at_least_two_pdfs(folder_path: str) -> bool:
    """
    Checks if a folder contains at least two PDF files.
    Args:
        folder_path (str): The path to the folder to check.
    Returns:
        bool: True if the folder contains at least two PDF files, False otherwise.
    """
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                count += 1
                if count >= 2:
                    return True
    return False


def merge_files(main_path: str, root_dir: list) -> None:
    files = []

    for row_num, folder in enumerate(root_dir):
        str_path = os.path.join(folder, '*.pdf') # Use os.path.join for paths
        pdfs = [path.replace("\\","/") for path in glob.glob(str_path, recursive=True) if os.path.isfile(path)] # also check if the glob is a pdf file, it may sometimes be a folder that ends with .pdf
        # .replace("\\","/") for 'slash' consistency... https://stackoverflow.com/a/18776536, tnx
        files = files + pdfs
        number_of_pages = get_num_pages(pdfs)

    files = flatten_array(files)
    total_pages = get_num_pages(files)
    # by default, save the output to the first folder
    output_path = os.path.join(root_dir[0], 'output.pdf')
    merge_pdf(files, output_path)
    

def scan_folders(folder_path: str) -> list:
    list_roots = []

    for (root, dirs, files) in os.walk(folder_path, topdown=True):
        if any(f.endswith('.pdf') for f in files):
            list_roots.append(root)

    return list_roots


# This ugly function is made by me
def recursive_merging(main_path: str, dirs: list) -> tuple[list]:
    folders = []
    outputs = []
    
    for folder in dirs:
        str_path = os.path.join(folder, '*.pdf') # Use os.path.join for paths
        pdfs = [path.replace("\\","/") for path in glob.glob(str_path, recursive=True) if os.path.isfile(path) and not os.path.basename(path).startswith('output')]        
        
        number_of_pages = merge_pdf(pdfs, os.path.join(folder, 'output.pdf'))
    
        if number_of_pages == 0: continue
        
        folders.append(folder.replace(main_path, './'))
        outputs.append(('output.pdf', number_of_pages))
        
    return folders, outputs