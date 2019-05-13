import os
import tempfile
import argparse

def pdf2img(path):
    from pdf2image import convert_from_path
    images = convert_from_path(path)
    path = os.path.splitext(path)[0] + "_%s.jpg"
    for i, img in enumerate(images):
        img.save(path%i, 'JPEG')

def pdf2txt(path):
    import pdftotext
    with open(path, "rb") as f:
          pdf = pdftotext.PDF(f)
    path = os.path.splitext(path)[0] + ".txt"
    with open(path, 'w') as f:
         f.write("\n\n".join(pdf))

def pdfmerge(path):
    from PyPDF2 import PdfFileMerger
    pdfs = path.split(",")
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))
    with open('result.pdf', 'wb') as fout:
        merger.write(fout)
def pdfsplit(path):
    import pyPdf
    path = path.split("--")
    s = path[1].split(":")
    for i in range(len(s)):
        if s[i] =="":
            s[i] = None
        else:
            s[i] = int(s[i])
    if len(s) == 1:
        s = slice(s[0], s[0]+1, None)
    elif len(s) == 2:
        s = slice(s[0], s[1], None)
    elif len(s) == 3:
        s = slice(s[0], s[1], s[2])
    else:
        print ("Cannot understand pages")    
    reader = pyPdf.PdfFileReader(file(path[0],"rb"))
    writer = pyPdf.PdfFileWriter()
    inputPages = [reader.getPage(i) for i in range(reader.getNumPages())]
    pages = inputPages[s]
    for page in pages:
        writer.addPage(page)
    name = (os.path.splitext(path[0])[0]+"-"+path[1]+".pdf").replace(":", "_")
    print (name)
    outputStream = file(name, "wb")
    writer.write(outputStream)

parser = argparse.ArgumentParser(description='pdf_reader')
parser.add_argument('name', type=str, help='Input file dir')
parser.add_argument('a', type=str, help='action')

args = parser.parse_args()
if args.a == "pdf2img":
    pdf2img(args.name)
if args.a == "pdf2txt":
    pdf2txt(args.name)
if args.a == "merge":
    pdfmerge(args.name)
if args.a == "split":
    pdfsplit(args.name)



    

