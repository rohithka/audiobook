# import pyttsx3
# import PyPDF2
#
# book = open('LegendofSuheldev.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)
# speaker = pyttsx3.init()
# for num in range(18, pages):
#     page = pdfReader.getPage(18)
#     text = page.extractText(page)
#     speaker.say(text)
#     speaker.runAndWait()

import pyttsx3
import pdfplumber
import PyPDF2

file = 'ponniyin selvan book1.pdf'

pdffileobj = open(file, 'rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)

pages = pdfreader.numPages

with pdfplumber.open(file) as pdf:
    for i in range(10, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)

        speaker = pyttsx3.init()
        voices = speaker.getProperty('voices')  # getting details of current voice
        speaker.setProperty('voice', voices[1].id)  # changing index, changes voices. o for male
        # speaker.setProperty('voice', voices[0].id)
        rate = speaker.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        speaker.setProperty('rate', 175)
        speaker.say(text)

        speaker.runAndWait()
