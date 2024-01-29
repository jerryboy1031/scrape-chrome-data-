# scape-chrome-data-
### How to login the website? / How to google a specific word and scape the results automatically? learn to scape online data (search results) from google chrome.
<p align="center">
    <img src="/scape.png" width="400">
    <br>
    <sup>Game cover designed by 陳佳俊
    </sup>
</p>

Sometimes, we are tired of searching for a topic or something, and finding the important information from massive results. How about letting the computer search and pick the results for us? [**scape-chrome-data-**](https://github.com/jerryboy1031/scrape-chrome-data-) uses python modules `selenium` and `bs4` to help us scrape the data from web. Then, it writes the results it pick on a csv file. The only thing we do is to open the csv and take a look.

It is **authored by** [**陳佳俊**](https://github.com/jerryboy1031). It is **maintained by** [**陳佳俊**](https://github.com/jerryboy1031).


## Contents
1. [Results](#results)
2. [Features](#features)
3. [Contributors](#contributors)
4. [Installation](#installation)
5. [Send Us Feedback!](#send-us-feedback)
6. [License](#license)



## Results
### Gameplay
<p align="center">
    <img src=".vs/figs/gameplay1.png" width="300">
</p>


## Features

- **[handle_search_result.py](https://github.com/jerryboy1031/scrape-chrome-data-/blob/main/handle_search_result.py)** 
    - **extract_website(string)**:
        -  start
        - open a google chrome website
        - search a specific title (i.e. 法國自由行)
        - extract data(titles, urls) from the result

    - **saveTOcsv(data)**
        - open a csv file "google_search_results.csv" with writting mode, and encoded with utf-8
        - save the data to a csv file, and add a header row


- **[login_fb.py file](https://github.com/jerryboy1031/scrape-chrome-data-/blob/main/login_fb.py)**
    - use senlenium to automate the web browser- open a google chrome website
    - to login a website (i.e. FB) with email and password (without verification code)

## Contributors
- [**陳佳俊**](https://github.com/jerryboy1031)



## Send Us Feedback!
Our library is open source for research purposes, and we want to improve it! So let us know (create a new GitHub issue or pull request, email us, etc.) if you...
1. Find/fix any bug (in functionality or speed) or know how to speed up or improve any part of OpenPose.
2. Want to add/show some cool functionality/demo/project made on top of it. We can add your project link to our project.

## License
OpenPose is freely available for free non-commercial use, and may be redistributed under these conditions. Please, see the [license](./LICENSE) for further details.
