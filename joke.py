import pycurl
import StringIO
import textwrap
import re
import string


def get_quote():
    global maxPage
    c = pycurl.Curl()
# Get text version of a quote, we are getting one-liners, but other source types
# are available such as fortune and famousquotes, see iheartquotes.com    
    c.setopt(c.URL, 'http://iheartquotes.com/api/v1/random?source=oneliners')
    contents = StringIO.StringIO()
    c.setopt(c.WRITEFUNCTION, contents.write)
    c.perform()
    lineout = contents.getvalue()
    lineout = re.sub(r'&quot','"',lineout)
# Remove the last section of the data...refers to the source webpage
    lineout = re.sub(r'\[oneliners.*','',lineout)
    formatted_text = textwrap.fill(lineout,width=16)
    splitted = string.split(formatted_text, '\n')
    if bool(len(splitted) % 2):
      # odd number so add a line to make it even or we would page off end
      splitted.append("----")
    maxPage = len(splitted)
    return splitted

x=get_quote()
print(x)