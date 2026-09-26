from bs4 import BeautifulSoup
import requests

with open(r"D:\VIBE PROJECTS\Project 102\python-automation\Web-Automation\sample.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

# Get all book titles inside .book-card using CSS selector
titles = soup.select(".book-card .title a")
for title in titles:
    print(f"Title: {title.text} | Link: {title['href']}")

# Get only in-stock badges
in_stock = soup.select(".book-card .badge.in-stock")
print(f"\nIn-stock books count: {len(in_stock)}")


