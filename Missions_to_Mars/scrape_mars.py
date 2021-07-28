from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time




def init_browser():
   # @NOTE: Path to my chromedriver in the homework folder
   executable_path = {'executable_path':r'C:\Users\firme\OneDrive\Documents\GitHub\web-scraping-challenge\Missions_to_Mars\chromedriver'}
   return browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser=init_browser()
     
    """
    NASA Mars News
    """
    #Mars News URL
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(3)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title =  soup.find('div', class_='col-md-12').text
    news_p = soup.find('div', class_='article_teaser_body').text
   
    """
    JPL Mars Space Images - Featured Image
    """
    # Featured Space Image URL
    url1 = 'https://spaceimages-mars.com/'
    browser.visit(url1)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    carousel_item =  soup.find('article', class_='carousel_item')
    style = carousel_item["style"]
    split_text = style.split("'")
    featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg' + split_text[1]
    
    
   