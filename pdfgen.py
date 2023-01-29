import os
from fpdf.fpdf import FPDF
from PIL import Image


try:
    os.mkdir("results")
except FileExistsError:
    pass

imagelist = os.listdir('jpegtemp')

print(imagelist)

newlist=sorted(imagelist, key=lambda x: int(x.split('.')[0]))

for index, item in enumerate(newlist):
    newlist[index]=os.path.join("jpegtemp",item)

print(newlist)

pdf=FPDF(unit="pt")
for image in newlist:
    im=Image.open(image)
    width,height = im.size
    pdf.add_page(format=(width,height))
    pdf.image(image,0,0)

pdf.output("results\\19280109.pdf")
