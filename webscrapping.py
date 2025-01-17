#Libraries
from os import link
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs
#load required webpage content
r = requests.get("https://portfolio-rho-two-21.vercel.app/portfolio.html")
#convert to BeautifulSoup content
soup = bs(r.content)
print(soup.prettify())
#to find
bold = soup.find_all(input("enter the element you want to find: "))
print(bold)
#to call and find something specific
speci = soup.find_all("b", string=re.compile(input("Enter the Word you want to find: ")))
print(speci)
st = soup.find("b")
print("hey")
print(st.string)
links = soup.select("a")
s_links = [link['href'] for link in links]
print(s_links)
