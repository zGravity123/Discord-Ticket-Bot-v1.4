# Discord Ticket Bot

A professional, asynchronous Discord bot designed for advanced ticket management. Features include an automated configuration wizard, HTML transcript generation, and a comprehensive feedback system.

## Overview

The Zen Ticket System is built with Python and `discord.py`. It is designed to handle customer support workflows efficiently. Key capabilities include:

- **Automated Asset Installation:** Automatically uploads required emojis and banners from a local directory to the Discord server.
- **Interactive Configuration:** Step-by-step slash command wizard to set up roles, categories, and logging channels.
- **Transcripts:** Generates HTML logs of closed tickets using `chat-exporter`.
- **Feedback Loop:** Collects user ratings and comments post-service via Direct Messages.

## Prerequisites

- Python 3.10 or higher
- A Discord Bot Token (with Message Content and Server Members Intents enabled)
- Git

## Directory Structure

The application requires a specific directory structure to function correctly, particularly for the asset loader. Ensure your project folder looks like this:

```
text
/TicketSystem
│
├── bot.py                 # Main entry point (Loader)
├── example.env            # Template file (Rename to .env)
├── config.json            # Auto-generated configuration file
├── requirements.txt       # Python dependencies
│
├── cogs/
│   └── tickets.py         # Main ticket logic
│
└── emojis/                # Required asset folder
    ├── banner-ticket.png  # Main panel banner (Large image)
    ├── camera.png         # Image attachment icon
    ├── certo.gif          # Confirm action
    ├── errado.gif         # Cancel/Close action
    ├── estrela.png        # Rating star
    ├── info.png           # Info button icon
    ├── livro.png          # Generic icon
    ├── notas.gif          # Feedback notes icon
    └── sirene.png         # Alert icon
```


## Installation

Follow these steps to set up the bot locally:

### 1. Clone the repository


git clone [https://github.com/zGravity123/TicketSystem.git](https://github.com/zGravity123/TicketSystem.git)
cd TicketSystem

```markdown
## Installation

### Install dependencies

```bash
pip install discord.py chat-exporter python-dotenv colorama aioconsole

```

## Configuration

1. **Rename the environment file:**
Rename `example.env` to `.env` to configure your secrets.
```bash
mv example.env .env
# Or manually rename via your file explorer

```


2. **Setup your Token:**
Open the `.env` file with a text editor and insert your bot token:
```env
DISCORD_TOKEN=your_discord_bot_token_here

```



## Running the Bot

Start the bot using Python:

```bash
python bot.py

```

## Setup & Usage

Once the bot is online, use the following Slash Commands in your Discord server to configure the system.

### 1. Asset Installation

**Command:** `/setup_emojis`

**Description:** Reads the local `emojis/` directory, uploads all assets to the server, and maps their IDs for the bot to use. This must be run first.

### 2. System Configuration

**Command:** `/config_ticket`

**Description:** Launches the configuration wizard.

* **Step 1:** Welcome & Support.
* **Steps 2-6:** Selects the Staff Role, Open Ticket Category, Claimed Ticket Category, Transcript Channel, and Feedback Channel.

### 3. Deploy Panel

**Command:** `/ticket_panel`

**Description:** Deploys the main support embed with the interaction button to the current channel.

## Dependencies

* discord.py
* chat-exporter
* python-dotenv
* aioconsole
* colorama

## License

This project is open-source and free for anyone to use.

```

```
