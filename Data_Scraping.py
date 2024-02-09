mapCord = "-118.33681%2C34.08500%2C15"
user = ''
loc = "UCLA"

# Define the path to your text file
file_path = "data.txt"  # Replace "your_file.txt" with the path to your text file

# Initialize an empty dictionary to store the data
data_dict = {}

# Open the text file and read its contents line by line
with open(file_path, "r") as file:
    for line in file:
        # Split each line into a date and a number
        date, number = line.strip().split()
        # Add the date and number to the dictionary
        data_dict[date] = int(number)

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time
from tqdm import tqdm

for date in tqdm(data_dict, desc="Capturing Screenshots"):
    # Initialize the WebDriver for Firefox
    browser = webdriver.Firefox()
    
    browser.maximize_window()

    # Navigate to the URL
    link = 'https://livingatlas.arcgis.com/wayback/#active='+ str(data_dict[date]) +'&mapCenter='+mapCord

    browser.get(link)

    # Wait for the cookie consent popup to load
    time.sleep(2)  # Adjust time as necessary

    # Click the "Accept All Cookies" button
    accept_button = browser.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_button.click()

    # Wait for the accept button to process
    time.sleep(2)

    checkbox_div = browser.find_element(By.CSS_SELECTOR, "div.margin-left-half.margin-right-quarter.cursor-pointer")
    checkbox_div.click()

    time.sleep(2)

    # Take a screenshot and save it
    screenshot_path = 'C:/Users/'+user+'/Downloads/'+loc+'/temp.png'
    browser.save_screenshot(screenshot_path)

    left = 400
    upper = 60
    right = 1910
    lower = 930

    # Open the full screenshot and crop it to the red boundary area
    img = Image.open(screenshot_path)
    cropped_img = img.crop((left, upper, right, lower))

    # Save the cropped image
    cropped_img_path = 'C:/Users/'+user+'/Downloads/'+loc+'/' + date + '.png'
    cropped_img.save(cropped_img_path)

    # Clean up by closing the browser
    browser.quit()