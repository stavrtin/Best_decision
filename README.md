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
#### -------------------ХРОМДРАЙВЕР-------------------
          
     options = webdriver.ChromeOptions()
     options.add_experimental_option('excludeSwitches', ['enable-logging'])
     s=Service('C:/chromedriver.exe')
     driver = webdriver.Chrome(service=s, options=options)


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

-----------------------------------------
Цвета
https://github.com/ikalnytskyi/termcolor

     from termcolor import colored, cprint

     print(colored('Привет мир!', 'green', attrs=['underline']))
     # print(colored('Hello, World!', 'green', 'on_grey', 'blink'))
     print(colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink']))
