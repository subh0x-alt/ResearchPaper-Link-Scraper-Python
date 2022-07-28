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
# Manipulate the url to get the required number of entries:
def url_manipulator(url, num_entries):
    # Manipulate the url to be compatible with the Science Direct search
    if (num_entries > 25 & num_entries <= 100):
        if (num_entries <= 50):
            num = 50
        else:
            num = 100
        url = url + f"&show={num}"
    else:
        # Need to work on this!!!!
        # url = url + f"&show=100&offset={num}"
        pass
    return url

# Function to get and store the data from the search page
def get_data(driver):
    # Incomplete: working on this!!!!
    # Get the data from the search page:
    data = driver.find_elements_by_class_name("result-item")
    # Store the data in a list:
    data_list = []
    for i in data:
        data_list.append(i.text)
    return data_list

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
            # Call the url manipulator function to manipulate the url:
            url = url_manipulator(driver.getCurrentUrl(), num_entries)
            # Incomplete: working on this!!!!
            # Wait for the page to load:
            sleep(randrange(1, 3))
            get_data(driver.get(url))
            
    
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