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

    browser.find_by_tag('button')[1].click()
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    carousel_item =  soup.find('img', class_='fancybox-image')
    split_text = src.split("'")
    print(split_text[0])
    featured_image_url = 'https://spaceimages-mars.com/' + split_text[0]
    
    """
    Mars Fact Alternate
    """
    #Mars facts URL with Earth and Mars comparison
    #url3 = 'http://space-facts.com/mars/'
    #browser.visit(url3)
    #time.sleep(1)

    #tables = pd.read_html(url3)
    #df = tables[0]
    #df.columns = ["Parameter", "Mars", "Earth"]
    #df.set_index('Parameter', inplace=True)
    
    
    #mars_fact_dict = df.to_html()
    


    """
    Mars Fact
    """
    # Mars Facts URL
    url = r"https://galaxyfacts-mars.com/"
    browser.visit(url)
    tables = pd.read_html(url)
    df = tables[1]
    df.columns = ['Fact', 'Value']
    df.set_index("Fact", inplace=True)
   
    html_table = df.to_html(table_id='scrape_table')
    
   
    """
    Mars Hemispheres
    """
    #Mars Hemispheres URL
    url = "https://marshemispheres.com/"    
    browser.visit(url)
    time.sleep(2)    
    
    
    img_url_list = []
    title_list = []
    hemi=2
    count=1
    x=0
    
    
#    url = "https://marshemispheres.com/"
    url = "https://marshemispheres.com/    
#    xpath = ('//*[@id="product-section"]/div[2]/div[' + str(hemi) +']/div/a/h3')
   #X Path into the Four Hemisphere Images
    xpath = ('//*[@id="publish"]/div[1]/div[1]/div[4]/div/a[' + str(hemi) +']/div/h3')    
#              //*[@id="publish"]/div[1]/div[1]/div[4]/div/a[4]/div/h3
#              //*[@id="publish"]/div[1]/div[1]/div[4]/div/a[6]/div/h3
#              //*[@id="publish"]/div[1]/div[1]/div[4]/div/a[8]/div/h3
    while count < 5:
        browser.visit(url)

        hemi_name = browser.find_by_xpath(xpath).text
        title_list.append(hemi_name)
        results = browser.find_by_xpath(xpath)

        img = results[0]
        img.click()
        time.sleep(2)

        # Scrape page into Soup
       browser.find_by_css('a.product-item img')[i].click()
        hemis_element = browser.links.find_by_text('Sample').first 
        hemisphere_dic['image_url'] = hemis_element['href']
        hemisphere_dic['hemisphere_title'] = browser.find_by_css('h2.title').text
        image_urls.append(hemisphere_dic)

        hemi+=2

        xpath = ('//*[@id="publish"]/div[1]/div[1]/div[4]/div/a[' + str(hemi) +']/div/h3')  
        count+=1
        x+=1
    
    image_urls = []
    h=0
    for items in title_list:
        if h < 4:
            dict = {"title": title_list[h], "img_url": img_url_list[h]}
            image_urls.append(dict)
            h+=1
    
    
    # Store data in a dictionary
    mars_data = {
       #News Title
       "news_title": news_title,
       #News Title
       "news_p": news_p,
       #Featured Image
       "featured_image_url": featured_image_url,
       #Mars Facts
       "html_table":html_table,
       #Mars Four Hemispheres
       "image_urls":hemisphere_image_urls
   }

    browser.quit()
    
   return mars_data