# --- -- ОФОРМЛЕНИЕ jupytherNotebook ----------
https://medium.com/analytics-vidhya/the-ultimate-markdown-guide-for-jupyter-notebook-d5e5abf728fd
  
  
             
 
# --- -- сводник для датафрейма ----------
https://dfedorov.spb.ru/pandas/%D0%A1%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D0%B2%20pandas.html
----------------------
https://habr.com/ru/company/ruvds/blog/494720/
     
-----------------------
https://medium.com/nuances-of-programming/%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B5-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%8B-%D0%B2-jupyter-notebook-82475fbed7de
--------------------- 
             
####  
--- условие для  нескольких условий в ДАТАФРЕЙМЕ ----------

def flag_df(df):
    if (df['trigger1'] <= df['score'] < df['trigger2']) and (df['height'] < 8):
        return 'Red'
    elif (df['trigger2'] <= df['score'] < df['trigger3']) and (df['height'] < 8):
        return 'Yellow'
    elif (df['trigger3'] <= df['score']) and (df['height'] < 8):
        return 'Orange'
    elif (df['height'] > 8):
        return np.nan 
df2['Flag'] = df2.apply(flag_df, axis = 1)


#### 
шаблон тлг-бота 
------------------
        from tok import token
        import telegram
        from telegram import Bot
        from telegram.ext import CommandHandler, MessageHandler, Updater

  

        bot = Bot(token=token)   # ---- внести  токен бота

        updater = Updater(token, use_context=True)
        dispatcher = updater.dispatcher

        def start(updater, context):
            updater.message.reply_text('asdasdas')
            # context.bot.

        start_handler = CommandHandler('start', start)

        dispatcher.add_handler(start_handler)

        updater.start_polling()
        updater.idle()

------------------
#############################################################
        бот с кнопками 
        https://gbcdn.mrgcdn.ru/uploads/asset/4526259/attachment/ddbbd77484b1b6eb540bf5856cdf236f.txt


### docer
------------------
Docker 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru
--------------------------
 
   
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
 
headers = {'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url = 'https://sport-dealer.ru/search/?query=Amino+X%2C+435+g'

    response = requests.get(url, headers=headers)
    dom = html.fromstring(response.text)
    dom.xpath('//h1')[0].text
    
    


  
    
    
------------------------------------------------
  
Селен

# from datetime import time, date, datetime, timedelta
from datetime import time, date, datetime, timedelta
import wait as wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import exceptions as se
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
