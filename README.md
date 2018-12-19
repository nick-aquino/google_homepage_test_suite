# google_homepage_test_suite

This repository is a Framework using Python 3 and Selenium for testing webpages. 
The included test suite will execute some tests on Google's homepage.

## Table of Content

- [Installation](#installation)
- [Usage](#usage)
- [Reporting](#reporting)

## Installation

To install google_homepage_test_suite: 

1. Clone this repository via git
2. Install requirements via requirements.txt

```batch
    $ pip install -r requirements.txt
```

3. Download and add the Selenium webdrivers to your PATH

The following are supported:
- Firefox: https://github.com/mozilla/geckodriver/releases
- Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads

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
