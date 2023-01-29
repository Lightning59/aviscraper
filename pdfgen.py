import os
from fpdf import FPDF


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

pdf=FPDF()
for image in newlist:
    pdf.add_page()
    pdf.image(image,0,0)

pdf.output("results\\19280109.pdf","F")
