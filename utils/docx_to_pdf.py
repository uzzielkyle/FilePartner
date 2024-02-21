import os
from docx2pdf import convert


class DocxConverter():
    def __init__(self) -> None:
        pass

    def single_conversion(self, file_path: str, output_name: str | None = None) -> int:
        """a function that converts a given docx file into a pdf file

        Args:
            file_path (str): the exact location of the docx file
            output_name (str | None, optional): desired output name if there's any. Defaults to None.

        Returns:
            int: 1 means successful, 0 means fail
        """
        try:
            if output_name:
                output_name = output_name + '.pdf'
                output_path = self.change_filename(file_path, output_name)
                convert(file_path, output_path)
            else:
                convert(file_path)

            return 1
        except:
            return 0

    def bulk_conversion(self, folder_path: str) -> int:
        """a function that converts all the docx files within a given folder

        Args:
            folder_path (str): the location of the folder

        Returns:
            int: 1 means successful, 0 means fail
        """
        try:
            convert(folder_path)

            return 1
        except:
            return 0

    @staticmethod
    def change_filename(filepath: str, new_filename: str) -> str:
        """
        Change the filename in a file path.

        Parameters:
        - filepath (str): The original file path.
        - new_filename (str): The new filename.

        Returns:
        - str: The updated file path with the new filename.
        """
        directory, old_filename = os.path.split(filepath)
        new_filepath = os.path.join(directory, new_filename)

        return new_filepath.replace("\\", "/")


if __name__ == '__main__':
    converter = DocxConverter()

    print(converter.single_conversion(
        'D:/coding-and-programming/python/projects/PDFMergeXpress/assets/demo_files/demo.docx', 'gawang_uzzi'))
    # print(converter.convert('D:/coding-and-programming/python/projects/PDFMergeXpress/utils/tests/demo.docx'))
