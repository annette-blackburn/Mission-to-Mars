# Import Splinter and BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def run_mission(driver):
    sleep_time = 1
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    driver.get(url)

    full_image_links = driver.find_elements(By.CSS_SELECTOR, "div.item")

    mars_hemispheres = []

    for idx, link in enumerate(full_image_links):
        #button = link.find_element(By.CSS_SELECTOR, "a.itemLink.product-item")
        img_thumb = link.find_element(By.CSS_SELECTOR, "img.thumb")
        img_name = link.find_element(By.CSS_SELECTOR, "div.description").find_element(By.CSS_SELECTOR, "a.itemLink.product-item").text
        img_thumb.click()
        # TODO: Comment out this "sleep" call if you have nicer internet than me
        #sleep(sleep_time)

        img = driver.find_element(By.CSS_SELECTOR, "div.downloads")
        download_link = img.find_element(By.CSS_SELECTOR, "a")
        download_info = download_link.get_property("href")
        download_link.click()

        # TODO: Comment out this "sleep" call if you have nicer internet than me
        #sleep(sleep_time)
        driver.back()

        # TODO: Comment out this "sleep" call if you have nicer internet than me
        #sleep(15)
        mars_hemispheres += [{"img_url": download_info, "title": img_name}]

    #print(mars_hemispheres)

    driver.quit()
    return mars_hemispheres