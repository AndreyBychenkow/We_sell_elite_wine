# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/AndreyBychenkow/We_sell_elite_wine
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt   
   ```
## Запуск

1. **Создайте файл .env и укажите путь к файлу с данными:**
   ```bash
   WINE_FILE_PATH=ваш путь к файлу   
   ```
   
2. **Запустите скрипт:**
   ```bash
   python main.py  
   ```

3. **Проверьте результат:**

После запуска программы в корневом каталоге должен появиться файл index.html. Откройте его в веб-браузере, чтобы увидеть результат.
  
Или перейдите по адресу: [127.0.0.1:8000/index.html](127.0.0.1:8000/index.html).


## Образец входных данных

Программа ожидает данные в формате Excel. Пример данных:

![Excel данные](https://i.postimg.cc/90Z2Qnsv/2.jpg) 

Для использования этих данных создайте Excel-файл с указанными колонками.


## Результат

   **Каталог вин отобразится в браузере**
   
   ![Результат](https://i.postimg.cc/264GvKcF/15-11-2024-173659.gif) 
   
   
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
