import re
from mkdocs.plugins import BasePlugin


class Pico8(BasePlugin):

    # This snippet of code allows to show a pico-8
    # web player in a HTML page

    snippet = "<div style='width:100%'>"
    snippet += "<iframe src='https://www.lexaloffle.com/bbs/widget.php?pid={}'"
    snippet += " allowfullscreen width='621' height='513'"
    snippet += " style='border:none; overflow:hidden; display:block; margin-left:auto; margin-right:auto'>"
    snippet += "</iframe></div>"

    def on_page_markdown(self, markdown, **kwargs):
        """
        Takes an article written in markdown and looks for the
        presence of a tag written with this style:

        {{ pico-8: 12345 }}

        When the tag is found, it will be replaced with a
        snippet code that will show a pico-8 web player onscreen.

        :param markdown: Original article in markdown format
        :param kwargs: Other parameters (won't be used here)
        :return: Modified markdown
        """

        plugin_pattern = r"\{\{[\s]*pico[-]{0,1}8:[\s]*([0-9]*)[\s]*\}\}"
        plugin_code = re.findall(plugin_pattern, markdown)
        if plugin_code:
            game_code = plugin_code[0]
            markdown = re.sub(plugin_pattern,
                              self.snippet.format(game_code),
                              markdown,
                              flags=re.IGNORECASE)

        return markdown
