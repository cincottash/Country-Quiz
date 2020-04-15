# Reddit Scraper

A mining tool for reddit.

## Features

* Scrapes any subreddit for input search token.<br/>

* Ability to return different data for certain subreddits.<br/>

* Sends post information to user via SMS.<br/>

* Short update period of 10 seconds, see results in quickly in real time.<br/>

## Prerequisites

A list of required libraries is located in requirments.txt and can be installed via Pip with 

```pip install -r requirments.txt```

## Built With

* Python3

* [PRAW](https://praw.readthedocs.io/en/latest/getting_started/installation.html) - Reddit API used to fetch posts.

* [Twilio](https://www.twilio.com/docs/quickstart/python) - SMS texting API used to send alerts to phone.

## Authors

* **[Shane Cincotta](https://github.com/cincottash)**

* **[Cerrach](https://github.com/cerrachiochris)**

## Usage

### If scraping /r/hardwareswap or /r/steamgameswap:
&nbsp;&nbsp;&nbsp;&nbsp;
```python3 main.py SubredditName BuyOrSell SearchToken```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* SubredditName = The string following /r/. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* BuyOrSell = [H] or [W], [H] indicates you want to buy the search token, [W] implies you want to sell the search token.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* SearchToken = The word you're scraping for.<br/>
### Otherwise:
&nbsp;&nbsp;&nbsp;&nbsp;
```python3 main.py SubredditName SearchToken```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* SubredditName = The string following /r/. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* SearchToken = The word you're scraping for.<br/>

### /r/hardswareswap, steamgameswap and buildapcsales subreddits will return price data.<br/>

## Known Issues
* No custom exception is thrown when program is ran with 0 arguments.

## Acknowledgments

Thanks to Cerrach for helping developing the alpha version of this tool.