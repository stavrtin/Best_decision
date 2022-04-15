Просто респонсы 
--------------------------------------------
#### Импортируем библиотеки
from pprint import  pprint
from lxml import html
import requests

url = 'https://sport-dealer.ru/search/?query=Amino+X%2C+435+g'

response = requests.get(url)
dom = html.fromstring(response.text)
dom.xpath('//h1')[0].text
------------------------------------------------
 
Селен
 #### ---- нажимаем кнопку ПРОЧАЯ ИНФОРМАЦИЯ ------
 
button_zakl = driver.find_elements(By.XPATH, '//div[@class ="mat-tab-label-content"]')[1] # --- закладка ----
actions = ActionChains(driver)
actions.move_to_element(button_zakl)
actions.click(button_zakl)
actions.perform()
    
    
Селен
 #### ---- нажимаем PageDown кнопку  ------
    actions = ActionChains(driver)
    actions.key_down(Keys.PAGE_DOWN)
    actions.perform()
