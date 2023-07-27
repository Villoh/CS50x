# Botilloh. A simple discord bot
#### Video Demo: https://youtu.be/O8ZDqOPFDlo <URL HERE>

### Description:
This is a Python Discord bot using discord.py that provides a variety of useful commands and features for server moderation, fun, productivity and more. The bot is designed to enhance your Discord server, it aims to provide a full suite of features for an all-in-one Discord assistant bot. Actually, is under active development to expand its features and utilities.

>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id sodales leo, non imperdiet turpis. Donec nec erat maximus, fermentum nunc vel, gravida ex. Mauris ornare lorem in nisl sollicitudin vehicula. Maecenas leo tortor, ultricies id facilisis ac, sollicitudin sed augue. Vivamus vulputate odio sit amet nisl eleifend, eu commodo dolor malesuada. Mauris porttitor, augue non convallis varius, libero odio dapibus dui, blandit pulvinar mauris justo id arcu. Nulla facilisi. Ut porta non magna ut efficitur. Curabitur molestie neque dolor, in viverra nisi pulvinar nec. Fusce malesuada orci id erat viverra lacinia. Nunc magna nunc, semper nec tempus a, finibus et lorem.

## Features
- Responds with weather information with a .png image.
- Translates text into multiple languages with [DeepL](http://deepl.com)
- Deletes message(s) from the channels with the ability to filter by date.
- Do some maths with the in-built calculator.

## Commands
- `/ping` - Gets a response from the server if it's running with the time in ms that it took to respond.
- `/sync` - Synchronize all the commands with the discord client server.
- `/weather <location>` - Gets current weather and temperature for a location
- `/translate <text> <dest>` - Translates text to another language.
- `/calculator` - Displays a simple calculator with discord buttons to do some basic maths.
- `/purge <amount>  Optional<before> Optional<after>` - Deletes specified number of messages.

## Technologies Used

- [**discord.py**](https://github.com/Rapptz/discord.py) - Python library for interacting with the Discord API
- [**deepl**](https://github.com/DeepLcom/deepl-python) - Implements the requests into their API. Functions for translating are implemented.
- [**wttr.in**](https://github.com/chubin/wttr.in) - Provides worldwide weather data including current conditions.
- [**aiohttp**](https://github.com/aio-libs/aiohttp) - For making asynchronous HTTP requests to the API
- [**Python 3.11**](https://github.com/python) - Programming language used

## Setup

1. `git clone https://github.com/villoh/botilloh`
2. `pip install -r requirements.txt`
3. Add Discord bot token in `token` file and DeepL token in `deepl_token` or use environment variables.
4. `python client.py`

## Contributing

Pull requests are welcome! Feel free to open issues for any bugs or desired features.

