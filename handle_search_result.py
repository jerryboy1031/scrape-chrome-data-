# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:14:22 2023

@author: User
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv

def saveTOcsv(data):
    # Save data to CSV file
    csv_file = "google_search_results.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "URL", "Snippet"])  # Header row
        writer.writerows(data)
        
def extract_website():
    # Configure Selenium
    driver_path = "/chromedriver_win32/chromedriver.exe" # Path to your ChromeDriver executable
    service = Service(driver_path)  
    options = Options()
    options.headless = True  # Run the browser in headless mode (without GUI)
    driver = webdriver.Chrome(service=service, options=options)

    # Define search query
    search_query = "法國自由行景點"  # Enter your desired search query

    # Perform search and extract data
    driver.get(f"https://www.google.com/search?q={search_query}")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find search result elements
    search_results = soup.find_all("div", class_="yuRUbf")

    # Extract data from search results
    results_data = [] # [ [title, url, snippet],...]
    for result in search_results[:10]:
        title = result.find("h3").get_text()
        url = result.find("a")["href"]
        snippet_element = result.find("span", class_="aCOpRe")
        snippet = snippet_element.get_text() if snippet_element else ""
        
        results_data.append([title, url, snippet])
        
    #saveTOcsv(data_results)
    
    # Close the browser
    driver.quit()

    #print("Scraping completed and data saved to", csv_file)
    print(results_data)



if __name__ == '__main__':
    extract_website()