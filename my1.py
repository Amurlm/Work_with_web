import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import re
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
# driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
url = 'https://finance.yahoo.com/quote/{}/financials?p={}'
stoke = 'F'
driver.get(url.format(stoke, stoke))
time.sleep(5)
# print(driver.find_element_by_id('content').text)

pageSource = driver.page_source
soup = BeautifulSoup(pageSource, 'html.parser')
driver.close()

pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]

print (script_data[:500])

def main ():
    pass

if __name__ == '__main__':
    main ()
