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
