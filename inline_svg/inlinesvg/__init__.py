# __init__.py
# from .plugin import InlineSvgPlugin

import sys
from scour import scour
import xml.etree.ElementTree as ET

def optimize_svg(fname):
    # remove DOCTYPE, comment...etc by parse and reverse SVG file.
    svgTree = ET.parse(fname).getroot()
    svgString = ET.tostring(svgTree)

    # optimize SVG string to single line string with scour(http://www.codedread.com/scour/).
    options=type("args", (object,), {
        "strip_comments": True,
        "strip_xml_prolog": True,
        "simple_colors": False,
        "style_to_xml": False,
        "group_collapse": False,
        "newlines": False,
    })
    return scour.scourString(svgString, options=options)

def main() -> None:
    fname = sys.argv[1] if len(sys.argv) > 1 else ""
    print(optimize_svg(fname))