from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from operator import itemgetter
import json
import os.path

## Setup chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless") # Ensure GUI is off
#chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/pyhton-scripts/chromedriver/stable/chromedriver")

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
file1 = open("nendoroids.txt","w")


def run_scrapper(year):
    driver.get('https://www.goodsmile.info/en/products/category/nendoroid_series/announced/' + str(year))
    driver.implicitly_wait(10)

    #driver.find_element(By.XPATH, '//*[@id="nendoroid"]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/ul/li[2]/span').click()
    driver.implicitly_wait(10)
    a = driver.find_elements(By.CSS_SELECTOR, ".hitItem.nendoroid.nendoroid_series")
    
    
    if a is None:
        return
    
    list = []
    

    for x in a:
        el = x.find_elements(By.TAG_NAME,'a')[0]
        link = el.get_attribute('href')
        a_html = el.find_elements(By.TAG_NAME,'img')[0]
        image = a_html.get_attribute('src')
        details = el.find_elements(By.TAG_NAME,'span')
        name = details[1].get_attribute('innerHTML')
        if len(details) > 2:
            number = details[2].get_attribute('innerHTML')
            list.append({'name' : name, 'number': number, 'url': link, 'image': image, 'year': year })
    sorted_list = sorted(list, key=itemgetter('number'))
    for item in sorted_list:
        file1.write(json.dumps(item) + ',\n')



for year in range(2006, 2024):
    run_scrapper(str(year))



file1.close()
