# Telegram YouTube Bot

This Telegram bot allows users to interact with YouTube channels through Telegram. It requires users to subscribe to a specific channel before they can access its features.

## Setup
1. **Clone the Repository**: `git clone https://github.com/IAP-programs/TeleTubeBot`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Configuration**:
   - Add your Telegram bot token to `bot_token`.
   - Obtain the YouTube API key and add it to `api_key`.
   - Enter the channel ID of the YouTube channel in `channel_id`.

## Obtaining Channel ID
To obtain the channel ID of a YouTube channel:
1. Go to the channel page on YouTube.
2. Click on the channel name to go to the channel's homepage.
3. Copy the URL from the browser's address bar.
4. The channel ID is the string of characters after "channel/" in the URL.

## Obtaining YouTube API Key
To obtain a YouTube API key:
- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project if you haven't already.

### 2. Enable the YouTube Data API v3

- In the Google Cloud Console, navigate to API & Services > Library.
- Search for "YouTube Data API v3" and enable it for your project.

### 3. Create credentials

- After enabling the API, go to API & Services > Credentials.
- Click on "Create credentials" and select "API key". This will generate an API key and copy the key 


## Usage
1. **Run the Bot**: `python bot.py`
2. **Adding Data**: Run `add_data.py` to add responses or data required for the bot.

## Contributing
Feel free to contribute to this project by forking and submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project is inspired by the need for Telegram bots to interact with YouTube channels seamlessly.
