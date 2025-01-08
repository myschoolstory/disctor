## Project Overview

This project is a Discord bot designed to interact with the BitTorrent network. It allows users to download, upload, and seed torrents directly from a Discord server. The bot is built using `discord.py` and `libtorrent`.

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Bot**:
   - Open `src/config.py`.
   - Replace `'your-discord-bot-token-here'` with your actual Discord bot token.
   - Adjust the paths for downloads, uploads, and seeds if necessary.

## Usage Instructions

1. **Run the Bot**:
   Start the bot by executing:
   ```bash
   python src/bot.py
   ```

2. **Bot Commands**:
   - **Download a Torrent**: `!download <torrent_url>`
   - **Upload a Torrent**: `!upload <file_path>`
   - **Seed a Torrent**: `!seed <torrent_url>`

   Replace `<torrent_url>` and `<file_path>` with the actual URL or file path you wish to use.

3. **Interacting with the Bot**:
   - Use the commands in any Discord channel where the bot is present.
   - The bot will respond with status messages indicating the success or failure of each operation.

## Additional Information

- Ensure your Discord bot has the necessary permissions to read and send messages in the channels you intend to use it.
- The bot's performance and capabilities depend on the network and system resources available.
