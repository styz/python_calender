# %%
import calendar
from IPython.display import display, HTML
import locale

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

cal = calendar.HTMLCalendar(calendar.SUNDAY)
calHtml = cal.formatyearpage(theyear=2021, width=4, encoding='UTF-8', css='cal.css')

css = '''
th, td {
    text-align: center;
    vertical-align: top;
    font-size: 1em;
}

table.month {
    border-collapse: collapse;
    border: 1px solid black;
    margin: 0.25em;
}

table.month th, table.month td {
    border: 1px solid black;
}

table.month td.sat {
    background-color: rgba(0, 0, 255, 0.5);
}

table.month td.sun {
    background-color: rgba(255, 0, 0, 0.5);
    background-image: url('data:image/svg+xml;charset=utf8,%3Csvg%20width%3D%22100%22%20height%3D%22100%22%20%20viewBox%3D%220%200%20200%20200%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%20%20%20%20%3Ccircle%20cx%3D%22100%22%20cy%3D%22100%22%20r%3D%2290%22%20%20stroke%3D%22green%22%20stroke-width%3D%2210%22%20stroke-opacity%3D%220.7%22%20fill%3D%22none%22%20%3E%3C%2Fcircle%3E%0A%3C%2Fsvg%3E%0A');
    background-size: cover;
    background-position: center;
}
'''

with open('buf/cal.css', 'w', encoding='UTF-8') as f:
    f.write(css)


display(HTML(calHtml.decode()))

# %%

import imgkit

with open('buf/cal.html', 'w', encoding='UTF-8') as f:
    f.write(calHtml.decode())

options={
    'enable-local-file-access': None,
    'disable-smart-width': None,
    'width': 800*6,
    'zoom': 6,
}
imgkit.from_string(calHtml.decode(), './buf/cal.png', options=options, css='./buf/cal.css')

# %%
from PIL import Image, ImageChops

def trim(image, offset):
    im = image.convert('RGB')
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        bbox2 = (bbox[0] - offset, bbox[1] - offset, bbox[2] + offset, bbox[3] + offset)
        return im.crop(bbox2)

im = Image.open('buf/cal.png')
im = trim(im, 10)
im.save('target/cal.png')
im.close()

# %%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

im = Image.open('out/cal.png')
imList = np.asarray(im)
plt.imshow(imList)
plt.axis("off")
plt.show()

# %%
