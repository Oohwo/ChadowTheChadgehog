# Chadow the Cedgehog
-----
*Chadow* is a Discord bot written in Python that spits out a random quote from Snapcube's Sonic the Hedgehog Fandubs!

The bot is currently being hosted on [railway.app](https://railway.app) and I'm using Airtable to store all my data. 

Invite link: [later]

## Demo

![Demo](https://cdn.discordapp.com/attachments/1030373948694728764/1033689034742046820/Testing_BlurbBot.gif)

## Current Features
`/quote` - Generate a random quote!

## Installation
1. Download this repo
2. Navigate to the bot directory via Terminal
3. Create a virtual environment: 
- Mac: `python3 -m venv bot-env`
- Windows: `py -3 -m venv bot-env` 
4. Activate the virtual environment: 
- Mac: `source bot-env/bin/activate`
- Windows: `bot-env\Scripts\activate.bat`
5. Install the needed libraries: 
- Mac: `pip install -r requirements.txt`
- Windows: `py -3 -m pip install -r requirements.txt`
6. Create a `.env` file with:
- `DISCORD_BOT_TOKEN = ''`
- `DISCORD_BOT_APP_ID = ''`
7. Run `main.py`

## Notes

## TODO
[] Add list of characters embed
[] Filter by character
[] Show list of lines by [character]