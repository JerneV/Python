## 
# Made as a joke
# Jerne V. - 25/01/2019
##


from bs4 import BeautifulSoup
import sys, os
import requests, urllib.request
import re


# Get input
code = input("What is the /g/*** code? ")
# Compose nHentai URL
url = "https://nhentai.net/g/" + code + "/"

# Collect webpage using requests
response = requests.get(url)
# Parse webpage with BS4
soup = BeautifulSoup(response.content, "html.parser")

 
# Try to find total amount of pages using BS4 and some beautiful RegEx! 
temp_pages = soup.body.findAll(text=re.compile('pages$'))
# Returns a big matrix, we sort it using RegEx to a 1x1 matrix with only the numbers. Then we extract the exact number of pages 
pages = int(re.findall(r'\d+', str(temp_pages[0]))[0])

# Get some output
print("Trying to download " + str(pages) + " images!")

## Next up are the images, the URL for these are different than the main page.
# We this time we go to the first image link and parse it using BS4
soup2 = BeautifulSoup(requests.get("https://nhentai.net/g/" + code + "/1/").content, "html.parser")
# Using some more BS4 we find the image link
imageSource = str([x['src'] for x in soup2.findAll('img', {'class': 'fit-horizontal'})][0])
# The link we get ends on /1.jpg or something, we don't need that. Delete it with this (lazy method) 
length = len(imageSource)
imagePreLink = imageSource[:-5]

## Then we're ready for the download
# Loop through the pages and download the suckers
for x in range(1, pages+1):
    # We re-add the /pageNumber.jpg on the end
    imageLink = imagePreLink + str(x) + ".jpg"
    # Create a place to store it
    imageName = code + " Page " + str(x) + ".jpg"

    # Download the actual image using urllib 
    urllib.request.urlretrieve(imageLink, imageName)
    
# Last output, why not eh? 
print("Succesfully downloaded " + str(pages) + " images from: " + url)







