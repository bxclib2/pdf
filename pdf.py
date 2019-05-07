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



    

