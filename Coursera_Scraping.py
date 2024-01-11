# Imports
import requests
from bs4 import BeautifulSoup

# Getting User Input
keywords = str(input("Enter keywords to search in Coursera..."))


try:
    res = requests.get(f"https://www.coursera.org/search?query={keywords}&").text
  
    soup = BeautifulSoup(res,"lxml")
    
    titles = soup.find_all("h3",class_ = "cds-119 cds-CommonCard-title css-e7lgfl cds-121")
    partners = soup.find_all("div",class_="css-oejgx0 cds-ProductCard-partners")
    skills = soup.find_all("div",class_="cds-CommonCard-bodyContent")
    ratings = soup.find_all("div",class_="cds-CommonCard-ratings")
    links = soup.find_all("a",class_ ="cds-119 cds-113 cds-115 cds-CommonCard-titleLink css-si869u cds-142")
    
except:
    print("Connection Error. Please run after some time...")
    exit()

# Opening a '.txt' file to write all the Courses details. Name of the File is the keywords we search for.
myfile = open(f"{keywords}_courses.txt","w")

for i in range(0,len(titles)-1):
    myfile.write("-"*100+"\n")
    myfile.write(titles[i].text+"\n")
    myfile.write("By "+partners[i].text[1:]+"\n")
    myfile.write(skills[i].text+"\n")
    myfile.write(ratings[i].text+"\t")
    myfile.write("https://www.coursera.org"+links[i]["href"]+"\n")
    myfile.write("_"*100+"\n")

myfile.close()