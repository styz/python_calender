# plugin.py
import re
import os
import inlinesvg

from mkdocs.plugins import BasePlugin
from mkdocs import utils

def replace_with_file_content(basepath, match):
    filename = os.path.abspath(os.path.join(basepath, match.group(2) + '.svg'))
    utils.log.info("mkdocs-inline-svg: including SVG: {}".format(
        filename))

    # optimized_svg = ''.join([
    #     '<figure class="figure-svg">',
    #     inlinesvg.optimize_svg(filename),
    #     '</figure>'])
    return inlinesvg.optimize_svg(filename)

class InlineSvgPlugin(BasePlugin):
    def on_page_markdown(self, markdown, **kwargs):

        basepath = os.path.dirname(kwargs.get("page").file.abs_src_path)

        pattern = re.compile(r"!\[(.*?)\]\((.*?)\.svg\)", flags=re.IGNORECASE)

        markdown = re.sub(
            pattern, lambda match: replace_with_file_content(basepath, match), markdown
        )

        return markdown
