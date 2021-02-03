# QRCode-Telegram-bot

## installation

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/46b19b1337ea4f68b6aa1a2b1275ab64)](https://app.codacy.com/gh/Abhijith-cloud/QRCode-Telegram-bot?utm_source=github.com&utm_medium=referral&utm_content=Abhijith-cloud/QRCode-Telegram-bot&utm_campaign=Badge_Grade)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Abhijith-cloud/QRCode-Telegram-bot/)

Libraries used: => Pyrogram => Telegraph

```sh
git clone https://github.com/Abhijith-cloud/QRCode-Telegram-bot.git / gh repo clone Abhijith-cloud/QRCode-Telegram-bot
```
```sh
pip3 install -r requirements.txt
```
### Add your bot details

An example `env.py` file could be:

```python3
class EnvData:
    BOT_TOKEN = '1991308069:tU1gaAyvgAAGgo3F2AI2J7nxcqvkwoTCrpY' #add your API_HASH from https://my.telegram.org/apps
    API_ID = 1234567 #Add your API_ID from https://my.telegram.org/apps
    API_HASH = 'bc4811980930ad49d7f8e2b024f7cf13' #Add your Bot token from @Botfather
```
Go and get the bot token [@BotFather](https://telegram.dog/BotFather)

click the link to get your app id & api_hash [my.telegram.org](https://my.telegram.org/auth)

### Run your Bot

```sh
python3 main.py
```

## Credits, and Thanks to

* [Dan Tès](https://telegram.dog/haskell) for his[Pyrogram Library](https://github.com/pyrogram/pyrogram)

### LICENSE
- GPLv3
