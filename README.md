[![Build Status](https://travis-ci.org/HenryFBP/ITMS448-osint-dashboard.svg?branch=master)](https://travis-ci.org/HenryFBP/ITMS448-osint-dashboard)

# OSINT Dashboard

This is a final project for ITMS448 at IIT: 

An OSINT dashboard for gathering intelligence from multiple sources.

We are focusing on domestic terrorism.

## Setup

Clone or download this repository.

All commands take place in the repo's directory.

Install Python 3.6 or higher.

`pip install pipenv` installs a Python environment manager.

`pipenv install` installs dependencies specified in `/Pipfile`.

`pipenv shell` opens a shell with all your Python deps installed.

Without this, the deps installed from `pipenv install` aren't referred to when you type `python`.

## Running

### The 4plebs web API scraper 

`cd bowser/`

`python bowser.py`

### The scrapy test

`cd scrapy/`

`scrapy runspider testScrapyProject/testScrapyProject/spiders/aarchivedmoe.py`

## Team

### George Lonngren
Role: Project Manager

### Henry Post
Role: Developer

### Michael Kotyar	
Role: Full Stack Developer

### Daniel Denekew
Role: Analysts - Generate Development

### Rawad Alahmadi
Role: TBD

### Robert Bacius
Role: TBD
