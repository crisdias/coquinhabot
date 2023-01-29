# Amazon Affiliate Bot

A Discord bot that monitors Amazon links and adds an affiliate link.

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/<repository_name>.git`
2. Install required packages using `pip install -r requirements.txt`
3. Create a Discord bot and invite it to your server by following the [Discord Developer Portal guide](https://discord.com/developers/docs/intro).
4. Set the following environment variables:
   - `TOKEN` with your Discord bot token
   - `CLIENT_ID` with your Discord bot client ID
   - `AMAZON_COUNTRY` with the two-letter country code for your Amazon Affiliate program
   - `BITLY` with your Bitly API key (optional)
   - `BITLY_GROUP` with your Bitly Group name (optional)
5. Run the bot using `python bot.py`


### Optional

Create a 'data/frases.txt' file with some phrases to be used by the bot.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

This project was generated using OpenAI's ChatGPT language model.
