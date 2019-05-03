#! /usr/bin/python

# Import modules
import fileinput
import requests
import re
import os

# Set environment variables
ImageUrl="https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData"
JsonFile="cache.json"
JsonUrl="https://arc.msn.com/v3/Delivery/Placement?&pid=338387&fmt=json&cdm=1&ctry=US"
SearchPattern="(?<=imageFileData/).*?(?=\?ver)"
HttpHeader= {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'User-Agent': 'WindowsShellClient/9.0.40929.0 (Windows)'
}

# Download JSON file
Respose = requests.get(JsonUrl, headers=HttpHeader)
with open(JsonFile,'wb') as file:
    file.write(Respose.content)

# Remove back slashes
for line in fileinput.input(JsonFile, inplace=True):
    print(line.replace("\\", "")),

# Remove opening quotes
for line in fileinput.input(JsonFile, inplace=True):
    print(line.replace("\"{", "{")),

# Remove closing quotes
for line in fileinput.input(JsonFile, inplace=True):
    print(line.replace("}\"", "}")),

with open(JsonFile, 'r') as file:
    content = file.read()

# Get the hashes from links and download
hash = re.findall(SearchPattern, content, re.DOTALL)
for i in hash:
    j = ImageUrl + "/" + i
    FileName = i + ".jpg"
    print(j)
    Respose = requests.get(j, headers=HttpHeader)
    with open(FileName,'wb') as file:
        file.write(Respose.content)
    # Delete files less that 2 KB which are blank
    if os.path.getsize(FileName) < 2048:
        os.remove(FileName)
