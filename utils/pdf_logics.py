from PyPDF2 import PdfMerger
import os


#  Credits to Ma'am Tine (https://github.com/kjvmartinez) for this function
def merge_pdf(pdfs: list[str], filename: str):
    merger = PdfMerger()
    
    for pdf_file in pdfs:
        merger.append(pdf_file)
        
    merger.write(filename)
    merger.close()
    

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
