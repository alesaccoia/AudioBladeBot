# AudioBlade Bot 🎵🤖

Welcome to AudioBlade Bot, IULM AI Lab's Discord bot that's slicing through the complexity of generative MIDI solutions like a hot knife through butter! 🎹🔪 Designed for musicians, creators, and anyone in between, AudioBlade Bot brings your MIDI files to life directly within your favorite Discord channels.

## Features 🌟

- **MIDI to MP3 Conversion**: Simply attach a MIDI file to your message, and watch as AudioBlade Bot converts it to an easily shareable MP3 file. 🎼➡️🎧
- **Command-Line Friendly**: Start the bot with just your token and let it handle the rest. Perfect for both beginners and seasoned command-line warriors. 🖥️👾
- **Intuitive Usage**: With a simple `!playmidi` command, converting and sharing your music is as easy as pie. 🍰
- **Clean-Up System**: No leftover files cluttering your space. AudioBlade Bot takes care of the mess after each conversion. 🧹✨

## Getting Started 🚀

Before you can use AudioBlade Bot, make sure you have a Discord bot token. If you don't, check out [Discord's developer portal](https://discord.com/developers/applications) to create your bot and get one.

### Prerequisites

- Python 3.x
- `discord.py` library
- `ffmpeg` and `timidity` for audio conversion
- On Linux:
    sudo apt-get install timidity
    sudo apt-get install ffmpeg

### Running the Bot

1. Clone this repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `ffmpeg` and `timidity` are installed on your system.
4. Run the bot with your Discord bot token:
   ```bash
   python audiobladebot.py <Your_Bot_Token>
   ```

## Usage 📖

To convert a MIDI file to MP3, simply join a Discord channel where AudioBlade Bot is present and attach a MIDI file with the `!playmidi` command. The bot will take care of the rest, providing you with a fresh MP3 file.

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions to improve AudioBlade Bot are **greatly appreciated**.

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.
