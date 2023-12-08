"""
Written By: Bishwas Bhatt
Purpose: Downloads PDFs from a certain slack channel into a local repo, and flags it as downloaded in another channel

------- GET STARTED -------
1. Install Packages/Libraries
2. Creating an app, and getting SlackAPI Token and put it into .env file
3. Add the bot into slack channels that are going to be used in this application through integration menu in channel details

------- Packages Installation Guide -------
pip install python-dotenv
pip install slackclient

------- HOW TO CREATE SLACK APP AND GET SLACKAPI TOKEN -------
https://api.slack.com/start/quickstart


------- Additional Installation Guide -------

Some devices may have issues with downloading slackclient library due to some packages not being up-to-date.
Do the following steps if thats the case:
1. Go to: https://www.lfd.uci.edu/~gohlke/pythonlibs/
2. Download the latest versions of the following packages: multidict, frozenlist, aiohttp
3. Make sure you are in the same directory where these packages resides and then open terminal in that directory
4. Run the command for all 3 packages: pip install packagename 
   Example: pip install multidict‑6.0.2‑py3‑none‑any.whl

Resources: 
Getting started with SlackAPI Tutorial: https://www.youtube.com/watch?v=KJ5bFv-IRFM
Conversations.History method: https://api.slack.com/methods/conversations.history
Slack API Tester: https://api.slack.com/methods/conversations.history/test
Sample Code: https://api.slack.com/methods/conversations.history/code
"""

import os
import time
import requests

from pathlib import Path
from dotenv import load_dotenv

from slack import WebClient
from slack.errors import SlackApiError

from datetime import datetime


# Import the environment file that has the slack bot token
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# This decides where the downloaded pdfs will go. Currently setup as a current directory under Downloads folder
DOWNLOAD_PATH = 'Downloads'

def download_pdf(file_url, file_name):
    response = requests.get(file_url)
    with open(os.path.join(DOWNLOAD_PATH, file_name), 'wb') as f:
        f.write(response.content)
def get_latest_timestamp():
    # replace the channel="" with the channelID found under channel details in slack
    result = client.conversations_history(channel="C0680KESRPX", latest=None)
    messages = result['messages']
    oldest_message = messages[0]
    latest_timestamp = oldest_message['ts']
    return latest_timestamp

def monitor_slack_channel():
    latest_timestamp = get_latest_timestamp()
    latest_timestamp = datetime.fromtimestamp(int(float(latest_timestamp)))
    print(f"Processing message with timestamp: {latest_timestamp}")
    while True:
        try:
            # replace the channel="" with the channelID found under channel details in slack
            result = client.conversations_history(channel="C0680KESRPX", latest=latest_timestamp)
            messages = result['messages']

            if messages:
                latest_message = messages[0]
                current_timestamp = latest_message['ts']
                current_timestamp = datetime.fromtimestamp(int(float(current_timestamp)))
                print(f"Processing message with timestamp: {current_timestamp}")
                
                    

                # Update the latest_timestamp if the current message has a later timestamp
                if latest_timestamp is None or current_timestamp > latest_timestamp:
                    if 'files' in latest_message:
                        for file_info in latest_message['files']:
                            if file_info['filetype'] == 'pdf':
                                file_url = file_info['url_private_download']
                                file_name = file_info['name']
                                download_pdf(file_url, file_name)
                                print(f"Downloaded {file_name}.")
                                #replace #random with the slack channel you will be using
                                client.chat_postMessage(channel="#random", text="Downloaded " + file_name)
                    latest_timestamp = current_timestamp
                 

        except SlackApiError as e:
            print(f"Error: {e.response['error']}")

        time.sleep(10)  # Adjust the interval as needed (e.g., 1 second)

if __name__ == "__main__":
    monitor_slack_channel()
