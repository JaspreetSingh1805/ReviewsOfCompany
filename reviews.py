import csv
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = "https://www.google.com/maps/place/Synopsys+India+Private+Limited/@15.1824796,75.373524,7z/data=!3m1!5s0x3bae11363cb31c4d:0x631d242bf52b664e!4m12!1m2!2m1!1sSynopsys!3m8!1s0x3bae11363a32bc2b:0x922d8c930422b49e!8m2!3d12.994084!4d77.6614297!9m1!1b1!15sCghTeW5vcHN5cyIDiAEBkgEQc29mdHdhcmVfY29tcGFueeABAA!16s%2Fg%2F1tg9f_41?entry=ttu&g_ep=EgoyMDI0MDkyNS4wIKXMDSoASAFQAw%3D%3D"

driver.get(url)

time.sleep(5)

# Scroll inside the reviews section
def simple_scroll_and_collect_reviews(driver, scrolls=500, scroll_pause_time=2):
    reviews = set()  # Set to avoid duplicates
    
    # Wait until the reviews section is loaded
    reviews_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "m6QErb"))
    )
    
    for _ in range(scrolls):
        html = driver.page_source
        soup = BS(html, 'html.parser')

        # Update class names based on current inspection of the page
        divs = soup.find_all("div", class_="MyEned")  # Adjust class name
        names = soup.find_all("div", class_="d4r55")  # Adjust class name

        for div, name in zip(divs, names):
            review_text = div.get_text().strip()
            reviewer_name = name.get_text().strip()
            if review_text and reviewer_name:  # Ensure both review and name are not empty
                reviews.add((reviewer_name, review_text))  # Add as a tuple

        # Scroll inside the reviews section instead of the entire page
        driver.execute_script("arguments[0].scrollBy(0, 1000);", reviews_section)

        time.sleep(scroll_pause_time)

    return list(reviews)  # Return the reviews as a list

# Get overall rating (ensure the class is correct)
def get_overall_rating(driver):
    html = driver.page_source
    soup = BS(html, 'html.parser')
    
    overall_rating_div = soup.find("div", class_="gm2-display-2")  # Update this class based on the page
    if overall_rating_div:
        return overall_rating_div.get_text().strip()
    
    return None  # Return None if the overall rating is not found

# Scroll and collect reviews
all_reviews = simple_scroll_and_collect_reviews(driver, scrolls=500)

# Get overall company rating
overall_rating = get_overall_rating(driver)

# Write data to CSV
csv_filename = "google_company.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Name", "Review", "Overall Company Rating"])
    
    for name, review in all_reviews:
        writer.writerow([name, review, overall_rating])

print(f"Data successfully written to {csv_filename}")

driver.quit()
