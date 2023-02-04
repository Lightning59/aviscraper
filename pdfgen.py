import os
from fpdf.fpdf import FPDF
from PIL import Image


def writepdffromjpegs(pdfname: str, jpegfolder: str) -> None:
    """
    Requires images in a folder jpegtemp in the current working directory
    :param pdfname: name of the pdf file to output(without extension - .pdf will be added automatically)
    :param jpegfolder: string for directory of a bunch of jpegs numbered. 1.jpeg to xxx.jpeg
    :return: Returns nothing - Creates a results folder in pwd if none already exists and outputs a pdf named based on
    the input string
    """

    try:
        os.mkdir("results")
    except FileExistsError:
        pass

    imagelist = os.listdir(jpegfolder)

    newlist = sorted(imagelist, key=lambda x: int(x.split('.')[0]))

    for index, item in enumerate(newlist):
        newlist[index] = os.path.join(jpegfolder, item)

    pdf = FPDF(unit="pt")
    for image in newlist:
        im = Image.open(image)
        width, height = im.size
        im.close()
        pdf.add_page(format=(width, height))
        pdf.image(image, 0, 0)

    try:
        pdf.output("results\\" + pdfname + ".pdf")
    except Exception as e:
        print("error writing pdf")
        print(e)


if __name__ == "__main__":
    writepdffromjpegs("19280312", "jpegtemp")
