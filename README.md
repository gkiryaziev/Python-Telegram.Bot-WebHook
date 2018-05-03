## Python-Telegram.Bot-WebHook.

[Telegram](https://telegram.org/) Bot ([Python 3](https://python.org/) / [Ngrok](https://ngrok.com/) / WebHook)

### Info
```
This is Telegram Bot, written in Python language with WebHook.
Answer comes to the local Flask server through the Ngrok service.
Server automatically receives a new Ngrok address and updates it in the Telegram WebHook, so run Ngrok first.
This project is under-development, but it works as example, I was just too lazy to make it beautiful ;D.
```

#### Install/Uninstall/Run
```bash
> python setup.py install

> pip uninstall telegram_bot

Windows:
> ngrok.exe http 5000
> telegram_bot.exe

Linux:
> ngrok http 5000
> telegram_bot


ngrok: https://62f3bc0d.ngrok.io/webhook
webhook: https://0b0477ff.ngrok.io/webhook
ngrok != webhook, setting up webhook url
ngrok: https://62f3bc0d.ngrok.io/webhook
webhook: https://62f3bc0d.ngrok.io/webhook
url's is equal, starting flask
 * Serving Flask app "telegram_bot.core" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
```

#### Use manually
#### Install Requirements
```bash
> pip install -r requirements.txt
```

### Usage
```bash
- create bot and get token
- set token in telegram_bot/core.py file
- run ngrok
- run server
- enjoy
```

#### Unittest
```bash
> python -m unittest tests/test_data.py
```

### Ngrok screenshot
![Alt text](/ngrok_scr.png?raw=true "ngrok screen")

### Bot screenshot
![Alt text](/bot_scr.png?raw=true "bot screen")