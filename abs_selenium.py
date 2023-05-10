from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
# options.add_argument('--headless')

driver = webdriver.Chrome(
    executable_path= '/Users/kizakitakao/Desktop/Lesson/tools/chromedriver',
    options=options)


driver.implicitly_wait(10)

url = 'https://search.yahoo.co.jp/image'

driver.get(url)
sleep(3)

search_box = driver.find_element_by_css_selector('.SearchBox__searchInputWrap > input.SearchBox__searchInput')
sleep(3)

search_box.send_keys('six-pack')
sleep(3)

search_box.submit()
sleep(3)

while True:
    prev_html = driver.page_source
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    current_html = driver.page_source
    sleep(3)
    
    # もし「もっと見る」ボタンがあれば、それをクリックして再度スクロールする
    # 「もっと見る」ボタンがなければ、スクロールを止める
    button = driver.find_elements_by_css_selector('.sw-MoreButton.target_modules > div > button.sw-Button.sw-Button--level4.sw-MoreButton__button.cl-noclick-log')
    sleep(3)
    
    if button:
        button[0].click()
    else:
        break

sleep(3)

with open('image_data.html', 'w') as f:
    f.write(current_html)
    
driver.quit()

