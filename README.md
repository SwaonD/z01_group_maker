## Description
This discord bot helps you create and join groups for certain projects of Zone01 school.
It is fully written in Python using [discord.py](https://discordpy.readthedocs.io/en/stable/) API and also store the data in a database with SQLite.

We have noticed a lot of difficulties regarding the fact of creating groups to work together during our internship. Some people were not changing groups, some of them couldn't find a group to work on a project, etc...

This bot was made to help our colleagues have a better opportunity to find groups to suits them, along with their project.

## Configuration
1. **Create your application and get your discord bot token**<br>
https://discord.com/developers/applications

2. **Add the following line with your token to a file called .env at the root of the directory**<br>
```sh
Z_01_GROUP_MAKER_DISCORD_BOT_TOKEN="<DISCORD_BOT_TOKEN>"
```
3. **Install the required python packages**<br>
```sh
python3 -m pip install -r requirements.txt
```
4. **Launch the bot**<br>
```sh
python3 main.py
```
### Dev Tools
- You can also add to your .env file a variable which store the discord ids of the devs to get access of advanced commands.
Here is the format:
```sh
Z_01_GROUP_MAKER_DEVS_IDS=xxxxxxxxxxxxxxx,xxxxxxxxxxxxxxx,xxxxxxxxxxxxxxx
```
To see which commands are available, send `!help`.

## Quick Start
1. **Install the bot on your server**<br>
https://discord.com/oauth2/authorize?client_id=1253304421983588422
2. **Configure the channel where the group messages will be sent**<br>
`/config channel:#my_text_channel`
3. **Create your first group using the project names on Zone01's website**<br>
`/create project:ascii-art`

## Commands
- /create<br>
	*Create a group. See the [valid group names](./data/project_names.txt).*
- /list<br>
	*List every groups.*
- /status<br>
	*A shortcut of /list but for the current user*
- /kick<br>
	*Kick a member of your group.*
- /config<br>
	*Admin command, it configure the channel where the group message will be sent.*
