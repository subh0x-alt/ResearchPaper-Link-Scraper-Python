# Import Selenium 4: firefox webdriver modules:
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import sys
# Importing time functions:
from time import sleep
from random import randrange

"""
Science-Direct Articles Scraper.
--Work In Progress--
@Version:       v1.5.0
@Last updated:  28 July 2022.
@Author:        Subhrajit Guchait.
"""

def url_manipulator(url, num_entries):
    # Manipulate the url to be compatible with the Science Direct search
    if (num_entries > 25 & num_entries <= 100):
        if (num_entries <= 50):
            num = 50
        else:
            num = 100
        url = url + f"&show={num}"
    else:
        # url = url + f"&show=100&offset={num}"
        pass
    return url


# Extract the links and info about the research papers:
def extract_links(driver):
    # create a if-else statement to get the number of entries to be extracted.
    num_entries = int(input("Enter the number of entries to be extracted:\t"))
    if num_entries < 1:
        sys.exit("Error: ScienceDirectScraper: Invalid number of entries to be extracted.")
    else:
        print(f"{num_entries}" + " entries will be extracted.")
        # Extract the links and info about the research papers:
        if num_entries <=25:
            pass
        else:
            driver.getCurrentUrl()
            # Call the url manipulator function to manipulate the url:
            url = url_manipulator(driver.getCurrentUrl(), num_entries)
            driver.get(url)
            # Wait for the page to load:
            sleep(randrange(2, 5))
            sys.exit("Error: ScienceDirectScraper: Invalid number of entries to be extracted.")
    
def ScienceDirectScraper():

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # Handle exceptions while opening the browser:
    try:
        if len(sys.argv) > 2:
            search_keys = " ".join(sys.argv[1:])
        else:
            search_keys = "Microchannel Fluid Flow Analysis"
        # Search the Science Direct website
        # Manipulate the input strings to be compatible with the Science Direct search
        search_keys = search_keys.replace(" ", "%20")
        driver.get(f'https://www.sciencedirect.com/search?qs='+ search_keys) # Open the Science Direct website.
    except:
        # Exit the program:
        sys.exit("Error: ScienceDirectScraper: Failed to open the Science Direct website.")

    # Wait for the page to load
    sleep(randrange(2, 5))
    
    response = input("Do you want to extract the links and info about the research papers? [Y/n]\t")
    if response.lower() == "y":
        # Extract the links and info about the research papers:
        extract_links(driver)
    else:
        # Exit the program:
        sys.exit("Error: ScienceDirectScraper: Failed to extract the links and info about the research papers.")


ScienceDirectScraper()