from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

url = "https://www.instagram.com/"
insta_username = "your_username"
insta_password = "your_password"

username_to_send_the_reels = "username"
no_of_reels = 50

driver.get(url=url)

try:
    username = WebDriverWait(driver=driver, timeout=5).until(
        EC.element_to_be_clickable((By.NAME, 'username')))
except:
    print('Username field not found!')
else:
    username.send_keys(insta_username)

try:
    password = WebDriverWait(driver=driver, timeout=5).until(
        EC.element_to_be_clickable((By.NAME, 'password')))
except:
    print('Password field not found!')
else:
    password.send_keys(insta_password)
    password.send_keys(Keys.ENTER)

try:
    not_now = WebDriverWait(driver=driver, timeout=5).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
except:
    print('Not now button not found!')
else:
    not_now.click()

try:
    not_now = WebDriverWait(driver=driver, timeout=5).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
except:
    print('Not now button not found!')
else:
    not_now.click()

sleep(2)

driver.get(url="https://www.instagram.com/reels/")

j = 1


def run():
    global j
    sleep(1)

    def share():
        global j
        try:
            share = WebDriverWait(driver=driver, timeout=5).until(EC.element_to_be_clickable(
                (By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[{j}]/div/div[2]/div[3]/div')))
        except:
            print('Share button not found!')
        else:
            share.click()
    share()

    try:
        input_username = WebDriverWait(driver=driver, timeout=5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/input')))
    except:
        share()
    else:
        input_username.send_keys(username_to_send_the_reels)

    try:
        select_user = WebDriverWait(driver=driver, timeout=5).until(EC.element_to_be_clickable(
            (By.NAME, 'ContactSearchResultCheckbox')))
    except:
        print('Select user box not found!')
    else:
        sleep(1)
        select_user.click()

    try:
        send_btn = WebDriverWait(driver=driver, timeout=5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div')))
    except:
        print('Send Button not found!')
    else:
        send_btn.click()
    j += 2


sleep(5)

try:
    body = WebDriverWait(driver=driver, timeout=10).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'body')))
except:
    print('Body not found!')
else:
    body.click()
    no_of_reels = no_of_reels*2
    for i in range(0, no_of_reels):
        run()
        sleep(1)
        body.send_keys(Keys.DOWN)
