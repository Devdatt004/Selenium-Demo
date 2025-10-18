from selenium import webdriver\n\ndriver = webdriver.Chrome()\ndriver.get('https://www.google.com')\nprint(driver.title)\ndriver.quit()
