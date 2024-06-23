# Z01 Group Maker

Better group creation for projects for Z01.

# Useful Infos
1. **Make sure you have pip installed**<br>
```sh
sudo apt install python3-pip
```
2. **Install the required python packages**<br>
```sh
python3 -m pip install -r requirements.txt
```

3. **Read the API documentation**<br>
[discord.py](https://discordpy.readthedocs.io/en/stable/)<br>
<br>

# The Bot

We have noticed a lot of difficulties regarding the fact of creating groups to work together during our internship. Some people were not changing groups, some of them couldn't find a group to work on a project, etc...

This bot was made to help our colleagues have a better opportunity to find groups to suits them, along with their project.

This bot was fully written in Python, uses an SQL database and the discordpy module.

### How does it work ?

When the bot is up and running, you can create a group with the slash command:
```bash
/create <project_name>
``` 

The provided project name is checked to see if its a valid project that is really in our project list. Once done, the bot sends an Embed where people have different actions. You can:

* Join the group
* Leave the group
* Delete the group
* Lock the group
