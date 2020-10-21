# Jupyter Notebook Conversion to Python

# Dependencies
import time
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser

# Executable path to driver
executable_path = {"executable_path": "C:\Chrome Driver\chromedriver_win32\chromedriver.exe"}
browser = Browser("chrome", **executable_path)


# NASA Mars News
# Visit NASA Mars News and scrape headlines
nasa_url = 'https://mars.nasa.gov/news/'
browser.visit(nasa_url)
time.sleep(1)
nasa_html = browser.html
nasa_soup = BeautifulSoup(nasa_html, 'html.parser')

# Parse Results HTML with BeautifulSoup
nasa_soup = BeautifulSoup(nasa_html, 'html.parser')

# Pull latest title and paragraph
news_list = nasa_soup.find('ul', class_='item_list')
first_item = news_list.find('li', class_='slide')
nasa_headline = first_item.find('div', class_='content_title').text
nasa_teaser = first_item.find('div', class_='article_teaser_body').text


# JPL Mars Space Images - Featured Image
# Visit the JPL website and scrape the featured image
# Parse HTML with BeautifulSoup
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)
time.sleep(1)
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(1)

try:
    expand = browser.find_by_css('a.fancybox-expand')
    expand.click()
    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, 'html.parser')

    img_relative = jpl_soup.find('img', class_='fancybox-image')['src']
    image_path = f'https://www.jpl.nasa.gov{img_relative}'
  
except:
    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, 'html.parser')

# Display link to featured image
img_relative = jpl_soup.find('img', class_ = 'fancybox-image')['src']
image_path = f'https://www.jpl.nasa.gov{img_relative}'
print(image_path)


# Mars Facts
# Visit mars facts site and scrap table using Pandas
mars_df = pd.read_html("https://space-facts.com/mars/")[0]
mars_df.columns = ["Description", "Value"]
mars_df.set_index("Description", inplace=True)

# Convert data to a HTML table string
mars_df.to_html('table.html')


# Mars Hemispheres
# Visit the USGS Astrogeology Science Center Site
executable_path = {"executable_path": "C:\Chrome Driver\chromedriver_win32\chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
time.sleep(1)

hemisphere_image_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    browser.find_by_css("a.product-item h3")[item].click()
    
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    hemisphere_image_urls.append(hemisphere)
    browser.back()
    
    hemisphere_image_urls

    # Close the browser after scraping
    mars_data = {
        'nasa_headline': nasa_headline,
        'nasa_teaser': nasa_teaser,
        'image_path': image_path,
        'mars_df': mars_df,
        'hemispehere_imgage_urls': hemisphere_image_urls
    }

    browser.quit()

if __name__ == "__main__":
    scrap()
