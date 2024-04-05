# Telegram YouTube Bot

This Telegram bot allows users to interact with YouTube channels through Telegram. It requires users to subscribe to a specific channel before they can access its features.

## Setup
1. **Clone the Repository**: `git clone https://github.com/IAP-programs/TeleTubeBot`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Configuration**:
   - Add your Telegram bot token to `bot_token.txt`.
   - Obtain the YouTube API key and add it to `api_key.txt`.
   - Enter the channel ID of the YouTube channel in `channel_id.txt`.

## Obtaining Channel ID
To obtain the channel ID of a YouTube channel:
1. Go to the channel page on YouTube.
2. Click on the channel name to go to the channel's homepage.
3. Copy the URL from the browser's address bar.
4. The channel ID is the string of characters after "channel/" in the URL.

## Obtaining YouTube API Key
To obtain a YouTube API key:
1. Sign in to [Google Developer Console](https://console.developers.google.com/).
2. Create a new project.
3. Enable the YouTube Data API.
4. Create an API key and save it securely.

## Usage
1. **Run the Bot**: `python bot.py`
2. **Adding Data**: Run `add_data.py` to add responses or data required for the bot.

## Contributing
Feel free to contribute to this project by forking and submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project is inspired by the need for Telegram bots to interact with YouTube channels seamlessly.
