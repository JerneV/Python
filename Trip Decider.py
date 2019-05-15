from bs4 import BeautifulSoup as BS
import requests
import re, random
import sys, os, subprocess

response = requests.get("https://www.brusselsairlines.com/nl-nl/bestemmingen/Default.aspx")
soup = BS(response.content, "html.parser")

col_first = soup.findAll("div", { "class" : "col first"})

r = re.compile(">[\S]*?<\/a>")

p = re.findall(r, str(col_first))

lists = []

for x in p:
    x = x.strip(">")
    lists.append(str(x[:-3]))

choice = random.choice(lists)
print("Bestemming is: " + str(choice))
url = "https://en.wikipedia.org/wiki/" + str(choice)


## From https://stackoverflow.com/a/4217323/7625009 
if sys.platform=='win32':
    os.startfile(url)
elif sys.platform=='darwin':
    subprocess.Popen(['open', url])
else:
    try:
        subprocess.Popen(['xdg-open', url])
    except OSError:
        print('Please open a browser on: '+url)
