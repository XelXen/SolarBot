<h1 align="center">SolarBot</h1>
<p align="center">A simple chatbot for telegram that utilizes the power of Machine Learning and AI for sending replies</p>

### Contents

- [Disclosure](#disclosure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Disclosure

This project is created purely with educational and research purposes in mind. You will be held responsible for all the actions.

## Requirements

This script requires the below packages to run

| Packages |
| --- |
| os |
| [transformers](https://pypi.org/project/transformers/) |
| [pyrogram](https://pypi.org/project/pyrogram/) |

## Installation

- Clone this repository: `git clone https://github.com/XelXen/SolarBot`
- Install Python: [Click here for a tutorial](https://realpython.com/installing-python/)
- Install required libraries via `pip` through the command `pip3 install -r requirements.txt`.

## Usage

- Before hosting the bot, we have to make sure that the host can handle the load of the bot. I would suggest an internet connection of 50MB/s, 16GB RAM, 4 Threads CPU and 10GB Storage.

- If you're ready then we will being with our first step, collecting the necessary information for the bot. You have to collect api_id, api_hash and bot_token (optional). You can get your api id and api hash by creating an application or using the current one from [here](https://my.telegram.org) and clicking on API development tools. You can run this bot in two ways, chatbot mode and userbot mode. If you're willing to use this bot as a userbot then you are ready to go but if you're willing to use this bot as a seperate chatbot then you would need a bot token. You can make a bot using BotFather ([Tutorial](https://blog.devgenius.io/how-to-set-up-your-telegram-bot-using-botfather-fd1896d68c02#:~:text=Who%20is%20BotFather,bot%27s%20token%20again.)) and get your bot token

- I would recommend using chatbot mode since it doesn't require any interaction so it can be hosted on almost any server whereas userbot mode would require you to sign in with your account in the shell so you might face difficulties hosting it on your preffered server

- Next step is to decide the personality of the bot, you can define the personality of the bot such as "Act like a friendy guy" or "Be like a rude teenager" etc. You can also give bot some of your personal knowledge such as "Hello bro, how are you?" and at last, think of a name for your bot. Gather all of the information we collected till now for the next step

- Next step is to fill up the required information that we collected, If you are hosting the bot locally then you can either fill up the config_file.py or set api_id, api_hash, name, bot_token, instruction, knowledge in the os enviroment but if you're hosting bot online then I would suggest you to set enviroment variables in the hosting service itself. Also make sure if your hosting service provides interactive UI if you're going for userbot mode

- The last step is to fire up the bot, just run the bot using a python interpreter. Initial execution can take upto 10 minutes since model will be downloaded and initial machine learning executions will be slow. Once your bot is executed, the next time you run it, it can take less then 1/10th the time of initial bootup. That's it, Thank you!
