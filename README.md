#!/usr/bin/python
# -*- coding: UTF-8 -*-
Суперучебник 

https://proproprogs.ru/python

https://www.youtube.com/watch?v=crUHP8Zo12k
   Фласк уроки
 ------------------------------------
 
   
 
https://www.youtube.com/watch?v=U3wGN6qNKFA&list=PLyaCd9XYVI9DiMvYl-8OdZk7ktc6NQWrb <br>

  Сеньер-помидор ДЖАНГО Ютуб
-----------------------------------
             
  
https://live.skillbox.ru/webinars/code/parser-na-python-za-3-dnya-poslednie-shtrikhi-i-podvedenie-itogov040522/
Парсер на Python за 3 дня: последние штрихи и подведение итогов
Деплой и размещение на сервере 48:06....
- зарегистрировать
- запустить виртуальную машину
-...
----------------------   
https://www.youtube.com/watch?v=TiHOQwzBOOc
Как создать мессенджер на Python. Интенсив по программированию
  
-----------------
Интенсивы Skillbox
https://live.skillbox.ru/webinars/code/parser-na-python-za-3-dnya-poslednie-shtrikhi-i-podvedenie-itogov040522/

---------------------- 

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
#### считать из json
          with open('c:\\Users\\stavr\\Downloads\\mongo.json', 'r', encoding='utf-8') as j_file: #открываем файл на чтение
              data1 = json.load(j_file)

#### сохранить в json
          with open('c:\\Users\\stavr\\Downloads\\mongo_new_3.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
              fh.write(json.dumps(data_3, ensure_ascii=False)) 
-------------------------------------------------------------------
     pip freeze > requirements.txt
     python -m pip install -r requirements.txt  
     или 
     pip install -r requirements.txt 
