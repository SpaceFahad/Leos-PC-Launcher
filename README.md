<br/>
<p align="center">
  <a href="https://github.com/SpaceFahad/Leos-PC-Launcher">
    <img src="https://i.imgur.com/oigcXpj.png" alt="Logo" width="300" height="300">
  </a>

  <h3 align="center">Leo's PC Launcher</h3>

  <p align="center">
    A Python coded discord bot that would launch/excute files on your computer (where the bot is hosted) when a command on discord is used.
    <br/>
    <br/>
    <br/>
    <a href="https://github.com/SpaceFahad/Leos-PC-Launcher/issues">Report Bug</a>
    .
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/SpaceFahad/Leos-PC-Launcher/total) ![Forks](https://img.shields.io/github/forks/SpaceFahad/Leos-PC-Launcher?style=social) ![Stargazers](https://img.shields.io/github/stars/SpaceFahad/Leos-PC-Launcher?style=social) ![Issues](https://img.shields.io/github/issues/SpaceFahad/Leos-PC-Launcher) ![License](https://img.shields.io/github/license/SpaceFahad/Leos-PC-Launcher) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](https://i.imgur.com/T8lxvV2.png)

This Discord bot, built using Python, empowers users to remotely execute files on their host computer directly from a Discord server. With a simple command trigger (/run), users can initiate the execution of various file types, including .bat, .lnk, .exe, and more, all within the Discord environment.

Features:
* Role-Based Permissions
* File Flexibility
* Channel Restriction
* Logging Capabilities
* Custom Responses


## Built With

Python 3.12.1

## Getting Started

Tested on: 
* Windows 11
* Windows 10
* Windows Server 2022
* Windows Server 2016

### Prerequisites

* [Python](https://www.python.org/downloads/) (Recommended: 3.12.1)
 

`Make sure to select add to PATH when installing Python`

### Installation

1. Create a bot and get a **token** from [Discord Developer Portal](https://discord.com/developers/applications)
`Make sure to enable all three Privileged Gateway Intents` ([Screenshot](https://i.imgur.com/3yBfslP.png))

2. Clone/Download the repo

3. Install Requirements

```python
pip install -r requirements.txt
```

4. Rename .env.example to .env and add your token and your log channel ID

```
DISCORD_TOKEN=<Token Here>
LOGS_CHANNEL_ID=<Log Channel ID Here>
```

3. Configure `config.yaml`


6. Run/Start `Leos-PC-Launcher.py`


### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/SpaceFahad/Leos-PC-Launcher/blob/main/LICENSE) for more information.

## Authors

* **SpaceFahad** - *a nub on* - [SpaceFahad](https://github.com/SpaceFahad/) - *Github*

## Acknowledgements

* [SpaceFahad](https://github.com/SpaceFahad/)
