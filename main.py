from PyPDF2 import PdfFileReader, PdfFileWriter
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='files')

def encryptFilePDF():
    pdfFile = open('./files/sample.pdf', 'rb')
    pdfReader = PdfFileReader(pdfFile)
    pdfWriter = PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    pdfWriter.encrypt('20scoops')

    resultPdf = open('./files/encrypted_output.pdf', 'wb')

    pdfWriter.write(resultPdf)
    resultPdf.close()
    return resultPdf

@app.route("/encrypt-pdf")
def home():
    encryptFilePDF()
    return send_from_directory(directory='files', filename='encrypted_output.pdf')
    
if __name__ == "__main__":
    app.run(debug=True)