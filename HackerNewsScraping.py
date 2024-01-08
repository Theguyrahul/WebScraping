# Imports
import requests
from bs4 import BeautifulSoup

# Getting Hacker News HTML 
res = requests.get("https://news.ycombinator.com/").text

# Creating Soup
soup = BeautifulSoup(res,"html.parser")

# Story attributes 
titles = soup.find_all("span", class_= "titleline")
points = soup.find_all("span", class_= "score")
ages = soup.find_all("span", class_= "age")

# A for loop to iterate through news
for i in range(0,len(titles)-1):
    print(titles[i].text)
    print(ages[i].a.text)
    print(points[i].text)
    link = titles[i].a["href"]
    print(f"Go for more details: {link}")
    print("*"*100)

