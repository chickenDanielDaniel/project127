from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("/Users/greeniewu/Dropbox/Mac/Desktop/PythonTesting/Class127/Project127/chromedriver")
browser.get(START_URL)
time.sleep(10)

headers = ["Name","Distance","Mass","Radius"]
star_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for tr_tag in soup.find_all("tr",attrs={"class","wikitable sortable jquery-tablesorter"}):
        td_tags = tr_tag.find_all("td")
        temp = []
        for index,td_tag in enumerate(td_tags):
            if index == 0:
                temp.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp.append(td_tag.contents[0])
                except:
                    temp.append("")

        star_data.append(temp)
                #To go to next page
        browser.find_element(By.XPATH,value = '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            #browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
with open("Scraper1.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

scrape()