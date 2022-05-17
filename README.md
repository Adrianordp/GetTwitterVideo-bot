# getTwitterVideo tool
This tool helps you to easly download the lastest videos from any public twitter account.

## Requirements
Before you use it, install required `pip` dependencies:
```bash
pip install yt_dlp
pip install pytwitter
pip install requests
```

## How to use it
Clone this repository locally, then setup the right settings for your twitter API bot as shown in this next session.

### First-use only setup
First, [create a twitter developer account](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) to obtain a bearer token.

Inside this project's path, find the `config-example.json` file:
```json
// config-example.json
{
    "bearer_token": "Your bearer token here"
}
```
Rename it to `config.json`. Then paste you bearer token into the designated area.

Your tool is ready to use!

### Running

In a command line console pointing at this project's path, run:
```bash
python3 main.py
```

On the interface, type the username you want the videos from and how many of the their latest videos you want to download.

Click on download and the video file will be downloaded to the same path of your `main.py`script.