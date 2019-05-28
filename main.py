import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from flask import Flask, send_from_directory, request, jsonify

directory = 'files'
app = Flask(__name__, static_folder=directory)

def encryptFilePDF(file_name, password):
    pathFile = './files/' + file_name
    pdfFile = open(pathFile, 'rb')
    pdfReader = PdfFileReader(pdfFile)
    pdfWriter = PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    pdfWriter.encrypt(password)

    resultPdf = open('./files/' + 'encrypted_file.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    os.remove(pathFile)

    return resultPdf

@app.route("/encrypt-pdf", methods=['POST'])
def encryptFileRoute():
    if not 'file' in request.files:
        return jsonify({'error': 'no file'}), 400
    pdf_file = request.files.get('file')
    file_name = pdf_file.filename
    mimetype = pdf_file.content_type

    if not mimetype in 'application/pdf':
        return jsonify({'error': 'bad-type'})

    if not os.path.exists(directory):
        os.makedirs(directory)

    pdf_file.save(os.path.join(directory, file_name))

    if not 'password' in request.form:
        return jsonify({'error': 'key password invalid or empty'}), 400
    password = request.form.get('password')
    
    encryptFilePDF(file_name, password)

    return send_from_directory(directory=directory, filename='encrypted_file.pdf')
    
if __name__ == "__main__":
    app.run(debug=True)