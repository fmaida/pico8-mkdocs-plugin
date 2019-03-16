import re
from mkdocs.plugins import BasePlugin


class Pico8(BasePlugin):

    snippet  = "<div style='width:100%'>"
    snippet += "<iframe src='https://www.lexaloffle.com/bbs/widget.php?pid=46052'"
    snippet += " allowfullscreen width='621' height='513'"
    snippet += " style='border:none; overflow:hidden; display:block; margin-left:auto; margin-right:auto'>"
    snippet += "</iframe></div>"
    
    def on_page_markdown(self, markdown, **kwargs):

        # Now we'll search on the text each occurrence
        # of the tag {{dolly}} and we'll replace it with some
        # random lyrics.
        # This class method (on_page_markdown) will be called each
        # time mkdocs needs to start processing a page before
        # rendering it in HTML.

        # For sake of simplicity, we won't use regular
        # expressions in this example to search and replace text.

        markdown = markdown.replace("{{pico8}}", snippet)

        # However if you prefer to use regex, please comment the
        # previous line of code and uncomment the following ones:

        # markdown = re.sub(r"\{\{(\s)*dolly(\s)*\}\}",
        #                   random_lyrics(),
        #                   markdown,
        #                   flags=re.IGNORECASE)

        return markdown
