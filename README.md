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

#### Generating CSV files via the command line

`cd bowser/`

`python bowserScraper.py`

Running this will generate a CSV file in `bowser/out/`.

Edit the end of `bowser.py` to make larger CSV files or gather from different boards.

#### Web UI

`cd client` and run `npm build`.

This generates JS and HTML that will be served under `0.0.0.0:1839/` as Flask static files.

Alternatively, you can run `npm start` if you wish to run the web UI under Node.js.

#### Web API/Static web interface

`cd bowser`

`python bowserHTTPAPI.py`

This will start an HTTP API on <http://0.0.0.0:1839/api>.

Also, a web UI from Node.js static files will be served on <http://0.0.0.0:1839/>.

This web UI must be built using `npm` as described in the "Web UI" section.

##### Heroku instance

Alternatively, <http://bowser-webapi.herokuapp.com/api> can be used if you need to access it over the internet and not locally.

The Heroku app may fail due to Cloudflare WAF blocking Heroku's IPs. Running it locally should prevent this.

##### DigitalOcean instance

<http://bowser-web-app.freemyip.com:1839> can be used with no restrictions to browse a live version of our project. Try going to `/api`!

### The scrapy test

`cd scrapy/`

`scrapy runspider testScrapyProject/testScrapyProject/spiders/aarchivedmoe.py`

## Node.js Web Client

See `/client` for a more detailed README file.

Project was bootstraped with 
Template: [https://www.creative-tim.com/product/material-dashboard-react](https://www.creative-tim.com/product/material-dashboard-react#)

- If using VS Code need [Flow extension](https://marketplace.visualstudio.com/items?itemName=flowtype.flow-for-vscode)

    Name: Flow Language Support  
    Id: flowtype.flow-for-vscode  
    Description: Flow support for VS Code  
    Version: 1.5.0  
    Publisher: flowtype 
    VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=flowtype.flow-for-vscode

- Turn off VS Code default javascript/script checker
  - Create a .vscode directory at root project level
  - Create a .vscode/settings.json file
  - copy json into the file

```json
{
  "extensions.enabled": [
    /*whatever extensions wanted to be*/
  ],
  "extensions.disabled": ["vscode.typescript-language-features"]
}
 ```

## Team

### George Lonngren

Role: Project Manager

### Henry Post

Role: Backend Developer

### Jarron Bailey

Role: Frontend Developer

### Michael Kotyar

Role: DevOps Engineer

### Cooper Van Kampen

Role: Machine Learning AI Cloud Malware Devloper (Agile)

### Daniel Denekew

Role: Analysts - Big Data Generate Development

### Rawad Alahmadi

Role: Project Assistant, Machine Language Data Scientist

### Robert Bacius

Role: Cloud AI Data Analysis

## Extra Documentation

4chan API:

<https://github.com/4chan/4chan-API>

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

<https://epic.org/foia/epic-v-dhs-media-monitoring/Analyst-Desktop-Binder-REDACTED.pdf>
