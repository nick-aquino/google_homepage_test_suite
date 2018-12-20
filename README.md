# google_homepage_test_suite

This repository is a Testing Framework using Python 3.6 and Selenium for testing webpages. 
The included test suite will execute some tests on Google's homepage.

## Table of Content

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Reporting](#reporting)


## Requirements

- Python 3.6
- pip
- Webdrivers for Chrome and Firefox (Added to PATH)
    - Firefox: https://github.com/mozilla/geckodriver/releases
    - Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads

## Installation

To install google_homepage_test_suite: 

1. Clone this repository via git
2. Install requirements via requirements.txt

```batch
    $ pip install -r requirements.txt
```

## Usage

You can execute the test suite on all supported browsers with the following command:

```batch
    $ python test_runner.py
```

To specify a browser (currently 'chrome' and 'firefox') you can add it as an argument.

For Example here is how you can execute on chrome only:

```batch
    $ python test_runner.py chrome
```

## Reporting

- Reports will be generated in /reports directory as TestResults_*_[timestamp].html
- Reports are in HTML and can be viewed in browser.
- Any Errors or Failures can be expanded to view traceback
