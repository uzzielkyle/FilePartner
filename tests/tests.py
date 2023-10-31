import sys; sys.path.append('../PDFMergeXpress')
import tempfile
import os
import unittest

from main import flatten_array, has_at_least_two_pdfs, get_num_pages
from PyPDF2 import PdfWriter

# python -m unittest discover --verbose tests
class TestFlattenArray(unittest.TestCase):
    def test_flatten_nested_list(self):
        nested_list = [1, [2, [3, 4], 5], 6]
        flattened = flatten_array(nested_list)
        expected = [1, 2, 3, 4, 5, 6]
        
        # Using different assertion methods
        self.assertEqual(flattened, expected, "Nested list flattening failed")
        self.assertListEqual(flattened, expected, "Nested list flattening failed")
        self.assertSequenceEqual(flattened, expected, "Nested list flattening failed")

    def test_flatten_empty_list(self):
        empty_list = []
        flattened = flatten_array(empty_list)
        expected = []
        
        # Using different assertion methods
        self.assertEqual(flattened, expected, "Empty list not handled correctly")
        self.assertListEqual(flattened, expected, "Empty list not handled correctly")
        self.assertSequenceEqual(flattened, expected, "Empty list not handled correctly")

    def test_flatten_single_element_list(self):
        single_element_list = [1]
        flattened = flatten_array(single_element_list)
        expected = [1]
        
        # Using different assertion methods
        self.assertEqual(flattened, expected, "Single element list not handled correctly")
        self.assertListEqual(flattened, expected, "Single element list not handled correctly")
        self.assertSequenceEqual(flattened, expected, "Single element list not handled correctly")


class TestHasAtLeastTwoPDFs(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory that contains two PDF files and one txt file
        self.test_dir = tempfile.mkdtemp()
        self.pdf_file1 = os.path.join(self.test_dir, "file1.pdf")
        self.pdf_file2 = os.path.join(self.test_dir, "file2.pdf")
        self.non_pdf_file = os.path.join(self.test_dir, "file.txt")

        with open(self.pdf_file1, "w") as f:
            f.write("This is a PDF content")

        with open(self.pdf_file2, "w") as f:
            f.write("This is another PDF content")

        with open(self.non_pdf_file, "w") as f:
            f.write("This is a text content")

    def tearDown(self):
        # make sure to clean up after each test
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_has_two_pdfs(self):
        # since initial setUp() has two PDF files, this should be true
        self.assertTrue(has_at_least_two_pdfs(self.test_dir), "Expected at least two PDF files")

    def test_has_one_pdf(self):
        # remove 1 pdf file, this should be false now since there is only one PDF file
        os.remove(self.pdf_file2)
        self.assertFalse(has_at_least_two_pdfs(self.test_dir), "Expected less than two PDF files")

    def test_no_pdfs(self):
        # remove 2 pdf files, this should be false now since there is no PDF file
        os.remove(self.pdf_file1)
        os.remove(self.pdf_file2)
        self.assertFalse(has_at_least_two_pdfs(self.test_dir), "Expected no PDF files")
    

class TestGetNumPages(unittest.TestCase):
    def setUp(self):
        # create a temporary directory that contains 2 pdfs
        self.test_dir = tempfile.mkdtemp()
        self.pdf_file1 = os.path.join(self.test_dir, "file1.pdf")
        self.pdf_file2 = os.path.join(self.test_dir, "file2.pdf")

        # create 3 pages to the first pdf and 4 pages to the second pdf
        self._create_pdf(self.pdf_file1, 3)
        self._create_pdf(self.pdf_file2, 4)

    def _create_pdf(self, file_path, num_pages):
        pdf = PdfWriter()
        for i in range(num_pages):
            # create a 612 x 792 page (standard letter size)
            pdf.add_blank_page(612, 792) 

        with open(file_path, "wb") as f:
            pdf.write(f)

    def tearDown(self):
        # make sure to clean up after each test
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_get_num_pages_with_two_pdfs(self):
        pdfs = [self.pdf_file1, self.pdf_file2]
        total_pages = get_num_pages(pdfs)
        self.assertEqual(total_pages, 7, "Expected 7 total pages")

    def test_get_num_pages_with_one_pdf(self):
        pdfs = [self.pdf_file1]
        total_pages = get_num_pages(pdfs)
        self.assertEqual(total_pages, 3, "Expected 3 total pages")

    def test_get_num_pages_with_no_pdfs(self):
        pdfs = []
        total_pages = get_num_pages(pdfs)
        self.assertEqual(total_pages, 0, "Expected 0 total pages")

    def test_get_num_pages_with_added_pages(self):
        pdfs = [self.pdf_file1]
        total_pages = get_num_pages(pdfs)
        self.assertEqual(total_pages, 3, "Expected 3 total pages")
        # now add the second pdf
        pdfs.append(self.pdf_file2)
        total_pages = get_num_pages(pdfs)
        self.assertEqual(total_pages, 7, "Expected 7 total pages")
