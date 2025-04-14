import os
import glob
import re
from shutil import copy
from PIL import Image
from pdf2image import convert_from_path

# Constants
LIST_DOCUMENT_TYPES = ["PDL", "PK", "BA", "SIP", "SLO", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
LIST_SPJBTL = ["SPJBTL 1", "SPJBTL 2", "SPJBTL 3", "SPJBTL 4", "SPJBTL 5"]
POPPLER_PATH = r"D:\Project\poppler\poppler-24.08.0\Library\bin"
JPEG_OPTIONS = {'optimize': True, 'progressive': False, 'quality': 50}
awal=1
akhir=410

# Variables
processed_files = []
new_filenames = []
original_filenames = []
# nopel_data = []

# Function to get sorted PDF files in a directory
def get_sorted_pdfs(directory):
    pdf_files = glob.glob(os.path.join(directory, "AIL*[0-9]*.pdf"))
    return sorted(pdf_files, key=lambda s: int(re.search(r'(?=.)\d+(?<=.)', os.path.basename(s)).group()))

# Process directories
# for folder in [d for d in os.listdir() if os.path.isdir(d)]:
#     print(f"Processing folder: {folder}")
    
# folder_path = os.path.basename(folder)
# processed_files.append(folder_path)
pdf_files = get_sorted_pdfs(os.getcwd())
print(pdf_files[awal-1:akhir])

# for index, pdf_path in enumerate(pdf_files, start=1):
#     pdf_filename = os.path.basename(pdf_path)
#     new_filename = f"{numbering}-{index}.pdf"
    
#     original_filenames.append(pdf_path)
#     new_filenames.append(new_filename)
#     numbering += 1

# nopel_data.append(f"{numbering},{folder_path}")

# Convert PDFs to images and save them
for numbering, path in enumerate(pdf_files[awal-1:akhir], start=0):
    try:
        images = convert_from_path(path, poppler_path=POPPLER_PATH, fmt="jpeg", jpegopt=JPEG_OPTIONS)
        doc_number=1
        number=numbering+awal
        for img in images:
            new_path = f"{number}-{doc_number}.pdf"
            while os.path.exists(new_path):
                # number, doc = new_path.split('-')
                doc_number = doc_number + 1
                new_path = f"{number}-{doc_number}.pdf"
            
            # print(new_path)
            
            img.save(new_path, dpi=(300, 300))
    except (OSError, Image.UnidentifiedImageError) as e:
        print(f"Error processing file {path}: {e}. Skipping...")
    print(path+"splitted")

# Save nopel data to a CSV
# with open("nopel.csv", "w") as nopel_file:
#     for entry in nopel_data:
#         nopel_file.write(f"{entry}\n")

print("Processing complete!")
