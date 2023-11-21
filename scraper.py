import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data = []
URL = "https://www.youtube.com/watch?v=FIXgPQsSCm8&ab_channel=DreamJelly"

# Setup Chrome driver without the 'with' statement
driver = webdriver.Chrome()

try:
    wait = WebDriverWait(driver, 15)
    driver.get(URL)

    # Scroll down the page to load comments
    for item in range(200): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(2)  # Reduced sleep time for faster execution

    # Collect comments
    comments = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-comment-renderer #content")))
    for comment in comments:
        data.append(comment.text)

finally:
    # Close the driver after execution
    driver.quit()

# Write data to a file
with open('comments.txt', 'w', encoding='utf-8') as file:
    for comment in data:
        file.write(comment + "\n")
