import pandas as pd
from datetime import datetime, date, timedelta
from pathlib import Path
from tqdm import tqdm
import shutil
import os, stat
import warnings
warnings.filterwarnings('ignore')

# Путь к папке с исходными файлами
data_check = input('Сначала сохранить свежие файлы в папку z:/Проектный офис/Протоколы/ Для завершения - Enter')

folder_path = Path('z:/Проектный офис/Протоколы/')
# Создание пустого списка для хранения DataFrame’ов

# Получаем список файлов для объединения
files_list = [file for file in folder_path.glob('DAT8651_*.xlsx')]

# Объединение всех файлов .xlsx в один большой файл
frames = []
for file_path in tqdm(files_list, desc='Объединение файлов', unit='файл'):
    df = pd.read_excel(file_path, sheet_name='Sheet', dtype='object')
    # df['файл'] = file_path
    frames.append(df)
# Объединение всех DataFrame’ов из списка

merged_frame = pd.concat(frames, ignore_index=True)
df_emias = merged_frame.copy()
df_emias['Дата протокола'] = pd.to_datetime(df_emias['Дата протокола'], errors ='coerce').dt.date

# Дубли
df_emias.drop_duplicates(inplace=True)


# Перед отправкой - исключить пустые НЕВИЗИТЫ !!!!!   Асцит
df_emias = df_emias[~df_emias['Асцит'].isna()]
df_emias.shape


df_emias.loc[  ~df_emias['Описание помощи в амбулаторных условиях'].isna() ,
                 'list_тип_визита'] = df_emias['Описание помощи в амбулаторных условиях'].str.split(';')
df_emias.loc[  ~df_emias['Дата следующего планового визита'].isna() ,
                 'list_дата_план_визита'] = df_emias['Дата следующего планового визита'].str.split(';')
df_emias.loc[ ( df_emias['list_тип_визита'].str[0] == 'визит врача'), 'план_дата_визит_врач' ] = df_emias['list_дата_план_визита'].str[0]
df_emias.loc[ ( df_emias['list_тип_визита'].str[1] == ' визит врача'), 'план_дата_визит_врач' ] = df_emias['list_дата_план_визита'].str[1]
df_emias.loc[ ( df_emias['list_тип_визита'].str[2] == ' визит врача'), 'план_дата_визит_врач' ] = df_emias['list_дата_план_визита'].str[2]
df_emias.loc[ ( df_emias['list_тип_визита'].str[3] == ' визит врача'), 'план_дата_визит_врач' ] = df_emias['list_дата_план_визита'].str[3]
df_emias['план_дата_визит_врач'] = pd.to_datetime(df_emias['план_дата_визит_врач'].str.strip()).dt.date
df_emias['ID пациента'] = df_emias['ID пациента'].astype('str')
df_emias = df_emias[[
                    'ID пациента',
                    'ОМС пациента',
                    'Дата протокола',
                    'ФИО врача',
                    'Бригада врача',
                    'ОВПП',
                    'Тип протокола',
                    'Диагноз пациента',
                    'Показания к паллиативной помощи',
                    'Категория пациента',
                    'Оказание паллиативной помощи',
                    'Состояние пациента',
                    'Болевой синдром',
                    'Оценка болевого синдрома на момент осмотра в баллах (ВАШ)',
                    'Оценка болевого синдрома на момент осмотра в баллах (НОШ)',
                    'Оценка болевого синдрома на момент осмотра в баллах (painaid)',
                    'Трахеостома',
                    'Респираторная поддержка',
                    'Мочеиспускание',
                    'Асцит',
                    'Установлено устройство',
                    'Дисфагия',
                    'Дисфагия. Степень',
                    'PPI',
                    'PPS',
                    'По шкале Морсе в баллах',
                    'По шкале Нортон в баллах',
                    'Описание помощи в амбулаторных условиях',
                    'Патронажный план',
                    'Частота посещений',
                    'Дата следующего планового визита',
                    'Дата следующего планового визита. С целью',
                    'Дата следующего планового визита. Причина',
                    'Манипуляции/Процедуры. Проведено',
                    # 'list_тип_визита',
                    # 'list_дата_план_визита',
                    'план_дата_визит_врач'
                     ]]
file_save_path = 'z:/Проектный офис/Протоколы/Все/Протокол ЕМИАС все визиты_' + datetime.now().strftime("%Y%m%d") + '.xlsx'

with pd.ExcelWriter(file_save_path,
                      engine="xlsxwriter",
                      date_format='DD.MM.YYYY',
                      datetime_format='DD.MM.YYYY HH:MM:SS') as writer:
    df_emias.to_excel(writer, index = False)

os.chmod(file_save_path, stat.S_IREAD)
# Оставляем только крайние визиты

df_emias = df_emias.sort_values(by=['ID пациента', 'Дата протокола'], ascending=[True, False]).drop_duplicates(subset=['ID пациента'])
file_save_path = 'z:/Проектный офис/Протоколы/Крайние визиты/Протокол ЕМИАС крайние визиты_' + datetime.now().strftime("%Y%m%d") + '.xlsx'

with pd.ExcelWriter(file_save_path,
                      engine="xlsxwriter",
                      date_format='DD.MM.YYYY',
                      datetime_format='DD.MM.YYYY HH:MM:SS') as writer:
    df_emias.to_excel(writer, index = False)

os.chmod(file_save_path, stat.S_IREAD)


data_check = input('Сохранил в .... z:/Проектный офис/Протоколы/Все/Протокол ЕМИАС все визиты_ \n '
                   'Для завершения - Enter')