# OSINT Dashboard: Bowser

[![Build Status](https://travis-ci.org/Team-Bowser-ITMS-448/ITMS448-osint-dashboard.svg?branch=master)](https://travis-ci.org/Team-Bowser-ITMS-448/ITMS448-osint-dashboard)

[![Coverage Status](https://coveralls.io/repos/github/Team-Bowser-ITMS-448/ITMS448-osint-dashboard/badge.svg)](https://coveralls.io/github/Team-Bowser-ITMS-448/ITMS448-osint-dashboard)

This is a final project for ITMS448 at IIT:

An OSINT dashboard for gathering intelligence from multiple sources.

The project's name is Bowser, named after [Mary Bowser](https://en.wikipedia.org/wiki/Mary_Bowser).

We are focusing on domestic terrorism.

## Setup

Clone or download this repository.

All commands take place in the repo's directory.

Install Python 3.6 or higher.

`pip install pipenv` installs a Python environment manager.

`pipenv install --dev` installs dependencies plus dev deps specified in `/Pipfile`.

`pipenv shell` opens a shell with all your Python deps installed.

Without this, the deps installed from `pipenv install` aren't referred to when you type `python`.

## Running

### Bowser (The 4plebs web API scraper)

`cd bowser/`

`python bowserScraper.py`

Running this will generate a CSV file in `bowser/out/`.

Edit the end of `bowser.py` to make larger CSV files or gather from different boards.

### The scrapy test

`cd scrapy/`

`scrapy runspider testScrapyProject/testScrapyProject/spiders/aarchivedmoe.py`

## Team

### George Lonngren

Role: Project Manager

### Henry Post

Role: Full-Stack Developer

### Michael Kotyar

Role: DevOps Engineer

### Cooper Van Kampen

Role: Machine Learning AI Cloud Malware Devloper (Agile)

### Daniel Denekew

Role: Analysts - Big DataGenerate Development

### Rawad Alahmadi

Role: Project Assitant, Machine Language Data Scientist

### Robert Bacius

Role: Cloud AI Data Analysis

## Extra Documentation

4plebs API documentation:

<https://archive.4plebs.org/_/articles/faq/>

Other adjacent tools:

<https://github.com/eksopl/asagi>

<https://github.com/FoolCode/FoolFuuka>

### Interesting links

<https://github.com/Grayson112233/python-4chan-scraper/>

### Keyword sources

A list of sources for keywords whose use may indicate terrorist activity.

<http://cryptome.org/2014/01/nsa-codenames.htm>

<https://buggedplanet.info/index.php?title=Category:NSA_codewords>

<https://www.businessinsider.com/nsa-prism-keywords-for-domestic-spying-2013-6>

<https://www.theregister.co.uk/2001/05/31/what_are_those_words/>

<http://www.scribd.com/doc/82701103/Analyst-Desktop-Binder-REDACTED>

<https://www.dailymail.co.uk/news/article-2150281/REVEALED-Hundreds-words-avoid-using-online-dont-want-government-spying-you.html#ixzz1w1SkH6gY>

<https://github.com/mogade/badwords/blob/master/en.txt>
