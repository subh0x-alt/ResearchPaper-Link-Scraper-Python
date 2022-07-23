## Test version:
# selenium 4
from asyncio import Handle
from selenium import webdriver
# importing necessary firefox webdriver modules
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import sys # For Retrirving the address from the commandline
# import os
from time import sleep
from random import randrange
import pandas as pd

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
    sleep(2) # seconds
    bttn_Xpath = "/html/body/div/div/div/div/div/div/div/section/div/div[1]/div/div/div/div[2]/div/form/div/div/div[4]/div/div[2]/button"
    driver.find_element(By.XPATH, value=bttn_Xpath).click()
except:
    print('Text Search Button not found!')

# Wait for the page to load
sleep(randrange(10,15))# seconds

## Intitialize empty lists to store data
articles_type = []
titles = []
# authors = []
journals = []
# journal_infos = []
# urls = []
# Research paper digital object identifier[doi] link
doi_links = []
# Collect all the info in articles:
article_containers = driver.find_elements(By.ID, 'srp-results-list')

for article in article_containers:
    try:
        article_type = article.find_element(By.CSS_SELECTOR, '.article-type u-clr-grey8'.replace(' ', '.')).text
        title = article.find_element(By.CSS_SELECTOR, '.anchor result-list-title-link u-font-serif text-s anchor-default'.replace(' ', '.')).text
        journal = article.find_element(By.CSS_SELECTOR, '.anchor subtype-srctitle-link anchor-default anchor-has-inherit-color'.replace(' ', '.')).text
        # journal_info = article.find_element().text
        # author = article.find_element().text
        # url = article.find_element().text
        doi_link = article.get_attribute('data-doi')
        articles_type.append(article_type)
        titles.append(title)
        journals.append(journal)
        # journal_infos.append(journal_info)
        # urls.append(url)
        doi_links.append(doi_link)
    except Exception as err:
        print(f'Error while scraping data: {err}')
        continue


article_container_df = pd.DataFrame({'article_type': articles_type, 'title': titles, 'journal': journals, 'doi-link': doi_links})

# article_container_df = pd.DataFrame({'article_type': articles_type, 'title': titles, 'journal': journals, 
# 'journal_info': journal_infos, 'url': urls, 'doi-link': doi_links})

# TODO: Add paginations for extracting articles from other pages as well.

# TODO: Exporting the results to a .json file.
article_container_df.to_json('Researchpaper_list.json', orient = 'split', compression = 'infer')