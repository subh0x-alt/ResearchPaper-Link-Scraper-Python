# Import Selenium 4: firefox webdriver modules:
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# Importing time functions:
from time import sleep
from random import randrange

class ScienceDirectScraper():
    """
    Science-Direct Articles Scraper. 
    @Version:       v1.5.0
    @Last updated:  24 July 2022.
    @Author:        Subhrajit Guchait.
    """
    def __init__(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def get_articles(self, *args):
        """
        Function to generate a list of articles using a list of input keywords.

        
        """
        #default keywords:
        def_search_keys = ['Microchannel', 'Fluid', 'Flow', 'Analysis']
        self.driver.get(f'https://www.sciencedirect.com/search')

