from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()

# Visit the url page
url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=en_US"

browser.get(url)

# Scroll down to a certain point
# browser.execute_script("window.scrollTo(0, 1440)")

interval = 2  # Scroll down every 2 sec.

# Save the height of the each scroll
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # Wait for the page loading
    time.sleep(interval)

    # Save the height of the current position
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("Finish scrolling")


soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # Original price
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})

    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, " <Excluding movies with no sale price>")
        continue

    # Movies with the sale price
    sale_price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    # Correct link : https://play.google.com + link

    print(f"Title : {title}")
    print(f"Original Price : {original_price}")
    print(f"Sale Price : {sale_price}")
    print("Link : ", "https://play.google.com" + link)
    print("-" * 120)

    browser.quit()
