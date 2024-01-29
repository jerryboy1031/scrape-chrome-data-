# scape-chrome-data-
### How to login the website? / How to google a specific word and scape the results automatically? learn to scape online data (search results) from google chrome.
<p align="center">
    <img src="/scape.png" width="600">
    <br>
    <sup>Game cover designed by 陳佳俊
    </sup>
</p>

[**scape-chrome-data-**](https://github.com/jerryboy1031/scrape-chrome-data-) is a video game. It features a beautiful game scene,  delicated actions, and two characters: a Ninja and Romans soldier, fighting until one of them is dead. 
What's more, the tints (i.e. hurt tint) and actions are beyond description.

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
    <img src=".vs/figs/gameplay2.png" width="300">
    <img src=".vs/figs/gameplay3.png" width="300">
    <br>
    <sup>Start fighting scene(Left), Attack action(Center), hurting tints(Right) 
</p>


## Features
- **extract_website(string)**:
    -  start
    -  exit
    -  icon

<p align="center">
    <img src="image/move1.png" width="100">
    <img src="image/move21.png" width="100">
    <br>
</p>

- handle_search_result.py
  - open a google chrome website
  - search a specific title (i.e. 法國自由行)
  - extract data(titles, urls) from the result

- **saveTOcsv(data)**
   - open a csv file "google_search_results.csv" with writting mode, and encoded with utf-8
   - save the data to a csv file, and add a header row

     1. login_fb.py file
   ### use senlenium to automate the web browser
- open a google chrome website
- to login a website (i.e. FB) with email and password (without verification code)

## Contributors
- [**陳佳俊**](https://github.com/jerryboy1031)



## Send Us Feedback!
Our library is open source for research purposes, and we want to improve it! So let us know (create a new GitHub issue or pull request, email us, etc.) if you...
1. Find/fix any bug (in functionality or speed) or know how to speed up or improve any part of OpenPose.
2. Want to add/show some cool functionality/demo/project made on top of it. We can add your project link to our project.

## License
OpenPose is freely available for free non-commercial use, and may be redistributed under these conditions. Please, see the [license](./LICENSE) for further details.
