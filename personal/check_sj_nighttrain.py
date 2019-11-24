#!/usr/bin/env python3
# by rog

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.sj.se/#/tidtabell/Abisko%2520turiststation/Stockholm%2520Central/enkel/avgang/20200409-0500/avgang/20200409-1500/VU--///0//")

print(driver.title)
bucket = driver.find_element_by_class_name('timetable-unexpanded-price__container')
print(bucket.text)


driver.quit()