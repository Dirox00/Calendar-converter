
import re


def read_pdf(path):
    '''Function for getting all the information of the given PDF.'''
    content = []

    return content

def create_calendar():
    '''Creates calendar named "Horario" if it doesn't exist.'''
    pass

def convert(delete=False):
    '''Write (deleting all previous stuff) or adds (not deleting).'''
    global content

    if delete == True:
        # deletes existing content
        pass
    # add new stuuf
    pass


pdfName = input('Hole path of the PDF: ')
content = read_pdf(pdfName)

# add google credentials

mode = input('Do you want to delete the previous content? (y/n)?: ')
convert(mode == 'y')