#For redirected download links
#Prints final url address or downloads the file
#Base code obtained from: https://stackoverflow.com/questions/44628699/how-to-download-a-file-from-a-url-which-redirects
import requests

#url = 'https://readthedocs.org/projects/django/downloads/pdf/latest/' (Hard-codes url. Comment out next 2 lines
# and uncomment this if you don't want to enter url by user input)

url = input("Input redirect url: ")
r = requests.get(url, allow_redirects=True)  # to get content after redirection

#get only final redirected URL
# r = requests.head(url, allow_redirects=True)

#don't understand this line, program works without it.
# pdf_url = r.url # 'https://media.readthedocs.org/pdf/django/latest/django.pdf'

print("final url is: " + (r.url))
#The following lines will download the file which the url goes to.
#change 'file_name.pdf' to whatever the file name is that you are downloading
# with open('file_name.pdf', 'wb') as f:
#     f.write(r.content)
