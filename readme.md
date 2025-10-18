# Heiliger Carsten Discord Bot

A Discord bot built with Python that responds to commands

## Features

- **$hello** - Bot responds with "Hello World!"
- **$meme** - Bot sends a random meme using the Meme API

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/mxmkrg/heiliger_carsten_discord_bot
   cd heiliger_carsten_discord_bot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your Discord Bot Token:

     ```bash
     DISCORD_TOKEN=your_token_here
     ```

   - Get your token from the [Discord Developer Portal](https://discord.com/developers/applications)

4. **Run the bot**

   ```bash
   python main.py
   ```

## Usage

Once the bot is running and added to your Discord server, you can use the following commands:

- Type `$hello` in any channel to get a greeting
- Type `$meme` in any channel to receive a random meme

## Requirements

See `requirements.txt` for the full list of dependencies. Main packages include:

- discord.py
- requests
- python-dotenv

## Sources

[Codedex Tutorial Link](https://www.codedex.io/projects/build-a-discord-bot-with-python)
