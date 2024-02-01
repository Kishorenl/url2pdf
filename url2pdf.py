# libs
import os
from utils.readAsBatch import read_file_in_batches
from utils.pdfgenerator import PdfGenerator
from urllib.parse import urlsplit, urlunsplit

# function to strip the hostname for the url so that we can store the pages in directory structure 
def remove_hostname(url):
    # Parse the URL into its components
    url_components = urlsplit(url)

    # Create a new URL without the hostname
    new_url = urlunsplit(('', '', url_components.path, url_components.query, url_components.fragment))

    return new_url

# batch size for retrieving the urls from the file
batch_size = 50

# Read the file in batches
url_list = read_file_in_batches('./data.txt', batch_size)

# Iterate over each url in the list
for url in url_list:
    
    url_without_hostname = remove_hostname(url)    

    pdf_file = PdfGenerator([url]).main()
    folder_path = os.path.dirname(url_without_hostname)
    file_name = os.path.basename(url_without_hostname) 
    
    # if the url ends without a file name, would like to add that page as index.pdf
    if file_name is None or not file_name.strip():
        file_name = 'index'

    folder_path = "./pdfs/" +folder_path
    file_path = os.path.join(folder_path, file_name+'.pdf')
    
    print(url, file_path, sep=" --> ")

    # Check if the folder exists, and create it if not
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, "wb") as outfile:
        outfile.write(pdf_file[0].getbuffer())