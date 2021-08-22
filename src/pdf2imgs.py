from pdf2image import convert_from_path, convert_from_bytes
import tempfile
import os
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def pdf2image2(pdfPath, imagePath, pageNum):
    # dpi = 72 -> 612 x 792
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(pdfPath, output_folder=path, dpi=500)
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        for image in images_from_path:
            image.save(imagePath + '/' + '%s.png' % images_from_path.index(image), 'PNG')
        # print(images_from_path)


pdfPath = "./NewYorkCourseMaterials.pdf"
imagePath = "./image/"
pdf2image2(pdfPath, imagePath, None)

