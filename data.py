from urllib.request import urlopen
from bs4 import BeautifulSoup

# NBA season we will be analyzing
year = 2019

# URL page we will be scraping
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

# This is the HTML from the given URL
html = urlopen(url)

soup = BeautifulSoup(html, features="html.parser")

# Use findAll() to get the column headers
soup.findAll('tr', limit=2)

# Use getText() to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
headers = headers[1:]

# Setting up a 2-Dimensional list
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]