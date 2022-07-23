# selenium 4
from asyncio import Handle
from selenium import webdriver
# importing necessary firefox webdriver modules
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import sys # For Retrirving the address from the commandline
# import os

# REVIEW: Build a Web Scraper to fetch Research Paper links and short summary on the papers and their 
# REVIEW: authors that matches the topics given in the command line input.
# REVIEW: from the Science Direct website using python and selenium
# REVIEW: save the links to a .txt file named with tags (ex:ResearchPapers-<tag1>_<tag2>)

# TODO: 1. Create a Simple web searcher for the Science Direct website which topic takes input from commandline

# get the address from either the command line or clipboard.
# if len(sys.argv) > 2:
topic = ' '.join(sys.argv[1:])
# else:
#     # TODO: Implement a function to read file named 'topics.txt' from the current directory.
#     topic = input("Enter the topics for which you want to search:\t")

topic_search = topic.replace(',', '')
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.sciencedirect.com/search')

# TODO: Enter the tags/topics into the 'Keywords' field
# Handling exceptions
try: 
    driver.find_element(By.ID, "qs").send_keys(str(topic_search))
except:
    print('Text SearchBox not found!')
    
# TODO: Make a search by clicking the search button

try:
    driver.implicitly_wait(2) # seconds
    bttn_Xpath = "/html/body/div/div/div/div/div/div/div/section/div/div[1]/div/div/div/div[2]/div/form/div/div/div[4]/div/div[2]/button"
    driver.find_element(By.XPATH, value=bttn_Xpath).click()
except:
    print('Text Search Button not found!')