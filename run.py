# imports include beautifulsoup
import requests
from bs4 import BeautifulSoup
#from os import path, access
import os.path
from urllib.parse import urljoin
from pathlib import Path
import subprocess

BASE_URL = "https://www.svtplay.se"

# ask for url or path
print("Please provide...")
print("full url from svtplay (full season)")
source = input("OR full path to last scraped html (empty will attempt to parse './last.htm'): ")

# determine what input provided
if not source.startswith("http"):
    # was path
    if source == "" and os.path.isfile("./last.htm"):
        source = "./last.htm"
    elif not os.path.isfile(source):
        print("Your source was deemed a file, but does not exist (or could not be read).")
        exit()

    with open(source, "r") as file:
        data = file.read()

else:
    # was url (so scraping)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(source, headers=headers)
    if response.status_code != 200:
        print(f"Unable to fetch page at: '{source}'. Status code: {response.status_code}.")
        exit()

    # save to file
    with open("last.htm", "w", encoding="utf-8") as file:
        file.write(response.text)

    data = response.text

# parse data
soup = BeautifulSoup(data, 'html.parser')
#print(soup.prettify())

# find unique links with specific end
unique_links = set()
for link in soup.find_all("a", href=True):
    href = link.get("href")
    if href.endswith("?video=visa"):
        href = href.replace("?video=visa", "")
        full_url = urljoin(BASE_URL, href)
        unique_links.add(full_url)

# write links to file
if len(unique_links) < 1:
    print("No (proper) links found, stop execution.")
    exit()

with open("queue.txt", "w", encoding="utf-8") as file:
    for link in unique_links:
        file.write(f"{link}\n")
        #print(link)

# output suggested folder-name and amount of episodes
#print(soup.title.string)
title = soup.title.string.split("|")[0].strip()
print(f"Found {len(unique_links)} episodes. Suggested folder name '{title}'")

# ask for target directory
ask_for_path = input("Where do you want to store episodes?: ")
pwd = os.path.dirname(os.path.realpath(__file__))

if ask_for_path == ".":
    target_path = os.path.join(pwd, title)
else:
    target_path = os.path.join(ask_for_path, title)

# create directory (fails upon existing, todo: REMOVE IF PROCESS FAILS)
Path(target_path).mkdir(parents=True)

# run yt-dlp with queue
queue_file = os.path.join(pwd,"queue.txt")
result = subprocess.run(["yt-dlp", "-a", queue_file, "-P", target_path])
print(result.stdout)