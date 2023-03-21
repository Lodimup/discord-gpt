# discord-gpt
ChatGPT in discord baby!

Shouts `TOMATO!` every messages.

# Usage
## Requirements
docker installed [link](https://www.docker.com)
## How to
* get OpenAI token [link](https://platform.openai.com/account/api-keys) You get $18 credits for free!
* create a bot in discord developer portal and invite it to your server. [link](https://discord.com/developers/applications)
* get your discord guild id [link](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)
rename `.env.sample` to `.env` and fill in the blanks.  
```
make
```
That's it!

# Notes
* You might want to edit `DEFAULT_SYSTEM_MESSAGE` in main.py
* On windows make will fail because of there is no `make` command. You can just run the commands in the makefile manually, or use WSL
