import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

# Ваше доменное имя DuckDNS и токен авторизации
DOMAIN = "garanre3.duckdns.org"
TOKEN = "4fae9c57-caac-4489-a50b-b175a0ef7969"

# Функция обновления IP-адреса на DuckDNS
def update_ip():
    try:
        # Получаем текущий IP-адрес
        current_ip = requests.get('https://api.ipify.org').text
        # Отправляем запрос на обновление IP-адреса на DuckDNS
        response = requests.get(f'https://www.duckdns.org/update?domains={DOMAIN}&token={TOKEN}&ip={current_ip}')
        if response.status_code == 200:
            print("IP адрес успешно обновлен на DuckDNS.")
        else:
            print("Ошибка при обновлении IP адреса на DuckDNS.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Класс для обработки HTTP запросов
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Возвращает HTML страницу с фоном
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Портфолио</title>
                <style>
                    body, html {
                        height: 100%;
                    }

                    body {
                        background-image: url('fon.jpg');
                        background-size: cover;
                        background-repeat: no-repeat;
                        background-position: center;
                        color: #ffffff;
                        text-align: center;
                        padding: 20px;
                        margin: 0;
                    }
                    .container {
                        max-width: 800px; /* Максимальная ширина контента */
                        margin: 0 auto;
                        padding-top: 20px;
                    }
                    .buttons {
                        position: absolute;
                        top: 20px;
                        right: 20px;
                    }
                    button {
                        margin: 10px;
                        background-color: #363636;
                        color: #ffffff;
                        border: none;
                        padding: 10px 20px;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #555555;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Мое портфолио</h1>
                    <div class="portfolio">
                        <!-- Здесь будет ваше портфолио -->
                        Шестой год подряд Владимир работает для вас и проводит ваши сделки за 2.5% от сумму! 
                        6 лет работы в сфере гарант услуг - это не просто цифра, это ценный опыт, который помогает обезопасить сделки от мошенников, защитить средства покупателя и товар продавца. 
                        С начала моего пути произошло огромное количество изменений как во мне, так и в моей работе. 25 декабря 2017 года был достигнут порог в 200 отзывов. 27 января 2018 года количество отзывов уже на отметке 500, а 3 октября 2019 уже на 1000! Но 23 июля 2020 года мне снесли страничку в вк... но теперь c новыми силами я открыл сайт где будет храниться вся моя история. Благодарен абсолютно каждому моему подписчику за доверие и за каждую проведенную через меня сделку, вы лучшие! 🕊
                    </div>
                </div>
                <div class="buttons">
                    <button onclick="showDealInfo()">Сделки</button>
                    <button onclick="showCurrencyExchangeInfo()">Обмен валют</button>
                    <button onclick="showGuarantorInfo()">О гаранте</button>
                </div>
                <script>
                    function showDealInfo() {
                        window.location.href = "/deal-info";
                    }
                    function showCurrencyExchangeInfo() {
                        window.location.href = "/currency-exchange-info";
                    }
                    function showGuarantorInfo() {
                        window.location.href = "/guarantor-info";
                    }
                </script>
            </body>
            </html>
            """
        elif self.path.endswith('.jpg'):
            # Отправляет изображение фона
            try:
                with open('fon.jpg', 'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'image/jpeg')
                    self.end_headers()
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404, 'File not found')
            return  # Завершаем выполнение метода после отправки изображения фона

        elif self.path == '/deal-info':
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Информация о сделках</title>
                <style>
                    body {
                        background-color: #212121;
                        color: #ffffff;
                        text-align: center;
                        padding: 20px;
                        margin: 0; /* Убираем отступы */
                    }
                    .container {
                        max-width: 800px; /* Максимальная ширина контента */
                        margin: 0 auto;
                        padding-top: 20px;
                    }
                    button {
                        margin: 10px;
                        background-color: #363636;
                        color: #ffffff;
                        border: none;
                        padding: 10px 20px;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #555555;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Информация о сделках</h1>
                    <!-- Ваш текст по сделкам здесь -->
                </div>
                <button onclick="goBack()">Назад</button>
                <script>
                    function goBack() {
                        window.history.back();
                    }
                </script>
            </body>
            </html>
            """
        elif self.path == '/currency-exchange-info':
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Информация об обмене валют</title>
                <style>
                    body {
                        background-color: #212121;
                        color: #ffffff;
                        text-align: center;
                        padding: 20px;
                        margin: 0; /* Убираем отступы */
                    }
                    .container {
                        max-width: 800px; /* Максимальная ширина контента */
                        margin: 0 auto;
                        padding-top: 20px;
                    }
                    button {
                        margin: 10px;
                        background-color: #363636;
                        color: #ffffff;
                        border: none;
                        padding: 10px 20px;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #555555;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Информация об обмене валют</h1>
                    <!-- Ваш текст по обмену валюты здесь -->
                </div>
                <button onclick="goBack()">Назад</button>
                <script>
                    function goBack() {
                        window.history.back();
                    }
                </script>
            </body>
            </html>
            """
        elif self.path == '/guarantor-info':
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Информация о гаранте</title>
                <style>
                    body {
                        background-color: #212121;
                        color: #ffffff;
                        text-align: center;
                        padding: 20px;
                        margin: 0; /* Убираем отступы */
                    }
                    .container {
                        max-width: 800px; /* Максимальная ширина контента */
                        margin: 0 auto;
                        padding-top: 20px;
                    }
                    button {
                        margin: 10px;
                        background-color: #363636;
                        color: #ffffff;
                        border: none;
                        padding: 10px 20px;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #555555;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Информация о гаранте</h1>
                    <!-- Ваш текст о гаранте здесь -->
                </div>
                <button onclick="goBack()">Назад</button>
                <script>
                    function goBack() {
                        window.history.back();
                    }
                </script>
            </body>
            </html>
            """
        else:
            self.send_error(404, 'Not Found')
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

# Запускаем функцию обновления IP-адреса
update_ip()

# Запускаем веб-сервер
server_address = ('', 80)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Starting server on port 80...")
httpd.serve_forever()
